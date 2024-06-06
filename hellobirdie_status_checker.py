from bs4 import BeautifulSoup
import requests
import csv

url = 'https://hellobirdie.2masterlight.site'
req = requests.get(url)
print(req.status_code)
soup = BeautifulSoup(req.text, "html.parser")

title = soup.title.string
print(title)