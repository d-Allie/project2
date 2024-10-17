import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
import sqlite3
import sys


con = None

name = "Daniel_1"
password = "cocoa"
password_hash = generate_password_hash(password)

try:
    con = sqlite3.connect('test.db')
    con.row_factory = sqlite3.Row

    cursor = con.cursor()
    # cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (name, password_hash))
    # con.commit()

    cursor.execute("SELECT id FROM users WHERE username = ?", (name,))
    # cursor.execute("SELECT password FROM users WHERE username = ?", (password,))
    # cursor.execute("SELECT * FROM users")
    # info = cursor.fetchall()
    info = cursor.fetchone()

    # for row in info:
        # if check_password_hash(row["password"], password):
            # print(f"Password is Correct")
        # else:
            # print("Password is not correct")


    # for row in info:
    print(info["id"])

except sqlite3.Error as e:

    print(f"Error {e.args[0]}:")
    sys.exit(1)

finally:

    if con:
        con.close()
