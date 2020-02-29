import requests
from urllib.parse import urljoin
from xml.etree import ElementTree as ET


def fetch_news(url='https://news.google.com'):
    '''
    Returns list of titles
    '''
    
    response = requests.get(urljoin(url, 'rss'))
    et = ET.fromstring(response.content)
    found_els = et.findall('channel/item/title')
    return [el.text for el in found_els]