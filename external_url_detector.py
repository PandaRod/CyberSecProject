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

import requests  # For making HTTP requests
import re        # For using regular expressions to detect URLs
from urllib.parse import urlparse  # To extract the domain name
from bs4 import BeautifulSoup  # To parse HTML content
import time  # To measure page load time

def fetch_external_url_info(url):
    """
    This function fetches additional information about an external URL:
    - HTTP status code
    - Content type
    - Title of the page
    - Meta description
    - Page load time
    """
    try:
        # Start the timer to measure page load time
        start_time = time.time()
        
        # Send a GET request to fetch the external URL's content
        response = requests.get(url, timeout=5)
        
        # Calculate the page load time
        load_time = round(time.time() - start_time, 2)
        
        # Extract the status code
        status_code = response.status_code
        
        # Extract the content type
        content_type = response.headers.get('Content-Type', 'N/A')
        
        # Parse HTML to extract the title and meta description
        title = "N/A"
        description = "N/A"
        if 'html' in content_type:
            soup = BeautifulSoup(response.text, 'html.parser')
            title_tag = soup.find('title')
            if title_tag:
                title = title_tag.text
            description_tag = soup.find('meta', attrs={'name': 'description'})
            if description_tag:
                description = description_tag.get('content', 'N/A')
        
        # Return a dictionary of the gathered information
        return {
            'status_code': status_code,
            'content_type': content_type,
            'title': title,
            'description': description,
            'load_time': load_time
        }
    
    except requests.exceptions.RequestException as e:
        # If an error occurs (e.g., network issue), return a failed status
        return {'status_code': 'Error', 'content_type': 'N/A', 'title': 'N/A', 'description': 'N/A', 'load_time': 'N/A'}

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

    # Output all external URLs detected at the end with more detailed formatting
    if external_urls:
        print("____________________________________________________________________________________")
        print("External URLs detected:\n")
        for url in external_urls:
            # Extract the domain name from the URL
            domain = urlparse(url).netloc

            # Fetch additional information about the external URL
            external_info = fetch_external_url_info(url)
            
            # Format the output with Name, Link, and Domain Info
            print(f"Name: {domain} | Link: {url} | Protocol: {url.split(':')[0].upper()} | Status Code: {external_info['status_code']} | "
                  f"Content Type: {external_info['content_type']} | Load Time: {external_info['load_time']}s")

            # Add the title and description if available
            if external_info['title'] != 'N/A':
                print(f"  Title: {external_info['title']}")
            if external_info['description'] != 'N/A':
                print(f"  Description: {external_info['description']}")
            
            # Add a separator line for clarity
            print("____________________________________________________________________________________")
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
