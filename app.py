from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import json

search_model = '718 cayman 2024'

driver = webdriver.Firefox()
driver.get("https://www.auto-data.net/en/")

model_dict = {}
wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchdivinput"]')))
search_input = driver.find_element(By.XPATH, '//*[@id="searchdivinput"]')
search_input.send_keys(search_model)

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="ajaxSearchDiv"]')))
options = driver.find_elements(By.CLASS_NAME, 'optionDiv')
options[0].click()

wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/table/caption/h2')))
table = driver.find_element(By.XPATH, '/html/body/div[2]/table/tbody')
table_head = table.find_elements(By.XPATH, "//tr[@class='no']")
table_all = table.find_elements(By.TAG_NAME, 'tr')

#dict inside dict
car_model_dict = {}
temp_dict = {}
data_section = 'general_information'

for elem in table_all:
    strong_elem = elem.find_elements(By.TAG_NAME, 'strong')
    if len(strong_elem) > 0 :
        if len(temp_dict) == 0:
            continue
        
        #add car info section dict into car model dict
        car_model_dict[data_section] = temp_dict
        temp_dict = {}

        #renew the data section name
        data_section = strong_elem[0].text.lower().replace(',', '').replace(' ', '_')
    else:
        if len(elem.find_elements(By.TAG_NAME, 'td')) < 1:
            continue
        
        table_head = elem.find_element(By.TAG_NAME, 'th').text
        #remove any element inside ()
        table_head = re.sub(r'\s*\([^)]*\)', '', table_head)
        table_head = table_head.lower().replace('.', '').replace('-', '').replace(' ', '_')
        table_head = table_head.replace('__', '_')

        table_data = elem.find_element(By.TAG_NAME, 'td').text
        table_data = table_data.split('\n', 1)[0]

        #add car data into temporary dict
        temp_dict[table_head] = table_data

driver.find_element(By.XPATH, '/html/body/div[2]/div[4]/img').click()

wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="slider"]')))
images_slider = driver.find_element(By.XPATH, '//*[@id="slider"]')
image_thumbs = images_slider.find_elements(By.TAG_NAME, 'img')
big_image = driver.find_element(By.XPATH, '//*[@id="bigimg"]')

image_count = 1
data_section = 'images'
temp_dict = {}

wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="slider"]')))
for thumb in image_thumbs:
    images_slider.send_keys(Keys.DOWN)
    image_source = big_image.get_attribute('src')
    temp_dict[f'image_{image_count}'] = image_source
    image_count += 1

car_model_dict[data_section] = temp_dict

with open('car_model.json', 'w') as json_file:
    json.dump(car_model_dict, json_file, ensure_ascii = False)