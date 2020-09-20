from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chrome_driver import PATH
import time

URL = 'https://iss-sim.spacex.com/'
driver = webdriver.Chrome(PATH)

"""
    ---------------------------------------
    :: HORIZONTAL TRANSLATION FUNCTIONS ::
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

    if currentX < 1.5:
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

    elif currentX > 5.0:
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
    :: FORWARD/BACKWARD TRANSLATION FUNCTIONS ::
    ---------------------------------------------
"""

def forwardControl():
    forward_btn = driver.find_element_by_id('translate-forward-button')
    backward_btn = driver.find_element_by_id('translate-backward-button')
    trans_up = driver.find_element_by_id('translate-up-button')
    trans_down = driver.find_element_by_id('translate-down-button')

    x_range = driver.find_element_by_css_selector("#x-range .distance").text
    x_range = float(x_range[:-2])
    y_range = driver.find_element_by_css_selector("#z-range .distance").text
    y_range = float(y_range[:-2])
    z_range = driver.find_element_by_css_selector("#z-range .distance").text
    z_range = float(z_range[:-2])

    for i in range(3):
        forward_btn.click()

    if x_range <= 60.0:
        for i in range(5):
            trans_down.click()

    elif x_range < 175.0:
        if z_range > 10.0:
            for i in range(5):
                trans_down.click()
        else:
            for i in range(15):
                trans_up.click()

            
    print("distance from dock is:", x_range)

def main():
    driver.get(URL)
    time.sleep(9)
    driver.find_element_by_id('begin-button').click()
    time.sleep(8)

    while True:
        forwardControl()
        horizontalControl()
        # Keep window open
        pass

if __name__ == "__main__":
    main()
