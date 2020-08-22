from selenium.webdriver import Firefox
import time
import random

boys = [0, 5, 7, 8, 9]
girls = [1, 2, 3, 4, 6, 10]
browser = Firefox()

browser.get('https://doodle.com/poll/ni4aibp7nhp4kifv')
# accept cookies
consent = browser.find_element_by_class_name("fc-cta-consent")
consent.click()
browser.get('https://doodle.com/poll/ni4aibp7nhp4kifv')

with open("names", "r") as names:
    for name_in in names:
        browser.get('https://doodle.com/poll/ni4aibp7nhp4kifv')
        time.sleep(1)

        others = browser.find_element_by_id("d-nextChevron")
        others.click()

        choice1 = random.choices(girls, weights=[7, 2, 2, 1, 2, 2])[0]
        option1 = browser.find_element_by_xpath(f"//div[@data-optionindex='{choice1}']")
        option1.click()

        choice2 = random.choices(boys, weights=[1, 2, 2, 2, 7])[0]
        option2 = browser.find_element_by_xpath(f"//div[@data-optionindex='{choice2}']")
        option2.click()

        name = browser.find_element_by_xpath("//input[@id='d-newParticipantInput']")
        send_name = str(name_in.strip())
        name.send_keys(send_name)

        send = browser.find_element_by_class_name("d-participateButton")
        send.click()
