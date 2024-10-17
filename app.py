import os

# from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
# [5]
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
import sys


from helpers import error, get_car_data, login_required

# Configure application
app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///test.db")


# [1]
@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# [4]
@app.route("/")
@login_required
def index():
    """Search Manufacturers Locations"""
    if request.method == "GET":
        return render_template("lookup2.html")


# [2]
@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("user"):
            return error("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return error("must provide password", 403)

        # Query database for username
        con = None

        try:
            con = sqlite3.connect('test.db')
            con.row_factory = sqlite3.Row

            cursor = con.cursor()

            # cursor.execute("SELECT * FROM users WHERE username = ?", (request.form.get("user"),))
            cursor.execute("SELECT id, username, password FROM users WHERE username = ?", (request.form.get("user"),))
            info = cursor.fetchall()

            # Check database for username, if username is empty
            if not info:
                return error("Could not find user with that username", 403)

            # for row in info:
                # print(f"{row['id']}, {row['username']}, {row['password']}")

        except sqlite3.Error as e:

            return error("Could not find user with that username", 403)

        finally:

            if con:
                con.close()


        # rows = db.execute(
            # "SELECT * FROM users WHERE username = ?", request.form.get("username")
        # )

        # Ensure password is correct
        for row in info:
            if not check_password_hash(
                row["password"], request.form.get("password")
            ):
                return error("invalid password", 403)

        # Remember which user has logged in
        session["user_id"] = row["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/lookup2", methods=["GET", "POST"])
@login_required
def lookup():
    """Search VIN Number"""
    if request.method == "GET":
        return render_template("lookup2.html")

    if not request.form.get("vin number"):
        return error("VIN cannot be blank", 400)

    else:
        if not request.form.get("year"):
            return error("Year cannot be blank", 400)

    number = request.form.get("vin number")
    year = request.form.get("year")
    search = get_car_data(number, year)
    print(search)

    if search is None:
            return error("Car was not found", 400)

    con = None

    try:
        con = sqlite3.connect('test.db')
        con.row_factory = sqlite3.Row

        cursor = con.cursor()
        cursor.execute("SELECT username FROM users WHERE id = ?", (session["user_id"],))

        info = cursor.fetchone()

        if not info:
            return error("Username not found", 403)

        record = info["username"]

        cursor.execute("INSERT INTO history (id, username, vin, year, time) VALUES (?, ?, ?, ?, CURRENT_TIMESTAMP)", (session["user_id"], record, number, year))
        con.commit()


    except sqlite3.Error as e:

        print(f"Error {e.args[0]}:")
        sys.exit(1)

    finally:

        if con:
            con.close()

    results = []
    for index in search["results"]:
        results.append({"Variable": index["Variable"], "Value" : index["Value"]})
    return render_template("searched.html", results=results)


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")

@app.route("/history", methods=["GET", "POST"])
@login_required
def history():

    # Query database for username
    con = None

    try:
        con = sqlite3.connect('test.db')
        con.row_factory = sqlite3.Row

        cursor = con.cursor()

        cursor.execute("SELECT username, vin, year, time FROM history WHERE id = ?", (session["user_id"],))
        # cursor.execute("SELECT id, username, password FROM users WHERE username = ?", (request.form.get("user"),))
        info = cursor.fetchall()

        # Check database for username, if username is empty
        if not info:
            return error("No History to show", 403)

    except sqlite3.Error as e:

        return error("Could not history that username", 403)

    finally:

        if con:
            con.close()

    return render_template("history.html", info=info)


