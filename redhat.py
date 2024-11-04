import numpy
import os
import time
import requests
import urllib
import re
import sys
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



if __name__ == "__main__":
    url_base = "https://access.redhat.com/security/security-updates/cve"

    options = Options()
    #options.set_headless(True)


    driver = webdriver.Chrome(chrome_options=options)
    driver.get("Security_Updates.html")

    html_base = driver.page_source.encode("utf-8")

    soup_base = BeautifulSoup(html_base.text, "html5lib")

    for a_each in soup_base.find_all("a"):
        #print(a_each)
        id_cand = a_each.get("href")
        print(id_cand)

    

"""
    url_base = "https://access.redhat.com/security/security-updates/cve"
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36"}

    
    html_base = requests.get(url_base, headers=header)

    soup_base = BeautifulSoup(html_base.text, "html5lib")

  

    
    for a_each in soup_base.find_all("a"):
        #print(a_each)
        id_cand = a_each.get("href")
        print(id_cand)

"""





