import wikipediaapi
import wikipedia
import json
import requests
import numpy as np
wiki_wiki = wikipediaapi.Wikipedia('MyProjectName (merlin@example.com)', 'en')

page_py = wiki_wiki.page('a')
#print("Page - Exists: %s" % page_py.exists())

def feed_data(type):
    PARAMS = {}
    if (type == "geo"):
        PARAMS = {
            "format": "json",
            "list": "geosearch",
            "gscoord": "29.886829786|-97.93666292",
            "gslimit": "10",
            "gsradius": "10000",
            "action": "query"
        }

    elif (type == "date"):
        DATE = wikipedia.datetime.today()
        return DATE

    elif (type == "user"):
        PARAMS = {
            "action": "query",
            "meta": "userinfo",
            "uiprop": "rights",
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


    if input == "geosearch":
        URL = "https://en.wikipedia.org/w/api.php"
        PARAMS = feed_data("geo")
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()

        PLACES = DATA['query']['geosearch']
        return PLACES
    elif input == "date":
        DATE = feed_data("date")
        return DATE

    elif input == "user":
        PARAMS = feed_data("user")
        R = S.get(url=URL, params=PARAMS)
        DATA = R.json()
        return DATA


def main():
    search = input("What type of date are you looking for?\n user, geosearch, date\nInput: ")
    print(saint_algorithm(search))

if __name__=="__main__":
    main()

#suggested = wikipedia.geosearch(29.886829786, -97.93666292,None, 10, 10000)
#wikipedia.datetime.today()
#x = suggested.json()
#print(suggested)

'''
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

#print(DATA)
#assert DATA['login']['result'] == 'Success'

#S = requests.Session()

#URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "meta": "userinfo",
    "uiprop": "rights",
    "format": "json"
}

R = S.get(url=URL, params=PARAMS)
USER = R.json()

print(USER)
'''


# THINGS WE CAN GET FROM WIKIPEDIA API:
# 1. "datetime" - Current data and time (potentially sensitive data)
# 2. "geosearch" - Gives articles around the given point/location (sensitive data leak)
# 3.