import requests


class TieBa(object):
    def __init__(self,name,page):
        self.name = name
        self.url = 'https://tieba.baidu.com/f?ie=utf-8&kw={}'.format(self.name)
        self.headers={
"User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
}
        self.page = page
        self.url_list = [self.url+'&pn='+str(50*i) for i in range(self.page)]

    def get_data(self,url):
        response = requests.get(url,headers=self.headers)
        return response.content

    def save_data(self,data,num):
        with open(f'{self.name}{num+1}.html', 'wb') as f:
            f.write(data)

    def run(self):
        for url in self.url_list:
            data = self.get_data(url)
            num = self.url_list.index(url)
            self.save_data(data,num)


if __name__ == '__main__':
    tb = TieBa('ufo',3)
    tb.run()
