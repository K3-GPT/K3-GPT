

1. 下面字母输出全小写、全大写
(1) hello word
(2)	HELLO WORD

a = "hello world"
print(a.upper())
print(a.lower())

2. 按照要求进行输出
（1）"asw2ewwsdf":把所有里面的【w】改为【a】输出
（2）"123456789":以【5】字符为切割点，进行切分为2段
（3）"我好饿啊!!!!":把后面的【!】清除掉并查找里面的【饿】的字符

b = "asw2ewwsdf"
print(b.replace("w","i"))

c = "123456789"
print(c.split("5",2))

d = "我好饿啊!!!!"
print(d.rstrip("!"))
print(d.find("饿"))

3.请把下面的字符串安装特定的格式化要求输出
（1）创建变量a，b。分别赋值"高"，"帅"。然后进行放到字符串里面进行输出：字符串输出例如[我又高又帅]
（2）使用format把Name和Age放到字符串进行输出。例如：【我今年26岁，我是梓良老师】
（3）创建heigh（身高）变量，赋值178.67123，分别用%s,%d,%.2f进行输出

e = "高"
f = "帅"
g = "我很%s" %e
h = "也很%s"%f
print(g+h)
print("我不仅{}还{}".format("高","帅"))

print("我今年{0}岁，名字叫{1}".format(18,"kk"))

high = 178.67123
print("身高：%s"%high)
print("身高：%d"%high)
print("身高：%23.2f"%high)
