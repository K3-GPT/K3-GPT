第一课笔记
#这是几个常见的数据类型，现在不用刻意去记
-int：整型，整数  python的int包含了long，short
-float：浮点类型，小数，分数（其实就是除法的另一种表达）
-bool：布尔类型，Boolean类型
-number类型：数字类型
-str：string类型，字符串类型，所有的引号都是字符串类型

#这是前期学习的俩核心输入输出，需要记住
print() 打印，输出
input() 输入

1.注释
1.1单行注释：
#    这个#号代表单行注释
print("我是")  # 这个代码代表的作用是输出“我是”

1.2多行注释
"""
1. 是三对双引号
这个是多行注释
"""

'''
2.是3对单引号
这个也是多行注释
你喜欢哪一个都可以
'''

3.1  变量：
”= “ 赋值

x= "你好"    #把 “你好” 这俩字赋值给  x
print(x)

结果：
你好

a = input("请输入数值")
print(a)
结果：
请输入数值（可接着输入）

4.数据类型
常见类型：
-int：整型，整数  python的int包含了long，short
-float：浮点类型，小数，分数（其实就是除法的另一种表达）
-bool：布尔类型，Boolean类型
-number类型：数字类型
-str：string类型，字符串类型，所有的引号都是字符串类型
=》"xxxx"，除了bool类型或者number类型，其他都是字符串，也就是说不是bool值，或者数字，一律加上引号

如何知道该数值是什么类型：type+变量名

a = 1.0
b = 8
print(type(a))
print(type(b))
结果：
<class 'float'>（float类型）a
<class 'int'>（int类型）b

4.1 int整型
变量名 = 整数
弱类型是由数值定义类型
强类型语言是声明定义去决定数值定义类型：int a = 1

a = 18
print(a)
print(type(a))
结果：
<class 'int'>


4.2 float浮点类型
凡是数字里面有小数点就是float类型

a = 18.0
print(a)
print(type(a))
结果：
<class 'float'>（float类型）

当int类型和float进行计算，优先级float大于int，结果为float类型

a = 18
b = 18.0
c = a + b
print(c)
print(type(c))
结果：
36.0
<class 'float'>


4.3
bool布尔类型(重点难点)
bool类型只有两个值，一个是True（真），一个False（假）
类似对错：
True =》对
False =》错误
bool类型有且只有一种写法
变量名 = True
变量名 = False
写法如下：
首字母必须要大写，其他必须是小写
a = True
b = False

bool值是可以运算的，在运算过程中：
True会变成1，False变成0

a = True
b = False
print(a + b)
结果：
1

a = True + 0
b = False + 0
print(a)
print(b)
print(a + b)
结果：
1
0
1

5.标识符与关键字
标识符：就是名字的意思，和我们名字是一样的道理，常用于我们起名的；变量名，函数名，方法名，类名（就是名字）
规则：
1.首字符必须是大小写字母或者下划线
2.标识符必须是大小写字母，数字以及下划线组成
3.不能是有特殊符号$%&^*和关键字（保留字）if，True，while都不能用


5.1常用规范命名方法：
下划线法：
my_name  ming_zi
驼峰法：
小驼峰：
首个单词的首字符是小写，其他单词的首字符是大写，其余是小写（小驼峰法常用于变量名和函数名）
myName
大驼峰 ：
首个单词的首字符都是大写


5.2关键字
import keyword
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

6.作业
6.1使用变量储存个人信息（姓名，身高，年龄，身份证号码等）
6.2使用单行注释标注各个变量的含义，使用多行注释标注代码文件demo的功能作用、编写日期、开发人
6.3使用使用驼峰法（小驼峰或者大驼峰）命名变量名储存商品信息（商品名，商品价格，商品数量，以及日期是否过期）
要求【这里特指是数值，等于号的右边：商品名的数值是:字符串类型 ，商品价格的数值是:float类型（浮点类型），商品数量的数值是:int类型（整型类型）
日期是否(自己写)过期是:bool类型（真是不过期。假是过期）】
6.5选择题
补充：分号同一行的意思
1.在程序中，小明在交互模式输入if = 1 结果输出为（）
A. 1   B. 0   C. False  D. 程序报错
2.在程序中，小明在交互模式中输入
_=False
print(_)
结果输出为（）
A. 1   B. 0   C. False  D. 程序报错
3.在程序中，在交互模式中输入# while = 1 ; print(while)结果输出为（）
A. 1   B. 没有显示   C. False  D.程序报错
4.在程序中，交互模式中输入
false = 1
print(false)
结果输出为（）
A. 1   B. 没有显示   C. False  D.程序报错
5. 在程序中，交互模式输入
a1 = 1
b1 = 1.0
sum = a1 + b1
print(sum)
结果输出为（）
A. 2.0  B. 0   C. False  D. 程序报错


#开发人：KK
#时间：2023年8月14日22:39:23

name= "夸克" #开发人名字
age=18 #开发人年龄
high=168 #开发人身高
print(name) #输出名字
print(age) #输出年龄
print(high) #输出身高
print(type(name))
print(type(age))
print(type(high))

#商品名称
ShopName = "盼盼面包"
#价格
Money = 6.32
#数量
Quantity = 648
#是否过期
date = True #没过期
print(ShopName)
print(Money)
print(Quantity)
print(date)
print(type(ShopName))
print(type(Quantity))
print(type(Money))
print(type(date))

'''选择
D C B D A'''


作业评：
1.在程序中，小明在交互模式输入if = 1 结果输出为（D）
# if就是关键字
A. 1   B. 0   C. False  D. 程序报错
2.在程序中，小明在交互模式中输入 _=False; print(_)结果输出为（C）
# 这里False没有参与到运算，不是0，是False
A. 1   B. 0   C. False  D. 程序报错
3.在程序中，在交互模式中输入  # while = 1 ; print(while)结果输出为（B）
A. 1   B. 没有显示   C. False  D.程序报错
4.在程序中，交互模式中输入
false = 1
print(false)
结果输出为（A）
A. 1   B. 没有显示   C. False  D.程序报错
5. 在程序中，交互模式输入
a1 = 1
b1 = 1.0
sum = a1 + b1
print(sum)
结果输出为（A）
A. 2.0  B.0  C. False  D. 程序报错