import requests
from lxml import etree

# 目标地址
url = 'https://nba.hupu.com/stats/players'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36 Core/1.77.119.400 QQBrowser/10.9.4817.400'}
# 发送请求
resp = requests.get(url, headers=headers)
# print(resp.text)
# 处理结果
e = etree.HTML(resp.text)
# 解析响应的数据
names = e.xpath('//table[@class="players_table"]//tr/td[2]/a/text()')
teams = e.xpath('//table[@class="players_table"]//tr/td[3]/a/text()')
# 是否保存
# print(names)
# print(teams)
with open('nba.txt', 'w',encoding='utf-8') as f:
    for name, team in zip(names, teams):
        # print(f'姓名：{name}, 球队：{team}')
        f.write(f'姓名：{name}, 球队：{team}\n')

