import requests
from bs4 import BeautifulSoup

# <웹스크래핑 결과 DB에 저장하기>


from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:<password>@cluster0.8s2if.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbhandey


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20211218', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a = movie.select_one('td.title > div > a')

    if a is not None:
        title = a.text
        rank = movie.select_one('td:nth-child(1) > img')['alt']
        star = movie.select_one('td.point').text

        doc = {
            'title': title,
            'rank': rank,
            'star': star
        };

        db.movies.insert_one(doc);



