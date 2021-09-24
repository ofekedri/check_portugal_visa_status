import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
#import chromedriver_binary
from env import * 


options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)
#driver = webdriver.Chrome('/root/docker/chromedriver')

driver.get('https://nacionalidade.justica.gov.pt/')

element = driver.find_element_by_id('SenhaAcesso')
element.send_keys(passport_request_id)
element.send_keys(Keys.ENTER)
dir_path = os.path.dirname(os.path.realpath(__file__))

#if os.path.exists(dir_path+"\portugal_passport.png"):
#  os.remove(dir_path+"\portugal_passport.png")
#else:
#  print('File does not exists')

time.sleep( 2 )
driver.save_screenshot("portugal_passport.png")

driver.close()

import send_notification
