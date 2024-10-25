from bs4 import BeautifulSoup
import requests

url = "https://www.pracuj.pl/praca/data%20scientist;kw?sal=1"
HEADERS = {
  "Access-Control-Allow-Origin": "*",
  "Content-Encoding": "gzip",
  "Content-Type": "text/html; charset=utf-8",
  "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7",
  "Sec-Ch-Ua": "\"Chromium\";v=\"118\", \"Google Chrome\";v=\"118\", \"Not=A?Brand\";v=\"99\"",
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
}

html_text = requests.get(url, headers=HEADERS)  # dodajemy headers zeby strona nie wykryla nas jako boty
soup = BeautifulSoup(html_text.text,
                     'lxml')  # lxml pozwala czytac html, a jest szybszy od html.parser wbudowanego w pythona

jobs = soup.find_all("div", class_="tiles_b18pwp01 core_po9665q")

print("Which town do you want to avoid")
unwanted_town = input('>')

for job in jobs:

  job_title = job.find("h2", class_="tiles_h1p4o5k6").text
  salary = job.find("span", class_="tiles_s1x1fda3").text
  company = soup.select_one(
    '#offers-list > div.listing_b1i2dnp8 > div.listing_ohw4t83 > div:nth-child(1) > div > div.tiles_cjkyq1p > div.tiles_cghoimp > div.tiles_c2ezmf3 > div.tiles_c3ppts3 > div > a').text
  link = job.div.div.a['href']  # wchodzimy po kolei do kolejnych divów
  town = job.find("h4", class_="tiles_r11dm8ju size-caption core_t1rst47b")
  town_2 = job.find("h4", class_="tiles_ws487bk size-caption core_t1rst47b")
  # dzieki select_one wyszukujemy dane za pomoca tagow, zwracamy pierwszy znaleziony element
  if town == None:
    town = town_2.span.text
  else:
    town = (town.text)

  if unwanted_town in town:
    continue

  print(job_title)
  print(salary)
  print(company)
  print(town)
  print(link)
  print()
