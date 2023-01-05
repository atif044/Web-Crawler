import urllib.parse
import requests
#import threading
from bs4 import BeautifulSoup
from general import create_project_directory
import os


def search(query):
    next = False
    results = ""
    try:
        for engine in ["google", "bing", "duckduckgo"]:
            if engine == "google":
                url = f"https://www.google.com/search?q={query}"
            elif engine == "bing":
                url = f"https://www.bing.com/search?q={query}"
            elif engine == "duckduckgo":
                url = f"https://duckduckgo.com/?q={query}"
            else:
                continue
            response = requests.get(url)
            results += response.text
            next=True
    except:
        print("Could not execute query...")
        next=False
    return results ,next

def extract_links(html):
    try:
        soup = BeautifulSoup(html, "html.parser")
        extracted_links = set()
        for link in soup.find_all("a"):
            href = link.get("href")
            if href and href.startswith("/url?q="):
                extracted_links.add(href[7:])
    except:
        print("Could not extract links")
    return link_seperator(extracted_links)

lnks = set()
def link_seperator(links):
    for link in links:
        parsed_link = urllib.parse.urlparse(link)
        domain = parsed_link.netloc
        lnks.add(domain)
        #print(domain)
    return lnks

def save_to_file(PROJECT_NAME, links):
    PROJECT=PROJECT_NAME + '/search.txt'
    with open(PROJECT, 'w') as f:
        for link in links:
            f.write(link + '\n')
    print("Links successfully saved to file: " + PROJECT )
            
def display_links(links):
    print("Query Links: \n")
    for link in links:
        print(link)
          
def execute(query):
    #query = input("Enter your query: ")
    PROJECT_NAME = ('S_'+query).upper()
    html,next = search(query)
    if  next:
        links = extract_links(html)
        if not os.path.exists(PROJECT_NAME):
            create_project_directory(PROJECT_NAME)
        display_links(links)
        save_to_file(PROJECT_NAME, links)
    else:
        print("Program terminated...")
    
