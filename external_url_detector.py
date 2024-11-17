# This script monitors external data sharing when querying Wikipedia's API.
# It uses Python's `requests` library to send a query to Wikipedia's API and checks if
# any URLs in the response are external (i.e., not belonging to Wikipedia).
# The script scans the response for URLs using a regular expression (via `re` library)
# and flags any external URLs.
# The script requires the `requests` library to be installed. If not installed, use the
# following command:
# pip install requests

# This script draws inspiration from the methods outlined in the paper "Sensitive Information Tracking in Commodity IoT" by Z. Berkay Celik et al.
# The paper focuses on the importance of monitoring and tracking the flow of sensitive information within IoT ecosystems to detect potential data leaks
# or unauthorized external transmissions. Specifically, the methodology in the paper revolves around identifying "data sinks"—external entities or networks
# that may unintentionally or maliciously receive sensitive data.
#
# In this script, a similar concept is applied by monitoring Wikipedia's API responses. The goal is to check for any external URLs
# in the API response that could indicate data being shared with third-party domains outside of Wikipedia. By identifying such URLs,
# the script ensures that potentially sensitive information is not leaking to external sites. This is analogous to tracking how IoT devices
# might transmit sensitive data to external networks or services. The method helps detect unintentional or harmful data sharing, maintaining
# data privacy and security during interaction with the Wikipedia API.

import requests  # For making HTTP requests to Wikipedia's API
import re        # For using regular expressions to detect URLs in the response
import io        # For capturing printed output
import sys       # For redirecting standard output      # For using regular expressions to detect URLs in the response

def detect_external_urls(response):
    """
    This function checks the response text for URLs and separates the external ones from internal ones.
    
    Arguments:
    - response: The HTTP response object from Wikipedia's API.
    
    This function will collect all URLs and then display them at the end along with a list of external URLs.
    """
    # Find all URLs in the response text using regular expression
    urls = re.findall(r'https?://[^\s]+', response.text)
    
    # List to store external URLs
    external_urls = []

    # Print all URLs first
    print("All URLs found in the response:")
    for url in urls:
        print(url)
    
    # Iterate through each detected URL and check if it's an external link
    for url in urls:
        if "wikipedia.org" not in url:
            # If the URL is not part of Wikipedia's domain, add it to the list
            external_urls.append(url)

    # Output all external URLs detected at the end
    if external_urls:
        print("____________________________________________________________________________________")
        print("External URLs detected:")
        for url in external_urls:
            print(url)
    else:
        print("No external URLs detected.")

def query_wikipedia_article(title):
    """
    This function sends a request to Wikipedia's API to fetch the content of a given article.
    
    Arguments:
    - title: The title of the Wikipedia article to fetch.
    """
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles={title}"
    response = requests.get(url)
    
    if response.status_code == 200:
        detect_external_urls(response)
    else:
        print(f"Error fetching article. Status code: {response.status_code}")

# Query a Wikipedia article (e.g., "Python (programming language)")
query_wikipedia_article("Python_(programming_language)")
