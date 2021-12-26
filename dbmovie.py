import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sparta:<password>@cluster0.8s2if.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbhandey

# movie = db.movies.find_one({'title':'스파이더맨: 노 웨이 홈'});
# star = movie['star']
# print(star);
#
# all_movies = list(db.movies.find({'star':star}, {'_id':False}));
# # all_movies = list(db.movies.find({조건문!}, {'_id':False}));
#
# for m in all_movies:
#     print(m['title']);


db.movies.update_one({'title':'스파이더맨: 노 웨이 홈'},{'$set':{'star':'0.00'}});