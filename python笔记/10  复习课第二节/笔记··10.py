复习课 2
散列类型
1. 字典(dict)  储存数据，无序序列
格式：
	字典名= {key1: value1, key2: value2}
    a = {1: 1, 2: 2}
特征：数值可改变，但没下标值，没切片，用key定位
1.1 增
①  update(dict)
同key， 更新value
不同key，加dict

②  setdefault(key, defualt) default值可以不写，默认为None
同key，不改
没key值，添加
a = {1: 1, 2: 2}
a.setdefault(5, True)       #{1: 1, 2: 2, 5: True}
print(a)

③ dict[key] = value  不常用


1.2  删
①  .pop(key, default)  只有字典有default值
写default，没key，返default
没default，没key，报错

②  .popitem() 随机删除  (末尾)

③  del dict[key]/del dict

④  .clear()

1.3 查
①  .get(key,default)  default默认None
没key，没default ：回 None
没key，有default： 回default

②  dict[key]
用key找value值，没key：报错

1.4  常用方法   .items()键值对  .keys() .values()
      .fromkeys(key,value) 本身没添加功能，需用另一个变量储存
.fromkeys(key, value)：
a = ('x', 'y', 'z')
b = dict.fromkeys(a, 0)
print(b)  # {'x': 0, 'y': 0, 'z': 0}

.items()        （常用于输出字典中的所有键值对）
a = {'name': 'Alice', 'age': 30, 'city': 'New York'}
for key, value in a.items():
    print(f"Key: {key}, Value: {value}")
# Key: name, Value: Alice
# Key: age, Value: 30
# Key: city, Value: New York

2.  集合 set  {}
格式：
	集合名= {1,2,3,56,789}
    ①没key，没index值，真无序，无查询
    ②只能是str，number，bool，tuple类型
    ③数值没有重复，用于去重，

2.1  空集合
a = set()
print(a)

2.2    添加       .add(数值)
a = {1, 2, 3, 4, 5, 6, 7, 53.4, 4}
a.add(456)
print(a)

2.3   删除
.remove(数值)    报错法
.discard(数值)     不报错法

2.3     交&、并|、差-集


3.控制流程
3.1     比较运算符：>,<,==,>=,<=,!=       逻辑运算符:or and not
3.2     分支控制
    ①单分支:
    if 条件语句:
        代码块

    ②双分支:
    if 条件语句:
        代码块
        else:
        代码块

    ③多分支：
    if 条件语句:
        代码
        elif:
        代码
        else:
        代码块

3.3     循环控制
可迭代对象: list, str, tuple, dict, set, range(), values().items(), keys()

①   for 变量名 in 可迭代对象:
            代码块
②range(起点,终点, 步长)  =>切片

③while 条件语句:
    代码块

    死循环:
    while 1:    /   while True:

3.4     终止循环
continue:     暂时跳过
break:          直接结束

例：
a = 0
while a <= 5:
    a += 1
    if a == 4:
        continue
    print(a)
'''
1.  初始 a = 0
2.  a = 0 + 1 = 1，检查 1 == 4 为假，打印 1。
3.  a = 1 + 1 = 2，检查 2 == 4 为假，打印 2。
4.  a = 2 + 1 = 3，检查 3 == 4 为假，打印 3。
5.  a = 3 + 1 = 4，检查 4 == 4 为真，执行 continue，跳过打印。
6.  a = 4 + 1 = 5，检查 5 == 4 为假，打印 5。
7.  a = 5 + 1 = 6，检查 6 == 4 为假，打印 6。
8.  由于 a 已增加到 6，a <= 5 不再成立，循环结束。
'''

4. 函数
作用：储存代码的
格式：
def func():#定义
	代码块
func()# 调用

4.1    返回值     返回结果，结束程序
例1：
def ac():
    a = 5
    b = 9
    c = a * b
    d=a+b
    print(c)
    return  c   # 不写return就返回None
    print(d)    #return后的代码不运行
ac()

例2：
def bc(number):
    if number == 1:
        return True #判断为假不运行
    else:
        print(False)
bc(0)

4.2    带参函数
①多参数        传入的实参和形参一一对应
    def 函数名(多参数)
	    代码块
    函数名(多参数)

②不定长参数
    1.      元组  => 切片、遍历
def func(*args):
	代码块
函数名(数值)

def func(*args):
    Tu = args[0]
    print(Tu)
    # Tu => args
func(tuple(range(1, 100)))

   2.      字典
两种调用方式：
    2.1
    def 函数名(**字典)
        代码块
    2.2
    函数名(**dict)
    函数名(变量=数值)
    2.3     沿用字典用法=>增删改查
def func(**Dict):
    print(Dict.get("1"))
a = {"1": 1, "2": 2, "3": 3}
func(**a)

5.      内置函数
max()                                          最大值
min()                                           最小值
len()                                             长度函数
sorted(reverse=True/False)            排序
sum()                                           求和

6.      匿名函数   减少代码量，简化程序复杂性
格式:
lambda 变量名: 代码块

7.      文档字符串   输出函数的注释
def 函数名():
    """
    字符串
    """
print(函数名.__doc__)

8.      函数对象
    8.1  函数可以赋值
    8.2  作为元素使用
    8.3  函数可以传入另一个函数里面

9.      名称空间:储存名字的地方
    9.1 作用域：一个数值的使用范围
    9.2 global  全局变量  =>局部变全局
    例：
    def func1():
        global a
      a = 2
    def func2():
        print(f"func2：{a}")
    #   func2() => 必须要运行到global才变成全局
    func1()
    func2()
    print(a)

    9.3 nonlocal  局部变量  => 局部的全局 （仅嵌套函数里用）
    例：
    def main():
        a = 10  # main 中的变量 a
        def func1():
            a = 1.5  # func1 中的变量 a
            def func2():
                a = 222  # func2 中的变量 a
                def func3():
                    def func4():
                        nonlocal a  # 声明 a 是 func2 中的变量
                        a = 4
                        print(f"func4:{a}")  # func4 中的 a  (4)
                    func4()
                    print(f"func3:{a}")  #  func3 中的 a (4) func3中没有修改，继续影响
                func3()
                print(f"func2.2:{a}")  # func2 中的 a (4)  func4 中改了 a
            print(f"func1.1:{a}")  # 打印 func1 中的 a 值 (1.5)
            func2()
            print(f"func2:{a}")  # 打印 func1 中的 a 值 (1.5)
        func1()
        print(f"func1:{a}")  # 打印 main 中的 a 值 (10)

    main()

    '''
    执行过程：
    1.`main`函数:
        定义变量`a = 10`
        调用`func1`
    2.`func1` 函数
        定义变量 a = 1.5。
        打印 func1.1:{a}，输出 func1.1:1.5。
        调用 func2
    3.`func2`函数
        定义变量`a= 222`
        调用`func3`
    4.`func3`函数
        调用`func4`
    5.`func4`函数
        使用`nonlocal a` 声明`a`引用`func2`的变量`a`
        将`a` 修改为`4`
        打印`func4:{a}`，输出`func4:4`
    6.返回到`func3
        打印`func3:{a}`，输出`func3:4`(因为`a`被'func4`修改为'4`)
    7.返回到`func2
        打印`func2.2:{a}`，输出`func2.2:4`(因为｀a`被func4`修改为`4`)
    8.返回到`func1
        打印`func2:{a}`，输出`func2:1.5`(`func1'内的`a未被'func2'修改)。
        打印`func1:{a}`，输出`func1:10`(`main`内的`a未被`func1'修改)
    
    为什么`222`没有影响最终的输出
        1.在`func2'中，局部变量`a`被初始化为`222`
        2.当`func4'被调用时，使用了`nonlocal a`关键字，这意味着`func4'将修改`func2`中的变量｀a`。
        3.因此，`func4`中的`a= 4`直接修改了`func2`中的`a`使得'222`被`4`替换。
        4.所以在`func3`和`func2、中打印'a`时，显示的都是`4而不是`222`
        5.`nonlocal a`使得`func4`修改'func2`中的`a`，而`func2'中的`a`原本是`222`，被修改为`4`。
        6.因此，`func2`中的`a`不再是`222`，而是`4`。
    '''



3.列表，元组，字典，集合所有方法,整理一遍








