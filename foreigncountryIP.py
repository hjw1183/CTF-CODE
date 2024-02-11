# This Python file uses the following encoding: utf-8
# -*- coding: utf-8 -*-
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests
from bs4 import BeautifulSoup

data = open('netstat_v2.txt', 'rb').read()

ip_list = list(set(re.findall(b'\d[\ ]+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})', data)))

for ip in ip_list:
    print(ip.decode('utf-8'))

with open('foreigncountryIP.txt', 'w') as file:
    for ip in ip_list:
         file.write(str(ip.decode('utf-8')) + "\n")

options = Options()
options.headless = True
chromedriver_dir = "C:\python\driver\chromedriver.exe"
driver = webdriver.Chrome(chromedriver_dir, chrome_options=options)
driver.implicitly_wait(3)   


f = open('foreigncountryIP.txt')
url_list = f.read().split('\n')
f.close()


for i in range(len(url_list)):
    read_url = url_list[i]
    save_filename = "C:\\test\\test"+str(i)+".html"
    try:
        response = requests.get('https://ip2c.org/' + read_url)
        print("response.encoding = ",response.encoding)
        with open(save_filename, "w", encoding="utf-8") as output:
            output.write(response.text)
            print(read_url)
            country = response.text.split(';')[3]
            print(country)
            
    except Exception:
        try:
            driver.get(url_list[i])
            driver.implicitly_wait(2)
            with open(save_filename, "w", encoding="utf-8") as output:
                output.write(driver.page_source)
        except Exception:
            print("ERROR OCCURRED")

driver.close()
driver.quit()

