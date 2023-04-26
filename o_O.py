import requests
from bs4 import BeautifulSoup
from time import sleep

list_card_url = []
headers = {"User-Agent":
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
           }

for count in range(1, 8):
    sleep(1)
    url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')  # html.parser
    data = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")
    for i in data:
        card_url = "https://scrapingclub.com" + i.find('a').get('href')
        list_card_url.append(card_url)


for card_url in list_card_url:
    response = requests.get(card_url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    data = soup.find('div', class_="card mt-4 my-4")
    name = data.find('h3', class_='card-title').text
    price = data.find('h4').text
    text = data.find('p', class_='card-text').text
    url_img = 'https://scrapingclub.com' + data.find('img', class_='card-img-top img-fluid').get('src')
    print(name + '\n' + price + '\n' + text + '\n' + url_img + '\n\n')
