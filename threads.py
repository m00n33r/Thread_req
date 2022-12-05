from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import _thread
import time


def getLink(threadName, delay, iterations):
    url = 'https://en.wikipedia.org'
    html = urlopen(url + '/wiki/Python')
    bs = BeautifulSoup(html, features="lxml")
    start = int(time.time())
    links = bs.find('div', {'id': 'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)(.+)$'))
    for i in range(0, iterations):
        time.sleep(delay)
        seconds_elapsed = str(int(time.time()) - start)
        link = links[i].get('href')
        print(f'{seconds_elapsed}sec, Thread: {threadName}, Link: {url + link}\n-----------------')


def getText(threadName, delay, iterations):
    html = urlopen(
        'https://zen.yandex.ru/media/proglib/-dorojnaia-karta-pythonrazrabotchika-623dd80fab7d9d0b45b60d19?&')
    bs = BeautifulSoup(html, features="lxml")
    start = int(time.time())
    text = bs.find('div', {'class': 'publication-columns-layout__columns-container'}).find_all('span')
    for i in range(0, iterations):
        time.sleep(delay)
        seconds_elapsed = str(int(time.time()) - start)
        print(f'{seconds_elapsed}sec, Thread: {threadName}, Link: {text[i + 4].text}\n-----------------')


try:
    _thread.start_new_thread(getLink, ('WikiLinks', 2, 6))
    _thread.start_new_thread(getText, ('ZenText', 4, 3))
except:
    print('Ошибка потока')
while True:
    pass
