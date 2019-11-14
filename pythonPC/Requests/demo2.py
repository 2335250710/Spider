import requests
import json


class JinShan(object):
    def __init__(self,word):
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.headers={
    "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
    }
        self.post_data = {
            'f': 'auto',
            't': 'auto',
            'w': word
        }

    def request_post(self):
        response = requests.post(url=self.url,headers=self.headers,data=self.post_data)
        return response.content.decode()

    def parse_data(self,data):
        dict_data = json.loads(data)
        try:
            content = (dict_data['content']['out'])
        except:
            content = (dict_data['content']['word_mean'][0])
        print(content)

    def run(self):
        data = self.request_post()
        self.parse_data(data)


if __name__ == '__main__':
    import sys
    word = sys.argv
    for i in word:
        jinshan = JinShan(i)
        jinshan.run()
