import requests
from pyquery import PyQuery as pq
import requests
from lxml import etree
import os


class BaiDu(object):
    def __init__(self,name):
        self.url = 'http://tieba.baidu.com/f?ie=utf-8&kw={}'.format(name)
        self.headers = {
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.01; Windows NT 5.0)'
        }
    # 发送请求，获取响应
    def get_data(self, url):
        response = requests.get(url,headers=self.headers)
        return response.content

    # 解析列表页数据，获取列表页面帖子的标题和链接
    def parse_list_page(self, data):
        with open('baidu.html', 'wb') as f:
            f.write(data)
        print(data)
        # html = etree.HTML(data)
        doc = pq(data)
        node_list = doc('.j_thread_list .threadlist_title a')
        # node_list = html.xpath("//*[@id='thread_list']/li[@class=' j_thread_list clearfix']/div/div[2]/div[1]/div[1]/a")
        # print(node_list)
        data_list = []
        # 遍历node_list
        for node in node_list.items():
            temp = {}
            # temp['url'] = 'http://tieba.baidu.com' + node.xpath('./@href')[0]
            # temp['title'] = node.xpath('./text()')[0]
            temp['url'] = 'http://tieba.baidu.com' + node.attr('href')
            temp['title'] = node.text()
            data_list.append(temp)
        # 提取下一页的节点
        # next_node = html.xpath('//*[@id="frs_list_pager"]/a[last()-1]/@href')[0]
        next_node = doc.find('#frs_list_pager .next').attr('href')
        # 拼接下一页的完整url
        next_url = 'http:' + next_node
        return data_list, next_url

    def parse_detail_page(self,data_list):
        # html = etree.HTML(data_list)
        doc = pq(data_list)
        # 提取详情页面的图片链接
        # image_list = html.xpath("//cc/div[contains(@class,'d_post')]/img[@class='BDE_Image']/@src")
        imagelst = doc.find('.BDE_Image').items()
        image_list = [img.attr('src') for img in imagelst]
        # 返回图片节点
        print(image_list)
        return image_list

    # 下载图片，保存图片文件
    # 创建文件夹
    def download(self, image_list):
        if not os.path.exists('images'):
            os.makedirs('images')
        for image in image_list:
            file_name = 'images'+ os.sep + image.split('/')[-1]
            image_data = self.get_data(image)
            with open(file_name,'wb') as f:
                f.write(image_data)

    def run(self):
        # 构造url和请求头
        # 发送请求，获取响应
        next_url = self.url
        # 开启循环
        while next_url:
            data = self.get_data(next_url)
            # 解析列表页数据，返回列表数据、下一页的数据
            data_list,next_url = self.parse_list_page(data)
            # 解析详情页的数据，获取详情页的图片的链接地址
            for data in data_list:
                url = data['url']
                result_list = self.get_data(url)
                image_list = self.parse_detail_page(result_list)
                # 保存数据，下载图片
                self.download(image_list)

b = BaiDu('校花吧')
b.run()