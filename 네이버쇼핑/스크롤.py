import time
import random

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def 스크롤(driver, ran_S, ran_E, target_text, duration):
    # Get the page height
    page_height = driver.execute_script("return document.body.scrollHeight")

    # Set the initial scroll position and randomize the scroll distance
    scroll_position = 0
    scroll_distance = random.randint(ran_S, ran_E)

    # start time
    start_time = time.time()

    # Start scrolling down
    while True:

        #when target text visible, break
        if target_text != '':
            print('here')
            try:
                print(target_text,0)
                footer = driver.find_element(By.PARTIAL_LINK_TEXT, target_text)
                print(target_text,1)
                time.sleep(0.5)
                driver.execute_script("arguments[0].scrollIntoView();", footer)
                print('keyword out')
                break
            except NoSuchElementException:
                try:
                    footer = driver.find_element(By.LINK_TEXT, target_text)
                    driver.execute_script("arguments[0].scrollIntoView();", footer)
                    print('keyword out')
                    break
                except NoSuchElementException:
                    footer = None

        #out when setted duration
        elif duration != 0:
            end_time = time.time()
            elapsed_time = end_time - start_time
            if elapsed_time >= duration:
                print('duration out')
                break

        # Check if we have reached the end of the page
        elif scroll_position >= page_height:
            print('bottom out')
            break


        # Scroll down by the random distance using JavaScript
        driver.execute_script(f"window.scrollBy(0, {scroll_distance});")
        scroll_position += scroll_distance

        # Randomly decide whether to stop scrolling or not
        if random.random() < 0.2:  # 20% chance to stop scrolling
            # Wait a random amount of time (between 500 and 3000 milliseconds) before scrolling again
            wait_time = random.randint(500, 3000)
            time.sleep(wait_time / 1000)  # convert wait time to seconds
        else:
            # Randomize the next scroll distance
            scroll_distance = random.randint(ran_S, ran_E)


def 스크롤_탑(driver):
    # Define the amount of scroll distance
    scroll_distance = random.randint(60, 110)

    # Scroll up the page
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.CONTROL + Keys.HOME)
    for i in range(int(scroll_distance/100)):
        driver.execute_script("window.scrollBy(0, -100);")
        time.sleep(random.randint(500, 2000)/1000)
    time.sleep(random.randint(500, 2000)/1000)



def simple_스크롤(driver,EA):
    for i in range(EA):
        stopper = random.randint(0,2)
        if stopper == 0:
            scroll_height = random.randint(40,500)
            driver.execute_script(f"window.scrollBy(0,{scroll_height});")
        time.sleep(random.randint(1500,5000)/1000)
