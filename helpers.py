import requests
import json

from flask import redirect, render_template, session
from functools import wraps


def get_car_data(vin, year):
    "Decode VIN"
    url = f"https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{vin}?format=json&modelyear={year}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for HTTP error responses
        manufacturer_data = response.json()
        # print("Returning data:", manufacturer_data)
        return {
            "amount": manufacturer_data["Count"],
            "message": manufacturer_data["Message"],
            "vin": manufacturer_data["SearchCriteria"],
            "results": manufacturer_data["Results"],
        }

    except requests.RequestException as e:
        print(f"Request error: {e}")
    except (KeyError, ValueError) as e:
        print(f"Data parsing error: {e}")
    return None

# car = "JF1VA2W64M9806022"
# year = 2021
# locations = get_car_data(car, year)
# print(locations)

# for index in locations["results"]:
    # print(f"{index["Variable"]} : {index["Value"]}")


# https://vpic.nhtsa.dot.gov/api/vehicles/decodevin/{vin}?format=json&modelyear={year}

# https://vpic.nhtsa.dot.gov/api/vehicles/GetMakeForManufacturer/{make}?format=json


# [4]
def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function


# [6]
def error(message, code=400):

    def escape(s):
        for old, new in [
            ("-", "--"),
            (" ", "-"),
            ("_", "__"),
            ("?", "~q"),
            ("%", "~p"),
            ("#", "~h"),
            ("/", "~s"),
            ('"', "''"),
        ]:
            s = s.replace(old, new)
        return s

    return render_template("error.html", top=code, bottom=escape(message)), code

