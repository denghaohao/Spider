import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.umei.cc/tupiandaquan/")
response.encoding = 'utf-8'
# print(response.text)

main_page = BeautifulSoup(response.text, 'html.parser')
alist = main_page.find_all('div', attrs={'class': 'taotu-main'})


# print(alist)
# print(type(alist))
n = 1
for items in alist:
    for item in items.find_all('li'):
        print(item.find('a').get('href'))
        # 拿到图片的链接，然后访问他
        resp = requests.get('https://www.umei.cc' + item.find('a').get('href'))
        resp.encoding = 'utf-8'
        c_page = BeautifulSoup(resp.text, 'html.parser')
        aelement = c_page.find('div', attrs={'class': 'big-pic'})
        src = aelement.find('img').get('src')
        with open(f'{n}.jpg', mode="wb") as f:
            f.write(requests.get(src).content)#写入二进制
            n += 1




