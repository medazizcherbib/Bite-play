import requests
import json
from pymongo import MongoClient

headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 ""Safari/537.36 "}

client = MongoClient('localhost', 27017)
db = client['bite&play']


def api_themoviedb_getdetails(id):
    try:
        themoviedb_api_url_details = 'https://api.themoviedb.org/3/movie/' + str(
            id) + '?api_key=67321a09b69f475100878a08a0bb7c78&language=en-US'
        themoviedb_api_url_video = "https://api.themoviedb.org/3/movie/" + str(
            id) + "/videos?api_key=67321a09b69f475100878a08a0bb7c78&language=en-US"
        details = requests.get(themoviedb_api_url_details)
        videos = requests.get(themoviedb_api_url_video)
        detail = json.loads(details.content.decode('utf-8'))
        video = json.loads(videos.content.decode('utf-8'))
        d = video.copy()
        d.update(detail)
        movies = db.movies
        movies.insert_one(d)
    except Exception as e:
        print(str(e))


file = open("movies_ids.txt", "r")
for x in range(1, 19999):
    print(str(x) + " sur 19999")
    api_themoviedb_getdetails(file.readline())
file.close()
