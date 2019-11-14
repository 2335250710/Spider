from lxml import etree
text = '''
<div>
<ul>
<li class="item-0 li"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive" name="hhh"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0 li"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)

# 返回所有节点数据
result = html.xpath('//*')
print(result)

# 返回指定节点数据
result = html.xpath('//li')
print(result)

# /子节点//子孙节点
result = html.xpath('//li/a')
print(result)
result = html.xpath('//ul//a')
print(result)

# 父节点..|parent::
result = html.xpath('//a[@href="link4.html"]/../@class')#获取href属性为link4.html的a标签的父节点的class内容
print(result)
result = html.xpath('//a[@href="link4.html"]/parent::*/@class')#获取href属性为link4.html的a标签的父节点的class内容
print(result)

# 属性过滤
result = html.xpath('//li[@class="item-1"]')#选取class为item-0的li节点
print(result)

# 文本获取
result = html.xpath('//li[contains(@class,"item-0")]/text()')#直接获取子节点
print(result)#返回结果为换行符

result = html.xpath('//li[@class="item-1"]/a/text()')
print(result)

result = html.xpath('//li[@class="item-1"]//text()')
print(result)

# 属性获取
result = html.xpath('//li/a/@href')
print(result)

# 属性多值匹配
result = html.xpath('//li[contains(@class,"item-0")]/a/text()')
print(result)

# 多属性匹配
result = html.xpath('//li[@class="item-inactive" and @name="hhh"]/a/text()')
print(result)

# 按序选择
result = html.xpath('//li[1]/a/text()')
print(result)#返回第一个节点 注意这里序号是从1号开始的

result = html.xpath('//li[last()]/a/text()')
print(result)#返回最后一个节点

result = html.xpath('//li[position()<3]/a/text()')
print(result)#返回前两个

result = html.xpath('//li[last()-2]/a/text()')
print(result)#返回倒数第三个

# 节点轴选择
text = """
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
"""

html = etree.HTML(text)
result = html.xpath('//li[1]/ancestor::*')
print(result)#获取第一个li所有祖先节点

result = html.xpath('//li[1]/ancestor::div')
print(result)#限定条件 div

result = html.xpath('//li[1]/attribute::*')
print(result)#获取所有属性值 返回li节点所有属性值

result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)#获取所有子节点 限定条件href = link1.html

result = html.xpath('//li[1]/descendant::span')
print(result)#获取所有的子孙节点,限定span节点,不包含a节点

result = html.xpath('//li[1]/following::*[2]')
print(result)#获取当前节点之后的所有节点,虽然加了*但又加了索引选择 只获取带第二个后续节点

result = html.xpath('//li[1]/following-sibling::*')
print(result)#获取当前节点之后的所有同级节点
