import requests
from datetime import datetime


def feed_data(data_type):
    """
    Prepare API parameters based on the requested data type.
    """
    if data_type == "geo":
        return {
            "format": "json",
            "list": "geosearch",
            "gscoord": "29.886829786|-97.93666292",
            "gslimit": "10",
            "gsradius": "10000",
            "action": "query"
        }
    elif data_type == "date":
        return datetime.today()
    elif data_type == "user":
        return {
            "action": "query",
            "meta": "userinfo",
            "uiprop": "rights",
            "format": "json"
        }
    else:
        raise ValueError("Invalid data type")


def saint_algorithm(input_data, session=None):
    """
    Handles API queries based on the input type.
    """
    session = session or requests.Session()
    if input_data == "geosearch":
        params = feed_data("geo")
        response = session.get("https://en.wikipedia.org/w/api.php", params=params)
        return response.json()
    elif input_data == "date":
        return feed_data("date")
    elif input_data == "user":
        params = feed_data("user")
        response = session.get("https://en.wikipedia.org/w/api.php", params=params)
        return response.json()
    else:
        raise ValueError("Invalid input")

