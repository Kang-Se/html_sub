import requests
from bs4 import BeautifulSoup



response = requests.get("https://movie.naver.com/movie/running/current.nhn")
soup = BeautifulSoup(response.text,'html.parser')

movie_section = soup.select('div[id=wrap] > div[id=container] > div[id=content] > div[class=article] > div[class=obj_section] > div[class=lst_wrap] > ul > li' )

movie_data = []

for movie in movie_section:
    movie_dict = {}
    a_tag = movie.select_one('dl > dt > a')
    movie_title = (str(a_tag).split('>')[1]).split('<')[0]
    movie_code = (a_tag['href'].split('?')[1]).split('=')[1]
    movie_dict["code"] = movie_code
    movie_dict["title"] = movie_title
    movie_data.append(movie_dict)
print(movie_data)
