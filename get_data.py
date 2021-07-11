from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
from io import BytesIO
import base64
import time
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(ChromeDriverManager().install())
# PATH = 'https://www.xuathoadon.com.vn/'
# for i in range(0,100):
#     driver.get(PATH)
#     time.sleep(1)
#     element = driver.find_element_by_xpath("//img[@id='captcha']")
#     loc = element.location
#     size = element.size
#     left = loc['x']
#     top = loc['y']
#     width = size['width']
#     height = size['height']
#     box = (int(left), int(top), int(left + width), int(top + height))
#     screenshot = driver.get_screenshot_as_base64()
#     img = Image.open(BytesIO(base64.b64decode(screenshot)))
#     area = img.crop(box)
#     area.save('test-ixhd/screenshot{}.png'.format(i+1), 'PNG')
# PATH = 'https://sinvoice.viettel.vn/tracuuhoadon'
# for i in range(0,1):
#     driver.get(PATH)
#     driver.set_window_size(1853,743)
#     element = driver.find_element_by_xpath("//img[@id='imageCaptcha']")
#     loc = element.location
#     size = element.size
#     left = loc['x']
#     top = loc['y']
#     width = size['width']
#     height = size['height']
#     box = (int(left), int(top), int(left + width), int(top + height))
#     screenshot = driver.get_screenshot_as_base64()
#     img = Image.open(BytesIO(base64.b64decode(screenshot)))
#     area = img.crop(box)
#     area.save('test-viettel/screenshot{}.png'.format(i+1), 'PNG')
PATH = 'https://evat.hilo.com.vn/'
for i in range(0, 10):
    driver.get(PATH)
    element = driver.find_element_by_xpath("//img[@id='CaptchaImage']")
    print(element)
    loc = element.location
    print(loc)
    size = element.size
    # left = loc['x']
    # top = loc['y']
    # width = size['width']
    # height = size['height']
    left, top = 539, 404
    width, height = 208, 39

    box = (int(left), int(top), int(left + width), int(top + height))
    screenshot = driver.get_screenshot_as_base64()
    img = Image.open(BytesIO(base64.b64decode(screenshot)))
    area = img.crop(box)
    area.save('Detect/IMAGES//test/data{}.png'.format(i+1), 'PNG')