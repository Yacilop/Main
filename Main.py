import requests
from selectolax.parser import HTMLParser
from urllib.parse import unquote
import json
from datetime import datetime


def get_json(url):
    data = {}
    response = requests.get(url=url)
    html = response.text

    tree = HTMLParser(html)
    scripts = tree.css("script")
    for script in scripts:
        if 'window.__initialData__' in script.text():
            jsontext = (script.text().split(';')[0].split('=')[1].strip())
            jsontext = unquote(jsontext[1:-1])

            data = json.loads(jsontext)

            with open("data.json", 'w') as file:
                json.dump(data, file, ensure_ascii=False)
    return data

def get_offers(data):
    offers = []
    for key in data:
        if 'bx-single-page' in key:
            items = data[key]["data"]["catalog"]["items"]
            for item in items:
                if "id" in item:
                    offer = {}
                    offer['title'] = item['title'].strip().replace('\xa0', '')
                    offer['price'] = item['priceDetailed']['value']
                    offer['date'] = datetime.fromtimestamp(item['sortTimeStamp'] / 1000)
                    offer['url'] = 'https://www.avito.ru' + item['urlPath']

                    offers.append(offer)
    return offers

def main():
    url = 'https://www.avito.ru/mtsensk/kvartiry/sdam/na_dlitelnyy_srok-ASgBAgICAkSSA8gQ8AeQUg?cd=1'
    data = get_json(url)
    offers = get_offers(data)
    # with open('data.json', 'r', encoding="utf-8") as file:
    #     data = json.load(file)
    #     offers = get_offer(data)

    for offer in offers:
        print(offer)


if __name__ == '__main__':
    main()
