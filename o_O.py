import requests
from bs4 import BeautifulSoup
from time import sleep

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Host": "httpbin.org",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36",
    "X-Amzn-Trace-Id": "Root=1-6448ff31-4d1cbae5563ca825330bbc4c"
}

for count in range(1, 8):
    sleep(3)
    url = f'https://scrapingclub.com/exercise/list_basic/?page={count}'

    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')  # html.parser

    data = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")

    for i in data:
        name = i.find('h4', class_="card-title").text.replace("\n", "")
        price = i.find('h5').text.replace('$', '')
        url_img = 'https://scrapingclub.com' + \
            i.find('img', class_="card-img-top img-fluid").get('src')

        print(name + '\n' + price + '\n' + url_img + '\n\n')
