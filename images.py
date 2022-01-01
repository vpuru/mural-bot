from serpapi import GoogleSearch
import requests
from bs4 import BeautifulSoup
import os
import pathlib
from dotenv import getKey

getKey()

def getBackgroundLinks(query):
    params = {
    "api_key": os.environ["key"],
    "engine": "google",
    "ijn": "2",
    "q": f'{query}',
    "google_domain": "google.com",
    "tbm": "isch",
    "safe": "active",
    }

    search = GoogleSearch(params)
    results = search.get_dict()
    return results['images_results']

def downloadBackgroundImages(data):
    # make our directory if needed
    with pathlib.Path("./asset") as mypath:
        if not mypath.is_file():
            os.mkdir("assets")
    
    # count
    count = 0
    
    # Download all images
    for item in data:

        # check if we have the images requred
        if count == 64:
            break

        # name our current file
        currFileName = f'assets/asset-{count}.jpg'
        currFileLink = item["original"]

        # get request & download
        with open(currFileName, 'wb') as f:
            # file data
            fileData = requests.get(currFileLink, timeout=3)

            # check for timeout or other error
            if fileData.status_code != 200:
                continue
            
            # write our file
            f.write(fileData.content)
            count += 1

        # Print (debug)
        # print(count, ": ", item["original"])


def scrapeForegroundImage(name):
    # make our directory if needed
    with pathlib.Path("./pfp") as mypath:
        if not mypath.is_file():
            os.mkdir("pfp")

    # clean up our name
    name = name.replace(" ", "-")
    name = name.lower()

    # create our url link using name
    url = f'https://www.famousbirthdays.com/people/{name}.html'

    # send request
    r = requests.get(url)

    # request comes up as != 200
    print(r.status_code)

    # scrape data
    soup = BeautifulSoup(r.text, 'html.parser')
    images = soup.find_all('img')

    # download the first file
    fileData = requests.get(images[0]['src'])

    # write file
    with open("pfp/asset.jpg", 'wb') as f:
        f.write(fileData.content)
    
    print("ok")

def query(name):
    # download background images
    mydata = getBackgroundLinks(name)
    downloadBackgroundImages(mydata)

    # download foreground images
    scrapeForegroundImage(name)