import pandas as pd
import requests
from bs4 import BeautifulSoup as bs

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'
cookie = 'uuid_n_v=v1; uuid=9723B330B85D11EA9B3075693A212BAF01F225023F47431C97B6440322F271D6; _csrf=5ae25f10be0efec67167e4b4eef026bdf596e29569609aa3069e8e492c308b00; mojo-uuid=545a2986730bccc76547d372a7c4ee19; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593252281; _lxsdk_cuid=172f53c7ac6c8-090694edfaaf9f-4353761-1fa400-172f53c7ac6c8; _lxsdk=9723B330B85D11EA9B3075693A212BAF01F225023F47431C97B6440322F271D6; mojo-session-id={"id":"2ebce9ecd26606c9a9afae6d0e6c4491","time":1593334278390}; mojo-trace-id=2; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593334321; __mta=108418493.1593252282066.1593334281225.1593334323593.3; _lxsdk_s=172fa1f9095-dd1-1c-89c%7C%7C5'

header = {}
header['user-agent'] = user_agent
header['cookie'] = cookie

url = 'https://maoyan.com/films?showType=3'

response = requests.get(url, headers=header)
# print(f'返回码:{response.status_code}')

bs_info = bs(response.text, 'html.parser')

movies = []
movies.append(("电影名称", "电影类型", "上映时间"))

for tag in bs_info.find_all('div', attrs={'class': 'movie-item-hover'}, limit=10):
    movie_title = tag.find('span', attrs={'class': 'name'}).text

    film_tags = tag.find_all('div', attrs={'class': 'movie-hover-title'})
    movie_tag = film_tags[1].text[4:].strip()
    plan_date = film_tags[3].text[6:].strip()

    movies.append((movie_title, movie_tag, plan_date))

maoyan = pd.DataFrame(data=movies)
maoyan.to_csv('./result/maoyan1.csv', encoding='utf8',
              index=False, header=False)
