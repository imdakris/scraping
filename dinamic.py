from requests import Session
from bs4 import BeautifulSoup
import time, random
base_url = "https://scrapingclub.com/exercise/list_infinite_scroll/"
headers = {"User-Agent":
           "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"
           }

def main(base_url):
    s = Session()
    s.headers.update(headers)
    count = 1
    pagination = 0
    while True:
        if count > 1:
            url = base_url + '?page=' + str(count)
        else:
            url = base_url
        response = s.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        if count == 1:
            pagination = int(soup.find('ul', class_='pagination invisible').find_all('li', class_='page-item')[-2].text)
        cards = soup.find_all('div', class_="col-lg-4 col-md-6 mb-4")
        for card in cards:
            name = card.find('h4', class_="card-title").text
            price = card.find('h5').text
            print(name, price)
        print(count)
        time.sleep(random.choice([5,7,9]))
        if count == pagination:
            break
        else:
            count += 1


main(base_url)
