import requests
from bs4 import BeautifulSoup

def crawl_web_for_terms(url, terms):
    try:
        # Send a GET request to the URL
        response = requests.get(url)
        response.raise_for_status()  # Check for errors in the request

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find elements containing the specified terms
        found_elements = soup.find_all(string=lambda text: any(term in text.lower() for term in terms))

        # Extract relevant information or store found elements
        # Example: printing found text
        for element in found_elements:
            print(element)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the web page: {e}")

# Set the URL and terms you want to search for
url_to_crawl = "https://example.com"
search_terms = ["python", "web scraping", "data science"]

# Call the function to crawl the web for specified terms
crawl_web_for_terms(url_to_crawl, search_terms)
