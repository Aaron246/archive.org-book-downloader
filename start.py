import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import cv2
import os
from PIL import Image

link = 'https://archive.org/details/crownofbeautybah0000brau'
number = 108

options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(link)
driver.set_window_size(1920, 1080)
time.sleep(10)

fs = driver.find_element(By.XPATH, "//a[text()='Log in']")
fs.click()

fs = driver.find_element(By.XPATH, '//input[@class="form-element input-email"]')
fs.send_keys("omids1919@gmail.com")

fs = driver.find_element(By.XPATH, '//input[@class="form-element input-password"]')
fs.send_keys("world123")

fs = driver.find_element(By.XPATH, '//input[@class="btn btn-primary btn-submit input-submit js-submit-login"]')
fs.click()

time.sleep(10)

driver.get(link)
time.sleep(10)
fs = driver.find_element(By.XPATH, '//div[@class="icon icon-fullscreen"]')
fs.click()

folder = driver.find_element(By.XPATH, '//div[@class="icon icon-left-arrow hflip"]')

for i in range(1, number+2, 2):
    driver.save_screenshot(str(i) + '-' + str(i + 1) + '.png')
    png_img = cv2.imread(str(i) + "-" + str(i + 1) + ".png")
    cv2.imwrite(str(i) + "-" + str(i + 1) + ".jpg", png_img, [int(cv2.IMWRITE_JPEG_QUALITY), 70])
    os.remove(str(i) + "-" + str(i + 1) + ".png")

    im = Image.open(str(i) + "-" + str(i + 1) + ".jpg")

    # Setting the points for cropped image
    left = 200
    top = 62
    right = 1720
    bottom = 1036

    # Cropped image of above dimension
    # (It will not change original image)
    im1 = im.crop((left, top, right, bottom))

    # Shows the image in image viewer
    im1.save(str(i) + "-" + str(i + 1) + ".jpg")

    folder.click()
    time.sleep(10)
