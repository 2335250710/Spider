import requests
import re


class maoyan(object):
    def __init__(self):
        self.url = 'https://maoyan.com/board/4'
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        }

    def requests_get(self):
        response = requests.get(self.url,headers=self.headers)
        if response.status_code == 200:
            print(response.text)
            return response.text
        return None

    def parse_one_page(self,html):
        pattern = re.compile(
            '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>(.*?)</p>.*?score.*?i.*?>(.*?)</i>.*?>(.*?)</i>.*?</dd>',re.S
        )
        items = re.findall(pattern, html)
        print(items)
        for item in items:
            print(item[0], item[1], item[2], item[3], item[4], item[5], item[6])

    def run(self):
        html = self.requests_get()
        self.parse_one_page(html)

my = maoyan()
my.run()
