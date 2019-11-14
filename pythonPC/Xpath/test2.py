import requests
from lxml import etree
import os


class BaiDu(object):
    def __init__(self,name):
        self.url = 'http://tieba.baidu.com/f?ie=utf-8&kw={}'.format(name)
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'
        }

    def get_data(self,url):
        response = requests.get(url,headers=self.headers)
        return response.content

    def parse_list_page(self, data):
        with open('baidu.html', 'wb') as f:
            f.write(data)
        print(data)
        html = etree.HTML(data)
        node_list = html.xpath("//*[@id='thread_list']/li[@class=' j_thread_list clearfix']/div/div[2]/div[1]/div[1]/a")
        print(node_list)
        data_list = []
        for node in node_list:
            temp = {}
            temp['url'] = 'http://tieba.baidu.com' + node.xpath('./@href')[0]
            temp['title'] = node.xpath('./text()')[0]
            data_list.append(temp)

        next_node = html.xpath('//*[@id="frs_list_pager"]/a[last()-1]/@href')[0]
        next_url = 'http:' + next_node
        return data_list,next_url

    def parse_detail_page(self,data_list):
        html = etree.HTML(data_list)
        image_list = html.xpath("//cc/div[contains(@class,'d_post')]/img[@class='BDE_Image']/@src")
        print(image_list)
        return image_list

    def download(self, image_list):
        if not os.path.exists('images'):
            os.makedirs('images')
        for image in image_list:
            file_name = 'images'+ os.sep + image.split('/')[-1]
            image_data = self.get_data(image)
            with open(file_name,'wb') as f:
                f.write(image_data)

    def run(self):
        next_url = self.url
        while next_url:
            data = self.get_data(next_url)
            data_list,next_url = self.parse_list_page(data)
            for data in data_list:
                url = data['url']
                result_list = self.get_data(url)
                image_list = self.parse_detail_page(result_list)
                self.download(image_list)

b = BaiDu('校花吧')
b.run()

