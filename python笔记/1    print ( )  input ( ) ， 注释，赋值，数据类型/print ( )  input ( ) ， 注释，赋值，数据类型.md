# 第一课

# 数据类型

```python
-int：整型，整数  python的int包含了long，short
-float：浮点类型，小数，分数（其实就是除法的另一种表达）
-bool：布尔类型，Boolean类型
-number类型：数字类型
-str：string类型，字符串类型，所有的引号都是字符串类型
```

## int  整型

```python
变量名 = 整数
弱类型是由数值定义类型
强类型语言是声明定义去决定数值定义类型：int a = 1

例：
a = 18
print(a)
print(type(a))
结果：
<class 'int'>
```

## float   浮点类型

### ①凡是数字里面有小数点就是float类型

```python
a = 18.0
print(a)
print(type(a))
结果：
<class 'float'>（float类型）
```

### ②当int类型和float进行计算，

### 优先级float大于int，结果为float类型

```python
a = 18
b = 18.0
c = a + b
print(c)
print(type(c))
结果：
36.0
<class 'float'>
```



## bool布尔类型(重点难点)

### ①bool类型只有两个值，

### 一个是True（真），一个False（假）

```python
bool类型有且只有一种写法
首字母必须要大写，其他必须是小写
a = True
b = False
```

### ②bool值是可以运算的，在运算过程中：
True会变成1，False变成0

```python
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
```



# 输入输出

```python
print() 打印，输出
input() 输入
```



# 注释

## 单行

```python
#    
print("我是")  # 这个代码代表的作用是输出“我是”
```

## 多行

```python
'''
3对单引号
这个也是多行注释
'''

"""
三对双引号
"""
```



# 变量

## ”= “ 赋值

```python
x= "你好"    
#把 “你好” 这俩字赋值给  x   
print(x)    

结果：
你好

a = input("请输入数值")
print(a)
结果：
请输入数值（可接着输入）
```



# 标识符与关键字

## 规则：

```
1.首字符必须是大小写字母或者下划线
2.标识符必须是大小写字母，数字以及下划线组成

3.不能是有特殊符号$%&^*和关键字（保留字）if，True，while都不能用
```



## 常用规范命名方法：

### 下划线法：

### my_name  ming_zi

### 驼峰法：

#### ①大驼峰法：

##### MyName

首个单词的首字符是小写，其他单词的首字符是大写，其余是小写（小驼峰法常用于变量名和函数名）

#### ②小驼峰法：

##### myName

首个单词的首字符是小写，其他单词的首字符是大写，其余是小写（小驼峰法常用于变量名和函数名）

##### 

## 关键字

### import keyword

```python
print(keyword.kwlist)
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break',
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally',
 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal',
 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```





