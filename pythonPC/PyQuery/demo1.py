html = '''
<div class="wrap">
    <div id="container">
        <ul class="list">
             <li class="item-0">first item</li>
             <li class="item-1"><a href="link2.html">second item</a></li>
             <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
             <li class="item-1 active"><a href="link4.html">fourth item</a></li>
             <li class="item-0"><a href="link5.html">fifth item</a></li>
         </ul>
    </div>
 </div>
'''

from pyquery import PyQuery as pq
doc = pq(html)
print(doc('li'))

# url初始化
doc = pq(url='http://www.baidu.com')
print(doc('head'))

# 基本css选择器
doc = pq(html)
print(doc('#container .list li'))

# 查找元素
# 子元素
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)

lis = items.children()
print(type(lis))
print(lis)

lis = items.children('.active')
print(lis)

# 父元素
doc = pq(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)

container = items.parents()
print(container)

parent = items.parents('.wrap')
print(parent)

# 兄弟元素
doc = pq(html)
li = doc('.list .item-0.active')
print(li.siblings())
print(li.siblings('.active'))

# 遍历
# 单个元素
doc = pq(html)
li = doc('.item-0.active')
print(li)

# 多个元素
lis = doc('li').items()
print(type(lis))
for li in lis:
    print(li)

# 获取属性
doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.attr('href'))
print(a.attr.href)

# 获取文本
print(a.text())

# 获取html
doc = pq(html)
li = doc('.item-0.active')
print(li)
print(li.html())

# DOM操作
# addClass、removeClass
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.remove_class('active')
print(li)
li.add_class('active')
print(li)

# attr、css
doc = pq(html)
li = doc('.item-0.active')
print(li)
li.attr('name','link')
print(li)
li.css('font-size','14px')
print(li)

# remove
htm1 = """
<div class="wrap">
    Hello, World
    <p>This is a paragraph.</p>
</div>
"""
doc = pq(htm1)
wrap = doc('.wrap')
print(wrap.text())
wrap.find('p').remove()
print(wrap.text())

# 伪类选择器
doc = pq(html)
li = doc('li:first-child')
print(li)
li = doc('li:last-child')
print(li)

li = doc('li:gt(2)')
print(li)

li = doc('li:contains(second)')
print(li)