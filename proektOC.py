import requests
from bs4 import BeautifulSoup
from time import sleep


elem = input('Введите инструмент из каталога, который вы ищите(электрогитара, акустическая гитара, синтезатор, звуковая карта, бас-гитара, комбоусилители): ').lower()
if elem == 'электрогитара':
    ssilka = 'https://www.muztorg.ru/category/elektrogitary?sort=price'
    n = 15
if elem == 'синтезатор':
    ssilka = 'https://www.muztorg.ru/category/sintezatory?sort=price'
    n = 6
if elem == 'акустическая гитара':
    ssilka = 'https://www.muztorg.ru/category/akusticheskie-gitary?sort=price'
    n = 24
if elem == 'звуковая карта':
    ssilka = 'https://www.muztorg.ru/category/zvukovye-karty?sort=price'
    n = 3
if elem == 'бас-гитара':
    ssilka = 'https://www.muztorg.ru/category/bas-gitary?sort=price'
    n = 4
if elem == 'комбоуселители':
    ssilka = 'https://www.muztorg.ru/category/kombousiliteli-dlya-elektrogitar?sort=price'
    n = 3

try:
    ssilka = ssilka
    response = requests.get(ssilka).text

    soup = BeautifulSoup(response, 'lxml')

    block_ssilka = 'https://www.muztorg.ru/' + soup.find('div', class_="product-caption").find('div', class_='title').find('a').get('href')
    block_nazvanie = soup.find('div', class_="product-caption").find('div', class_='title').text
    block_cena = soup.find('div', class_='product_offer').find('p', class_="price").text
    cena = ''.join(n for n in block_cena if n.isalnum()).lower()

    for p in range(1, n):
        url = ssilka+f'&page={p}'
        response = requests.get(url).text
        sleep(3)
        soup = BeautifulSoup(response, 'lxml')

        instrumentals = soup.findAll('div', class_="product-caption")

        for instrument in instrumentals:
            block_ssilka = 'https://www.muztorg.ru/' + instrument.find('div', class_='title').find('a').get('href')
            block_nazvanie = instrument.find('div', class_='title').text
            block_cena = instrument.find('p', class_="price").text
            cena = ''.join(n for n in block_cena if n.isalnum()).lower()
            print('Ссылка на товар : ', block_ssilka, 'Название товара : ', block_nazvanie, 'Цена товара :', cena)

except NameError:
    print('Такой товар не найден, либо его нет в программе')