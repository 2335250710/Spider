import requests

url = 'http://www.baidu.com/'

proxies = {
    'http': 'http://222.162.216.193:8080',
    'https': 'http://175.43.35.36:9999'
}

response = requests.get(url,proxies=proxies)
print(response.text)
print(response.status_code)