import requests
from bs4 import BeautifulSoup
import pandas as pd

myurl = "https://maoyan.com/films?showType=3"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36"
header = {'user-agent': user_agent}
response = requests.get(myurl, headers=header)

print(response.text)
print(f'返回码是：{response.status_code},{response.url}')

soup = BeautifulSoup(response.text, "html.parser")

movies = soup.find_all('div', attrs={'class': 'movie-hover-info'}, limit=10)
# 保存数据
data = []
for m in movies:
    #title = m.find('span',attrs={'class':'name'}).text
    infos = m.find_all('div', attrs={'class': 'movie-hover-title'})
    # 名称
    name = infos[0].find('span', attrs={'class': 'name'}).text
    # 类型div
    cat_div = infos[1]
    # 日期div
    date_div = infos[3]
    # 去掉span
    cat_div.find('span').extract()
    date_div.find('span').extract()
    # 类型
    cat = cat_div.text.strip().replace('\n', '').replace('\r', '')
    # 日期
    date = date_div.text.strip().replace('\n', '').replace('\r', '')
    print(name)
    print(cat)
    print(date)
    data_list = [name, cat, date]
    data.append(data_list)
print(data)
df = pd.DataFrame(data)
# windows 用gbk
df.to_csv('./maoyan1.csv', encoding='gbk', index=False, header=False)

