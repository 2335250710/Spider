import requests
from lxml import etree

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
        print(data)
        html = etree.HTML(data)
        grade_list = html.xpath('//*[@class="grid_view"]/li/div/div/em/text()')
        title_list = html.xpath('//*[@class="grid_view"]/li/div/div/div/a/span[1]/text()')
        actors = html.xpath('//*[@class="grid_view"]/li/div/div/div/p[1]/text()')
        temp = {}
        # temp1 = {}
        actor = [actor for actor in actors]
        title = [title for title in title_list]
        grade = [grade for grade in grade_list]
        # for i in range(len(title)):
        #     temp1[title[i]] = actor[i]
        temp1 = {i: j for i, j in zip(title, actor)}
        # print(temp1)
        l = [{i[0]:i[1]} for i in temp1.items()]
        for i in grade:
            temp[i] = l[int(i)-1]
        print(temp)

    def run(self):
        data = self.get_data()
        self.parse_data(data)


b = DouBan()
b.run()