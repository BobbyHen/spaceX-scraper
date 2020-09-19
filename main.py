from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chrome_driver import PATH
import time

URL = 'https://iss-sim.spacex.com/'
driver = webdriver.Chrome(PATH)

"""
    ---------------------------------------
    :: HORIZONTAL TRANSLATIONS FUNCTIONS ::
    ---------------------------------------
"""
def getX():
    currentX = driver.find_element_by_css_selector("#yaw .error").text
    value = float(currentX[:-1])
    print(value)
    return value

def checkRateX():
    currentXRate = driver.find_element_by_css_selector("#yaw .rate").text
    value = float(currentXRate[:-3])
    return value

def horizontalControl():
    currentX = getX()
    rateX = checkRateX()

    left_btn = driver.find_element_by_id('yaw-left-button')
    right_btn = driver.find_element_by_id('yaw-right-button')

    if currentX < 0.0:
        # Go to the LEFT
        left_btn.click()
        time.sleep(1)
        # Call getX()
        currentX = getX()
        rateX = checkRateX()
        if rateX <= -0.4:
            # Equalize X
            for i in range(3):
                right_btn.click()

    elif currentX > 0.0:
        # Go to the RIGHT
        right_btn.click()
        time.sleep(1)
        # Call getX()
        currentX = getX()
        rateX = checkRateX()
        if rateX >= 0.4:
            # Equalize X
            for i in range(3):
                left_btn.click()
"""
    ---------------------------------------------
    :: FORWARD/BACKWARD TRANSLATIONS FUNCTIONS ::
    ---------------------------------------------
"""

def main():
    driver.get(URL)
    time.sleep(9)
    driver.find_element_by_id('begin-button').click()
    time.sleep(8)

    while True:
        horizontalControl()
        
        # Keep window open
        pass
        

if __name__ == "__main__":
    main()
