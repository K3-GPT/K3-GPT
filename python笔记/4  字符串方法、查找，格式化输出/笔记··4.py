1.字符串方法
1.1 			replace( )代替方法使用：
				格式：.replace("","")
replace(old,new,number)
old:       原来的字符
new：      代替的字符
number:    代替的个数，number可以不写，默认是全部（-1是结尾的意思），从左往右代替
	其中：个数值一定是int类型，全部的负数都是看作-1，就是全部的意思
	注：只有从左往右
例：全部的我改为你
#第一种：曲线修改
a = "我是kk，我身高180，年龄18岁"
b = a.replace("我","你")
print(b)
# 第二个，直接打印
print(a.replace("我","你"))
# 第三个，覆盖
a = a.replace("我","你")
print(a)

1.2 strip( )方法使用
	格式：strip(字符)
	注：删除字符串左右指定连续数值，匹配时不按照字符顺序
例：
a = "!!!!  !1!!!123!!1! !!!!"
print(a.strip("! "))

1.3 rstrip( )/lstrip()使用：lift right
	格式：lstrip：删除字符串左指定连续数值，匹配时不按照字符顺序
         rstrip：删除字符串右指定连续数值，匹配时不按照字符顺序
例：
a = "!!!!  !1!!!123!!1! !!!!"
print(a)#原话
print(a.lstrip("! "))#左边的！和空格
print(a.rstrip("! "))#右边的！和空格
print(a.lstrip("! 1"))
print(a.rstrip("! 1"))
print(a.rstrip("! 1,3"))

1.4 split( )分割方法使用：（输出的格式是列表，常用于爬虫）
		格式：split(字符,number)   根据输入的字符作为一个分割点 number：分割的次数， 为-1(全部的意思)
		注：没有从左往右切或者中间切
例：以逗号为分割点，分割全部
a = "123423523623723823923"
print(a.split("3",3))#,号前为切掉的数，,号后的为份数-1
b = "123,1234,1236,1235"
print(b.split(",")
结果：
['12', '42', '52', '62', '72', '82', '92', '']
['123', '1234', '1236', '1235']

1.5   upper( )，lower( ) title( )方法使用       大小写切换
		格式：upper() 字符串的字母全部改为大写
			 lower() 字符串的字母全部改小写
			 title() 字符串每一个单词(空格区分)的首字母大写，其他都是小写（类似大驼峰法）
例：
a = "hELlo woRLd"
print(a.upper())
print(a.lower())
print(a.title())


2. 字符串的查找
2.1 find(字符)： 查询字符串是否含有某个数值并输出该数值最左边的下标值（匹配不到的数值会输出-1）
		格式：find(字符,起点,终点) 终点是开区间 ，和切片是一样的道理
例：# 查找o
a = "hello worldo yujkucfo"
print(a.find("o",5,10))

2.2 endswith(字符)： 查询字符结尾是否是输入的字符串，输出bool值
		运用：判断文件后缀
		格式：a.endswith("字符串")
例：
a = "xxxx.py"
print(a.endswith(".py"))
print(a.endswith(".txt"))
b = "kk is bb"
print(b.endswith("bb"))
print(b.endswith("is"))

2.3 isdigit()：判断字符是否为纯数字组成，输出bool值
	运用：str(字符串）要换为int（整形），用到这个方法判断
例：
a = "123"
print(a.isdigit())
a = "123.0"
print(a.isdigit())


3.  格式化输出       仅是输出，本质不变
3.1 %格式化
%d  替换成整型格式                                              int
%f  替换成浮点类型格式，默认是小数点后6位，如果你想保留后a位，%.af      float
%s  替换成字符串格式                                            str
拓展：
浮点类型有偏差，后6位的数字会有浮动
1.111111 =》用的时候，计算的时候会有偏差：1.111119~1.111100

例：
%d 占位符
a = 1000.000
print(a)
b = "我的零花钱是%d" % a
print(b)
print(type(b))

%s 直接格式成字符串相当于str(数值)
注：最终只保留到后13位，且不四舍五入
a = 1000.00000000000000

#法一
b = "%s" % a
print(b)
#法二
c = str(a)
print(c)
结果：
1000.0

a = 1000.0575655462457
b = "%s" % a
print(b)
结果：
1000.0575655462457

%f 保留小数点后__位，有遵守四舍五入
a = 1000.666675474378348096368645
b = "%.9f" % a#		保留后9位
print(b)
print(type(b))
结果：
1000.666675474
<class 'str'>

3.2 format()格式化输出多个数值
格式一：
"{下标值1}{下标值2}".format(数值1,数值2,数值3)  根据右边的下标值进行填充
注：下标值从0开始，不可以左边下标值超过右边的最大下标值   下标值 能 为负
例：
print("kk又{1}又{0}{2}{3}{4}{5}".format("高","帅",4,89,",",12.3))
print("kk又{0}又{1}".format("高","帅"))
print("kk又{1}又{0}{5}{3}{2}{5}".format("高","帅",4,89,",",12.3))
结果：
kk又帅又高489,12.3
kk又高又帅
kk又帅又高12.389412.3

错例：
print("kk又{1}又{3}".format("高","帅"))
print("kk又{-1}又{-3}".format("高","帅"))

格式二：
"{变量名1}{变量名2}".format(变量名1=xxx,变量名2=xxx)
例：
a = "{name}个个都是{iKun}".format(name="同学们", iKun = "蔡徐坤")
print(a)
结果：
同学们个个都是蔡旭坤

错例：不符合标识符，所以不能这样用
a = "{0}个个都是{1}".format(0="同学们", 1 = "蔡旭坤")
print(a)
结果：expression cannot contain assignment

3.3 f-String:占位符{}
格式：变量名 = 数值
print(f"{变量名}")
例：
a = "高"
print(f"个个都很{a}")
a = 65
print(f"个个都很{a}")
a = 9.87
print(f"个个都很{a}")
a = True
print(f"个个都很{a}")
结果：
个个都很高
个个都很65
个个都很9.87
个个都很True


作业：
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




