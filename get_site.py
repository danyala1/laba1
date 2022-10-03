import time
import random
from bs4 import BeautifulSoup
import requests

import info


def get_site(add_url, base_url=info.base_URL):
    time.sleep(random.randint(20, 30))
    html_text = requests.get(base_url + add_url, headers={"User-Agent": info.user_agent}).text
    return BeautifulSoup(html_text, 'lxml')