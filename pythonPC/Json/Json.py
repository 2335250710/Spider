import json

# python中支持单引号,但是转换数据类型的时候,要使用双引号
str = '{"neuedu":"Python","grade":1}'
print(str)
print(type(str))

# 将字符串转换成字典
dict_data_str = json.loads(str)
print(dict_data_str)
print(type(dict_data_str))

# 将字典转成json字符串,默认编码为ascii码,需要设置ensure_ascii为False
json_data = json.dumps(dict_data_str, ensure_ascii=False)
print(json_data)
print(type(json_data))

# 把字典转成json写入文件,写文件如果遇到编码ascii错误,可以指定编码格式为utf8
f = open('data.json', 'w', encoding='utf8')
json.dump(dict_data_str, f, ensure_ascii=False)

# 读取json文件中的内容,转换成字典
f = open('data.json','r',encoding='utf8')
dict_data = json.load(f)
print(dict_data)
print(type(dict_data['grade']))