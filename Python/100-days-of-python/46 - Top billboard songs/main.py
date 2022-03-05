import requests
import datetime as dt
import random
from bs4 import BeautifulSoup

class SongWithArtist:
    def __init__(self, artist, song):
        self.artist = artist
        self.song = song
    pass

def get_random_date_str():
    day =  random.randint(1, 28)
    month = random.randint(1,12)

    if (day<10):
        day = "0" + str(day)
    if (month<10):
        month = "0" + str(month)

    year = random.randint(2000, dt.datetime.now().year)

    return f"{year}-{month}-{day}"

TEST = "https://www.billboard.com/charts/hot-100/2000-06-21/"
URL = "https://www.billboard.com/charts/hot-100"

date = get_random_date_str()
#html = requests.get(url=f"{URL}/{date}").text
html = requests.get(url=TEST).text
soup = BeautifulSoup(html, "html.parser")

print(f"{URL}/{date}")
songs = []
items = soup.select(selector=".o-chart-results-list__item.lrv-u-flex-grow-1.lrv-u-flex.lrv-u-flex-direction-column")
for item in items:
    title = item.select_one(selector="#title-of-a-story").text.rstrip().lstrip()
    artist = item.select_one(selector=".c-label").text.rstrip().lstrip()
    songs.append(SongWithArtist(artist, title))
print(songs)

for song in songs:
    print(f"Artist: {song.artist} Song: {song.song}")
print(len(songs))



