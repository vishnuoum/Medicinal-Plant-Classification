import requests
from bs4 import BeautifulSoup
from logConfig import logging


def nearBy(location):

    logging.info("Calling nearby function")

    URL = "https://www.google.com/search?q=ayurveda+hospitals+near+" + location
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')

    logging.info("Parsing HTML Page")


    f = open("data.html", "a")
    f.write(r.text)
    f.close()

    logging.info("Finding useful tags")

    divs = soup.find_all("div",{"class" : "X7NTVe"})
    print(len(divs))
    results = []
    for div in divs:
        details = {}
        details["hospital"] = div.find("div",{"class":"BNeawe deIvCb AP7Wnd"}).text
        details["location"] = div.find("div",{"class":"BNeawe tAd8D AP7Wnd"}).text.replace("Open 24 hours","")
        details["rating"] = div.find("span",{"class":"r0bn4c rQMQod tP9Zud"}).text.strip().split()
        details["url"] = "https://www.google.com" + div.find("a")["href"]
        results.append(details)
        # print(div.find("div",{"class":"BNeawe deIvCb AP7Wnd"}).text)
    print(results)

    logging.info("Returning scraped results")

    return results

