from bs4 import BeautifulSoup
import requests
import selenium
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException        

import threading

links = ["https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1800&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1810&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1820&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1830&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1840&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1850&gender=F&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1860&gender=F&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1870&gender=F&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1880&gender=F&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1890&gender=F&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1850&gender=M&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1860&gender=M&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1870&gender=M&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1880&gender=M&count=100&offset=",
"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1890&gender=M&count=100&offset="]
def setup(linknum):

    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory' : "/Users/baltasarsalamonwelwert/Downloads/Fabi"}
    chrome_options.add_experimental_option('prefs', prefs)
    #chrome_options.headless = True
    driver = webdriver.Chrome(options=chrome_options)

    driver.implicitly_wait(10)
    #site = "https://www.familysearch.org/auth/familysearch/login?icid=hr-signin&returnUrl=https%3A%2F%2Fwww.familysearch.org%2Fsearch%2Frecord%2Fresults%3Frecord_country%3DChile%26collection_id%3D1520559%26count%3D100%26offset%3D0&ldsauth=false"
    #site = "https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year0=1800&count=100&offset=0"
    #site = "https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year1=1800~1800&count=100&offset=0"
    site = links[linknum]
    username = ""       //FILL THESE OUT
    password = ""
    driver.get(site)
    driver.find_element_by_id("userName").send_keys(username)
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("login").click()
    return driver

def expand_shadow_element(element,g):
  shadow_root = g.execute_script('return arguments[0].shadowRoot', element)
  return shadow_root

def get_elem(driv):   
    root = driv.find_element_by_css_selector("search-artifact-results")
    expanded_root = expand_shadow_element(root,driv)
    #try:
    #    expanded_root.find_element_by_class_name("fs-alert fs-alert--error errorMessage")
    try:
        print("Not found")
        root2 = expanded_root.find_element_by_css_selector("sr-panels")
        expanded_root2 = expand_shadow_element(root2,driv)

        root3 = expanded_root2.find_element_by_css_selector("sr-records")
        expanded_root3 = expand_shadow_element(root3,driv)

        expanded_root3.find_element_by_css_selector("button").click()
    except:
        print("found")
        driv.refresh()
        get_elem(driv)

def download(n,link):
    b = setup(link)
    time.sleep(10)
    root = b.find_element_by_css_selector("search-artifact-results")
    expanded_root = expand_shadow_element(root,b)
    root2 = expanded_root.find_element_by_css_selector("sr-panels")
    expanded_root2 = expand_shadow_element(root2,b)

    root3 = expanded_root2.find_element_by_css_selector("sr-records")
    expanded_root3 = expand_shadow_element(root3,b)
    try:
        a = round(int(str(expanded_root3.find_element_by_class_name("search-criteria").text).split(" ")[2])/100)+1
        print("a: ", a)
        offset = int((a * 100)/2)
    except:
        print("asjkd")
        b.refresh()
        a = round(int(str(expanded_root3.find_element_by_class_name("search-criteria").text).split(" ")[2])/100)+1
        print("a: ", a)
        offset = int((a * 100)/2)

    #b.get(f"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&count=100&offset={offset}")
    for i in range(a):
        #print(offset)
        get_elem(b)
        time.sleep(3)
        offset += 100
        #b.get(f"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&count=100&offset={offset}")
        #b.get(f"https://www.familysearch.org/search/record/results?record_country=Chile&collection_id=1520559&birth_place1=8%2CChile&death_year0=1800&count=100&offset={offset}")
        b.get(links[link] + str(offset))
    print(f"Worked page {offset}" )
    b.quit()
    #driver.quit()
threads = list()
for i in range(10):

    start = 2500 * i 
    try:
        x = threading.Thread(target=download, args=(start,i,))
        threads.append(x)
        x.start()
    except:
        pass

for i in enumerate(threads):
    x.join()
