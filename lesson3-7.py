import requests
from bs4 import BeautifulSoup

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
# data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=pnt&date=20210829',headers=headers)
data = requests.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver', headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


# print(soup)



# title = soup.select_one('#review1 > div > a')
# print(title['onclick'])




# old_content > table > tbody > tr:nth-child(2) > td.title > div > a
# old_content > table > tbody > tr:nth-child(7) > td.title > div > a


movies = soup.select('#old_content > table > tbody > tr')

for movie in movies:
    a = movie.select_one('td.title > div > a')

    if a is not None:
        title = a.text
        print(title)