# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.keys import Keys
# import pymongo,time
#
#
# class JD(object):
#     def __init__(self):
#         host = "localhost"
#         dbname = 'JDsearch'
#         dbcol = 'JD'
#         search = input('请输入搜索的类容：')
#         self.browser = webdriver.Chrome()
#         self.browser.get('https://search.jd.com/Search?keyword={}&enc=utf-8'.format(search))
#         self.client = pymongo.MongoClient(host=host, port=27017)
#         self.db = self.client[dbname]
#         self.collections = self.db[dbcol]
#
#     def get_data(self):
#         self.browser.implicitly_wait(10)
#         self.browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
#         self.browser.implicitly_wait(10)
#         ul = self.browser.find_element_by_class_name('gl-warp')
#         items = ul.find_elements_by_class_name('gl-item')
#         print(len(items))
#         if len(items) == 60:
#             return items
#         else:
#             self.get_data()
#
#     def parser_data(self, items):
#         for item in items:
#             link = item.find_element_by_css_selector(".p-img a").get_attribute("href")
#             img = item.find_element_by_css_selector(".p-img a img").get_attribute("src")
#             if not img:
#                 img = item.find_element_by_css_selector(".p-img a img").get_attribute("data_lazy_img")
#                 print(img)
#                 img = "https:" + img
#             price = item.find_element_by_css_selector(".p-price i").text
#             title = item.find_element_by_css_selector(".p-name a em").text
#             trade_name = item.find_element_by_css_selector(".p-shop a").text
#             commit = item.find_element_by_css_selector(".p-commit").text
#             data = {"link": link, "img": img, "title": title, "shop_name": trade_name, "commit": commit, "price": price}
#             self.save_to_mongo(data)
#
#     def save_to_mongo(self, data):
#         try:
#             if self.collections.insert_one(data):
#                 print("save to mongodb success!", data)
#         except Exception:
#             print('save to mongodb false!')
#
#     def get_next_page(self):
#         next_page = self.browser.find_element_by_partial_link_text("下一页")
#         next_page.click()
#         time.sleep(1)
#         items = self.get_data()
#         print(items)
#         self.parser_data(items)
#
#     def run(self):
#         items = self.get_data()
#         print(1)
#         self.parser_data(items)
#         print(2)
#         self.get_next_page()
#         print(3)
#
# if __name__ == "__main__":
#     jd = JD()
#     jd.run()