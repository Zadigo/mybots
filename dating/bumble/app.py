import os
import time
from collections import deque
from threading import Thread

import numpy
import requests
from bs4 import BeautifulSoup
from matplotlib import image, pyplot
from PIL import Image
from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class ImageMixin:
    image_patn = None
    # path = 'C:\\Users\\Pende\\Documents\\myapps\\bots\\other\\test.jpg'

    def fit_transform_image(self):
        # Save the image to a temp
        # folder in ordr to work on it

        # Get the path of the image
        # and open it with PIL
        path = self.path
        img = Image.open(self.image_path).resize((200, 200))

        # Loads the height, width, channel
        # of the image into an array
        image_statistics = numpy.asarray(img.convert('L'))
        # Save the new image
        Image.fromarray(image_statistics).save('some_image.jpg')

    def get_image_data(self, url):
        def send_request():
            response = requests.get(url, user_agent=None)
            if response.status_code == 200:
                with open('', mode='rb') as f:
                    for data in response.iter_content(1024):
                        if data:
                            f.write(data)
                        else:
                            break
                self.image_path = 'path' or None

        request_thread = Thread(target=send_request)
        request_thread.start()
        
        return request_thread.is_alive()

class Bumble(ImageMixin):
    matched_users = deque()
    users = deque()

    def __init__(self):
        self.driver = Edge(executable_path=os.environ.get('EDGE_DRIVER'))
        self.driver.get('https://bumble.com')

    def login(self, username, password):
        time.sleep(5)
        
        try:
            login_button = self.driver.find_element_by_xpath('//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a')
        except:
            print('Could not connect.')
            return False
        else:
            login_button.click()

        time.sleep(10)

        # Facebook login
        facebook = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[1]/div/div[2]/div')
        facebook.click()

        time.sleep(5)

        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        username_field = self.driver.find_element_by_xpath('//*[@id="email"]')
        password_field = self.driver.find_element_by_xpath('//*[@id="pass"]')

        username_field.send_keys(username)
        password_field.send_keys(password)

        login_button = self.driver.find_element_by_xpath('//*[@id="u_0_0"]')
        login_button.click()

        self.driver.switch_to.window(base_window)

        time.sleep(5)

        return True

    def like(self):
        self.user_profile()
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_RIGHT)
        time.sleep(3)
        return True
            
    def dislike(self):
        self.driver.find_element_by_tag_name('body').send_keys(Keys.ARROW_LEFT)
        time.sleep(3)
        return True

    def auto_swipe(self, n=10):
        for _ in range(1, n):
            self.like()
        return self.matched_users

    def user_profile(self):
        name_and_age = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[1]/article/div[1]/div[1]/article/div[2]/section/header/h1')
        image = self.driver.find_element_by_xpath('//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[1]/article/div[1]/div[1]/article/div[1]/figure/picture/img')
        user = name_and_age.text, image.get_attribute('src')
        if user:
            self.users.append(user)
            time.sleep(1)
            return True
        time.sleep(1)
        return False

# bumble = Bumble()
# bumble.login('pendenquejohn@live.fr', 'Constance97170-Jac')
# bumble.auto_swipe()
