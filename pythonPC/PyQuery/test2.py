import requests
from pyquery import PyQuery as pq

class DouBan(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/top250'
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'
        }

    def get_data(self):
        response = requests.get(self.url,headers=self.headers)
        return response.content.decode()

    def parse_data(self, data):
        # print(data)
        doc = pq(data)
        data_list = doc('.item').items()
        movie_list = []
        for movie in data_list:
            temp = {}
            temp['grade'] = movie.children('.pic em').text()
            temp['title'] = movie.children('.info .hd a span:first-child').text()
            temp['rate'] = movie.children('.info .bd .star span:lt(2)').text()
            movie_list.append(temp)
        print(movie_list)

    def run(self):
        data = self.get_data()
        self.parse_data(data)


b = DouBan()
b.run()
