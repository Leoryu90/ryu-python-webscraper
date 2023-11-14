from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)

driver.get('https://kr.indeed.com/jobs?q=python&l=&from=searchOnHP&vjk=89395b6ac5014113')


base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"

response = get(f"{base_url}{search_term}")

if response.status_code != 200:
    print("Can't requests page")

else:
    print(response.text)


while (True):
    pass
