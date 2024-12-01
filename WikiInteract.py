import wikipediaapi
import wikipedia
import json
import requests
import numpy as np


# THINGS WE CAN GET FROM WIKIPEDIA API:
# 1. "datetime" - Current data and time (potentially sensitive data)
# 2. "geosearch" - Gives articles around the given point/location (sensitive data leak)
# 3. "user" - Return account info for the currently logged-in user in JSON (sensitive data leak)
# 4. "search" - Returns the information of a page with the provided title (potential sensitive data)
# 5. "random" - Returns the information of random pages (potential data leak)
# 6. "links" - Return all links on the page with the given title (potential data leak)
# 7. "summary" - Returns a summary of the page with the given title (potential data leak)
# 8. "categories" - Returns a list of categories for the given page (low potential data leak)
# 9. "languages" - Returns a list of all currently supported languages (low potential data leak)
# 10. "contributors" - Returns a list of all logged contributors and count of anonymous contributors (potential data leak0

def feed_data(type):
    PARAMS = {}
    # Tainted data for "geosearch"
    if (type == "geo"):
        PARAMS = {
            "format": "json",
            "list": "geosearch",
            "gscoord": "29.886829786|-97.93666292",
            "gslimit": "10",
            "gsradius": "10000",
            "action": "query"
        }

    # Tainted data for "datetime"
    elif (type == "date"):
        DATE = wikipedia.datetime.today()
        return DATE

    # Tainted data for "userquery"
    elif (type == "user"):
        PARAMS = {
            "action": "query",
            "meta": "userinfo",
            "uiprop": "rights",
            "format": "json"
        }

    # Tainted data for "pagequery"
    elif (type == "page"):
        SEARCHPAGE = "Texas State University"
        PARAMS = {
            "action": "query",
            "format": "json",
            "list": "search",
            "srsearch": SEARCHPAGE
        }

    # Tainted data for "random"
    elif (type == "random"):
        PARAMS = {
            "action": "query",
            "format": "json",
            "list": "random",
            "rnlimit": "5"
        }

    # Tainted data for "links"
    elif (type == "links"):
        PARAMS = {
            "action": "query",
            "format": "json",
            "titles": "Texas State University",
            "prop": "links"
        }

    # Tainted data for "summary"
    elif (type == "summ"):
        SUMM = wikipedia.summary('Texas State University')
        return SUMM

    # Tainted data for "categories"
    elif (type == "categories"):
        PARAMS = {
            "action": "query",
            "format": "json",
            "prop": "categories",
            "titles": "Texas State University"
        }

    # Tainted data for "languages"
    elif (type == "langs"):
        LANGS = wikipedia.languages()
        return LANGS

    # Tainted data for "contributors"
    elif (type == "contr"):
        PARAMS = {
            "action": "query",
            "titles": "Texas State University",
            "prop": "contributors",
            "format": "json"
        }
    return PARAMS


def saint_algorithm(input):
    wiki = wikipedia

    USERNAME = "Rpandal30"
    PASSWORD = "Rod118217!@"

    S = requests.Session()

    URL = "https://www.mediawiki.org/w/api.php"

    # Retrieve login token first
    PARAMS_0 = {
        'action':"query",
        'meta':"tokens",
        'type':"login",
        'format':"json"
    }

    R = S.get(url=URL, params=PARAMS_0)
    DATA = R.json()

    LOGIN_TOKEN = DATA['query']['tokens']['logintoken']

    PARAMS_1 = {
        'action': "login",
        'lgname': USERNAME,
        'lgpassword': PASSWORD,
        'lgtoken': LOGIN_TOKEN,
        'format': "json"
    }

    R = S.post(URL, data=PARAMS_1)
    DATA = R.json()

    # Get pages of things around a certain location
    if input == "geosearch":
        URL = "https://en.wikipedia.org/w/api.php"
        PARAMS = feed_data("geo")
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()

        PLACES = DATA['query']['geosearch']
        return PLACES

    # Get current Date & Time
    elif input == "date":
        DATE = feed_data("date")
        return DATE

    # Get a user's info
    elif input == "user":
        PARAMS = feed_data("user")
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        return DATA

    # Get information of specific page
    elif input == "page":
        URL = "https://en.wikipedia.org/w/api.php"
        PARAMS = feed_data("page")
        R = S.get(url=URL, params=PARAMS)
        RAWDATA = R.json()
        DATA = RAWDATA['query']['search']
        return DATA

    # Get information of random pages
    elif input == "random":
        URL = "https://en.wikipedia.org/w/api.php"
        PARAMS = feed_data("random")
        R = S.get(url=URL, params=PARAMS)
        RAWDATA = R.json()
        DATA = RAWDATA["query"]["random"]
        return DATA

    # Get all links pertaining to that page
    elif input == "links":
        URL = "https://en.wikipedia.org/w/api.php"
        PARAMS = feed_data("links")
        R = S.get(url=URL, params=PARAMS)
        RAWDATA = R.json()

        DATA = RAWDATA['query']['pages']
        return DATA

    # Get the summary of the provided page
    elif input == "summary":
        SUMM = feed_data("summ")
        return SUMM

    # Get list of categories for provided page
    elif input == "categories":
        URL = "https://en.wikipedia.org/w/api.php"
        PARAMS = feed_data("categories")
        R = S.get(url=URL, params=PARAMS)
        RAWDATA = R.json()
        DATA = RAWDATA["query"]["pages"]
        return DATA

    # Get list of languages available
    elif input == "lang":
        LANGS = feed_data("langs")
        return LANGS
    # Get list of contributors for that page
    elif input == "contributors":
        URL = "https://en.wikipedia.org/w/api.php"
        PARAMS = feed_data("contr")
        R = S.get(url=URL, params=PARAMS)
        RAWDATA = R.json()
        DATA = RAWDATA['query']['pages']
        return DATA



# MAIN FUNCTION - DO NOT DELETE!
#'''
def main():
    search = input("What type of date are you looking for?\nOptions: user, geosearch, date, page, random, links, summary, categories, lang, contributors\nInput: ")
    print(saint_algorithm(search))

if __name__=="__main__":
    main()
#'''