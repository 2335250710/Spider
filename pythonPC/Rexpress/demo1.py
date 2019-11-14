import re

content = 'Hello 123 4567 World_This is a Regex Demo'

print(len(content))

result = re.match('^Hello\s\d\d\d\s\d{4}\s\w{10}',content)
print(result)
print(result.group())# 输出匹配的内容
print(result.span())# 输出匹配的范围

result = re.match('^Hello\s(\d+)\s(\d+)\sWorld',content)
print(result)
print(result.group())
print(result.group(1))
print(result.group(2))
print(result.span())

result = re.match('^Hello.*Demo$',content)
print(result)
print(result.group())

# 贪婪模式
result = re.match('^He.*(\d+).*Demo$',content)
print(result)
print(result.group(1))

# 使用.?拒绝贪婪模式
result = re.match('^He.*?(\d+\s\d+).*Demo$',content)
print(result)
print(result.group(1))

# 修饰符
content = '''Hello 1234567 World_This
is a Regex Demo'''
result = re.match('^He.*?(\d+).*?Demo$',content,re.S)#匹配换行符之外的任意字符 添加修饰符re.S
print(result.group(1))

# 转义匹配
content = '(百度)www.baidu.com'
result = re.match('\(百度\)www\.baidu\.com', content)
print(result.group())

content = 'Auto Hello 1234567 World_This is a Regex Demo'
result = re.match('He.*?(\d+).*Demo', content)
print(result) # 返回None

content = 'Auto Hello 1234567 World_This is a Regex Demo'
result = re.search('He.*?(\d+).*Demo', content)
print(result.group())

# search 实例
html = '''<div id="songs-list">
<h2 class="title">经典老歌</h2>
<p class="introduction">
经典老歌列表
</p>
<ul id="list" class="list-group">
<li data-view="2">一路上有你</li>
<li data-view="7">
<a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
</li>
<li data-view="4" class="active">
<a href="/3.mp3" singer="齐秦">往事随风</a>
</li>
<li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
<li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
<li data-view="5">
<a href="/6.mp3" singer="邓丽君">但愿人长久</a>
</li>
</ul>
</div>'''

result = re.search('li.*?active.*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result)
print(result.group(1))
print(result.group(2))

# findall()搜索整个字符串, 返回匹配规则的所有内容实例:
result = re.findall('li.*?href="(.*?)".*?singer="(.*?)">(.*?)</a>', html, re.S)
print(result)
[print(i[0],i[1],i[2]) for i in result]

# sub()参数1 参数2 规则 参数3 字符串
strs = '34iaU8hw9kcj2k3O0jc7oqqw8W'
strs = re.sub('\d+','',strs)# 去掉所有数字
print(strs)

# 获取html文本所有li节点的歌名
results = re.findall('<li.*?>\s*?(<a.*?>)?(\w+)(</a>)?\s*?</li>', html, re.S)
for result in results:
    print(result[1])