import requests
import config
from bs4 import BeautifulSoup


URL = config.UTL_FOR_AUTH

print(requests.get(URL).text)