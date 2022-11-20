import requests
import json
import re
# def get_one_page(url):
#     headers = {
#         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
#     }
#     response = requests.get(url, headers=headers)
#     if response.status_code == 200:
#         return response.text
#     return None
# def main():
#     url = "http://maoyan.com/board/4"
#     # url = "http://www.baidu.com"
#     # html = get_one_page(url)
#     print(html)
#     with open("maoyan.html", mode="w", encoding="utf8") as f:
#         f.write(html)
# main()
with open("maoyan.html", mode="r", encoding="utf8") as f:
    html = f.read()
# print(html)
# response = re.search('<dd>.*?<i.*?>(.*?)</i>.*?<a.*?title="(.*?)".*?data-src="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', html, re.S)
# print(response)
# print(response.group(1))
# print(response.group(2))
# print(response.group(3))
# print(response.group(4))
# print(response.group(5))
# print(response.group(6))
# print(response.group(7))

# pattern = re.compile(
#     '<dd>.*?<i.*?>(.*?)</i>.*?<a.*?title="(.*?)".*?data-src="(.*?)".*?star">\s+(.*?)\s*?</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',
#     re.S
# )
# results = re.findall(pattern, html)
# print(type(results))
# print(results)

# for result in results:
#     print(result)
def parse_page_one(html):
    pattern = re.compile(
        '<dd>.*?<i.*?>(.*?)</i>.*?<a.*?title="(.*?)".*?data-src="(.*?)".*?star">(.*?)</p>.*?releasetime">(.*?)</p>.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',
        re.S
    )
    results = re.findall(pattern, html)
    for result in results:
        yield {
            'rank': result[0],
            'name': result[1],
            'image': result[2],
            'actor': result[3].strip()[3:] if len(result[3]) > 3 else "",
            'time': result[4][5:],
            'score': result[5] + result[6],
        }

results = parse_page_one(html)
print(type(results))

for result in results:
    # print(result)
    print(json.dumps(result, ensure_ascii=False))
