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
import sys       # For redirecting standard output

def detect_external_urls(response, output_list):
    """
    This function checks the response text for URLs that do not belong to Wikipedia.
    
    Arguments:
    - response: The HTTP response object from Wikipedia's API.
    - output_list: A list to store external URLs.
    
    This function will append any external URLs found in the response text to the list.
    """
    # Find all URLs in the response text using regular expression
    urls = re.findall(r'https?://[^\s]+', response.text)
    
    # Iterate through each detected URL and check if it's an external link
    for url in urls:
        if "wikipedia.org" not in url:
            # If the URL is not part of Wikipedia's domain, append it to the list
            output_list.append(url)

def query_wikipedia_article(title):
    """
    This function sends a request to Wikipedia's API to fetch the content of a given article.
    
    Arguments:
    - title: The title of the Wikipedia article to fetch.
    """
    url = f"https://en.wikipedia.org/w/api.php?action=query&prop=revisions&rvprop=content&format=json&titles={title}"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Create a list to store external URLs
        external_urls = []
        detect_external_urls(response, external_urls)
        
        # If external URLs are found, return the list
        if external_urls:
            print("External URLs detected:")
            for url in external_urls:
                print(url)
        else:
            print("No external URLs detected.")
    else:
        print(f"Error fetching article. Status code: {response.status_code}")

# Redirecting the print statements to capture them
original_stdout = sys.stdout  # Save the original stdout
sys.stdout = io.StringIO()    # Create a StringIO object to capture output

# Query a Wikipedia article (e.g., "Python (programming language)")
query_wikipedia_article("Python_(programming_language)")

# Capture the output and store it in a variable
captured_output = sys.stdout.getvalue()

# Reset stdout back to its original state
sys.stdout = original_stdout

# You can now inspect or process captured_output to find any external URLs
print("Captured Output:")
print(captured_output)
