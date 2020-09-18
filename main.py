import time
from webbot import Browser
# from bs4 import BeautifulSoup
import requests
from requests_html import HTMLSession

url = 'https://iss-sim.spacex.com/'
session = HTMLSession()
response = session.get(url)

# r = requests.get(website)
# parsed_html = BeautifulSoup(website, "html.parser")

def getXCoords():
    targetX =  float(response.html.find('.error')[0].text)
    return targetX

def main():

    web = Browser()
    web.go_to(url)
    
    while True:
        time.sleep(8)
        web.click('BEGIN')
        
        currentX = getXCoords()
        
        # Move to the left and right until (selector = #yw .error) == 0.0
        while currentX > 0.0 or currentX < 0.0:
            if currentX < 0.0:
                web.press(web.Key.RIGHT)
                time.sleep(1.5)
                currentX = getXCoords()
                print(currentX) # Print value of current X value

            if currentX > 0.0:
                web.press(web.Key.LEFT)
                time.sleep(1.5)
                currentX = getXCoords()
                print(currentX) # Print value of current X value
    
    # print(value)

if __name__ == "__main__":
    main()

