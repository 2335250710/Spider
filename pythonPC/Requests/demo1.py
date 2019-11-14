import requests
#
# response = requests.get('https://www.baidu.com')
# print(response.status_code) #打印状态码
# print(response.url)         #打印请求url
# print(response.headers)     #打印头信息
# print(response.cookies)     #打印cookie信息
# print(response.text)        #以文本的形式打印网页源代码
# # print(response.request)
# print(response.content)     #以字节流打印

# data = {
#     'name': 'germey',
#     'age': 22
# }
# response = requests.get('http://httpbin.org/get',params=data)
# print(response.text)
# print(response.json())
# print(type(response.json()))

# response = requests.get('blob:https://www.bilibili.com/c366b239-05a0-4732-8210-205a04320cc7')
# r = response.content
# with open('c.mp4','wb') as f:
#     f.write(r)

# header={
# "User-Agent":"Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16",
# }
# data={
#     'name': 'germey',
#     'age': 22
# }
# response = requests.post('https://httpbin.org/post',data=data,headers=header)
# print(response.text)

