import requests
from lxml import etree


class Picture(object):
    def __init__(self):
        self.url = "http://www.ivsky.com/tupian/meishishijie/"
        self.headers = {
            "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
        }

    def request_get(self, url):
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            print(response.text)
            return response.text
        return None

    def get_picture(self, text):
        html = etree.HTML(text)
        result = html.xpath('//div[@class="il_img"]//img')
        for i in result:
            src = i.get('src')
            alt = i.get('alt')
            print(src,alt)

    def run(self):
        text = self.request_get(self.url)
        self.get_picture(text)


picture = Picture()
picture.run()
