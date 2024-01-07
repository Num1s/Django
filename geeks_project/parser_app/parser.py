import requests
from bs4 import BeautifulSoup as bs 
from django.views.decorators.csrf import csrf_exempt

URL = "https://www.house.kg/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

@csrf_exempt
def get_html(url, params=''):
    request_house = requests.get(url, headers=HEADERS, params=params)
    return request_house

@csrf_exempt
def get_data(html):
    soup = bs(html, 'html.parser')
    items = soup.find_all('div', class_='category-block-content-item')
    houses = []
    for item in items:
        houses.append({
            'title_name': item.find('div', class_='main-title').get_text(),
            'price': item.find('div', class_='main-price').find('p', class_='price').find('span', class_='currency-2').get_text(),
            'city': item.find('div', class_='main-city').find('span', class_='main-city-span').get
        })

    return houses


@csrf_exempt
def parser_houses():
    html = get_html(URL)
    if html.status_code == 200:
        all_houses = []
        for page in range(0, 1):
            html = get_html(URL, params=page)
            all_houses.extend(get_data(html.text))

        return all_houses
    
    else:
        raise Exception('Error in parse')
