from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
import time

# browser = webdriver.Chrome()
# try:
#     browser.get('https://www.baidu.com')
#     input = browser.find_element_by_id('kw')
#     input.send_keys('Python')
#     input.send_keys(Keys.ENTER)
#     wait = WebDriverWait(browser, 10)
#     wait.until(EC.presence_of_element_located((By.ID, 'content_left')))
#     print(browser.current_url)
#     print(browser.get_cookies())
#     print(browser.page_source)
# finally:
#     browser.close()

# browser.get('https://www.taobao.com')
# 单个节点
# input_first = browser.find_element_by_id('q')
# input_second = browser.find_element_by_css_selector('#q')
# input_third = browser.find_element_by_xpath('//*[@id="q"]')
# print(input_first,input_second,input_third)
# print(browser.page_source)
# 获取单个节点的方法
# find_element_by_id()
# find_element_by_name()
# find_element_by_xpath()
# find_element_by_link_text()
# find_element_by_partial_link_text()
# find_element_by_tag_name()
# find_element_by_class_name()
# find_element_by_css_selector()

# 多个节点
# lis = browser.find_elements_by_css_selector('.service-bd li')
# print(lis)
# 获取多节点的方法
# find_elements_by_id()
# find_elements_by_name()
# find_elements_by_xpath()
# find_elements_by_link_text()
# find_elements_by_partial_link_text()
# find_elements_by_tag_name()
# find_elements_by_class_name()
# find_elements_by_css_selector()

# 节点交互
# input = browser.find_element_by_id('q')
# input.send_keys('iPhone')
# time.sleep(1)
# input.clear()
# input.send_keys('iPad')
# button = browser.find_element_by_class_name('btn-search')
# button.click()

# 动作链
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to.frame('iframeResult')
# source = browser.find_element_by_css_selector('#draggable')
# target = browser.find_element_by_css_selector('#droppable')
# actions = ActionChains(browser)
# actions.drag_and_drop(source, target)
# actions.perform()

# 执行JavaScript
# browser.get('https://www.zhihu.com/explore')
# browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
# browser.execute_script('alert("To Bottom")')

# 获取节点信息
# get_attribute() 获取属性
# text  获得文本
# lis = browser.find_elements_by_css_selector('.service-bd li a')
# print(lis)
# for ele in lis:
#     print(ele.text)
#     print(ele.get_attribute('href'))
# browser.close()

# 切换frame
# url = 'http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable'
# browser.get(url)
# browser.switch_to_frame('iframeResult')
# try:
#     logo = browser.find_element_by_class_name('logo')
# except NoSuchElementException:
#     print('NO LOGO')
# browser.switch_to.parent_frame()
# logo = browser.find_element_by_class_name('logo')
# print(logo)
# print(logo.text)

# 延时等待
# 隐式等待 imlicitly_wait()
# browser.implicitly_wait(5)
# browser.get('https://www.taobao.com')
# input_first = browser.find_element_by_id('q')
# print(input_first)
# browser.close()
# 显示等待 until()
# browser.get('https://www.taobao.com')
# wait = WebDriverWait(browser, 10)
# input = wait.until(EC.presence_of_element_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)
# 等待条件
# title_is() 标题是某内容
# title_contains() 标题包含某内容
# presence_of_element_located() 节点加载出来 传入定位元组 例如(By.ID, 'p')
# visibility_of_element_located() 节点可见 传入定位元组
# visibility_of() 可见 传入节点对象
# presense_of_all_element_located()   所有节点加载出来
# text_to_be_present_in_element() 某个节点文本包含某文字
# text_to_be_present_in_element_value()   某个节点值包含某文字
# frame_to_be_available_and_switch_to_it()    加载并切换
# element_to_be_clickable()   节点可点击
# stateness_of()  判断一个节点是否仍在DOM 可判断页面是否刷新
# element_located_to_be_selected()    节点可选择 传入节点对象
# element_selection_state_to_be()     传入节点对象以及状态 相等返回True否则返回False
# element_located_selected_to_be()    传入定位元组以及状态 相等返回True否则返回False
# alert_is_present()      是否出现警告

# 前进和后退
# forword()前进 back()后退
# import time
# browser.get('https://www.baidu.com')
# browser.get('https://www.taobao.com')
# browser.get('https://www.python.org')
# browser.back()
# time.sleep(1)
# browser.forward()
# browser.close()

# Cookies
# 获取 get_cookies() 添加 add_cookies() 删除 delete_all_cookies()
# browser.get('https://www.zhihu.com/explore')
# print(browser.get_cookies())
# browser.add_cookie({'name':'name','domain':'www.zhihu.com','value':'germery'})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())

# 选项卡管理
import time

browser = webdriver.Chrome()
browser.get('https:www.baidu.com')
browser.execute_script('window.open()')
print(browser.window_handles)
browser.switch_to_window(browser.window_handles[1])
browser.get('https://www.taobao.com')
time.sleep(1)
browser.switch_to_window(browser.window_handles[0])
browser.get('https://python.org')