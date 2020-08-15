import os
import time

from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys



class Tinder:
    matched_users = []

    def __init__(self):
        self.driver = Edge(executable_path=os.environ.get('EDGE_DRIVER'))
        self.driver.get('https://tinder.com')

    def login(self, username, password):
        WebDriverWait(self.driver, 6000).until(expected_conditions \
                .element_to_be_clickable((By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')))
        
        try:
            facebook = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button')
        except:
            print('Could not connect.')
            return False
        else:
            facebook.click()

        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        username_field = self.driver.find_element_by_xpath('//*[@id="email"]')
        password_field = self.driver.find_element_by_xpath('//*[@id="pass"]')

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_button.click()

        self.driver.switch_to.window(base_window)

        time.sleep(10)

        localization_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
        localization_button.click()

        time.sleep(10)

        try:
            accept_to_receive_messages = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
        except:
            print('Could not find message button or message modal did not pop up.')
            return False
        else:
            accept_to_receive_messages.click()

    def like(self):
        # like_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        # self.button_click(like_button)

        # Test for the 
        # random pop screen
        # popup = self.close_random_popup()
        # if popup:
        #     popup.click()

        # time.sleep(1)

        self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)

        time.sleep(3)

        try:
            # If we have a match, we have to
            # manage the card in question by
            # clicking on the link
            match_card_link = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        except:
            # There is no match, then continue
            # swiping until we find one
            return False
        else:
            match_card_link.click()
            self.matched_users.append(1)
            return True
            
    def dislike(self):
        dislike_button = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[2]/button')
        self.button_click(dislike_button)

    def auto_swipe(self, n=10):
        for _ in range(1, n):
            self.like()
            time.sleep(3)
        return self.matched_users

    @staticmethod
    def button_click(button):
        try:
            button.click()
        except:
            return False
        else:
            return True

    def close_random_popup(self):
        WebDriverWait(self.driver, 2000).until(
            expected_conditions.visibility_of((By.XPATH, '//*[@id="modal-manager"]'))
        )
        try:
            # Deals with the pop up that asks us
            # to add tinder to the homescreen
            home_screen_button = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        except:
            return False
        else:
            return home_screen_button


tinder = Tinder()
tinder.login('pendenquejohn@live.fr', 'Constance97170-Jac')
tinder.auto_swipe()
