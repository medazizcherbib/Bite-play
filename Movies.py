import urllib.request
import urllib.parse
import urllib
from urllib.parse import urlencode
from urllib.request import Request, urlopen
import re
import sys
from bs4 import BeautifulSoup
import requests
import json
import time

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 ""Safari/537.36 "}


def get_movies_ids():
    try:
        for page_number in range(1, 2000):
            print("Page Num : " + str(page_number))
            url = "https://www.themoviedb.org/movie?page=" + str(page_number)
            scrap_html = urllib.request.Request(url)
            result = urllib.request.urlopen(scrap_html)
            result_data = result.read()
            movies_ids = re.findall(r'<p class="view_more"><a id="movie_(.*?)" class="result"', str(result_data))
            for movies_id in movies_ids:
                file.write(movies_id + "\n")
    except Exception as e:
        print(str(e))


file = open("movies_ids.txt", "w")
get_movies_ids()
file.close()
