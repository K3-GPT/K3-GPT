1.
创建变量，从1到100进行输出，数值之间用【, 】分开
for a in range(0,100) :
    print(a,end="，")

2.根据第一题进行改进，主要数值分别输出奇数、偶数、3 / 5 / 7的倍数、2和3的公共倍数
方法一：（奇数偶数）
for a in range(1, 101,2):
        print(a, end="，")
print(end="\n")
for a in range(2, 101,2):
        print(a, end="，")
方法二：
for a in range(1, 101):
    if a % 2 != 0:
        print(a, end="，")
print(end="\n")
for a in range(1, 101):
    if a % 2 == 0:
        print(a, end="，")

2和3的公共倍数
for a in range(1, 101):
    if a % 2 ==0 and a % 3 == 0:
        print(a, end="，")

3     5      7的倍数
for a in range(1, 101):
        print(a*3, end="，")
print(end="\n")

for a in range(1, 101):
        print(a*5, end="，")
print(end="\n")

for a in range(1, 101):
        print(a*7, end="，")
print(end="\n")

改：
for i in range(1,101):
    if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print(i, end=" ")

3.
根据第一题再进行改进，数值输出到80就停止输出
for a in range(1, 101):
    print(a, end="，")
    while a==80:
        continue

4.
创建一个字典    {"name": "屠龙刀", "price": 10000, "cid": 1001, "count": 1},     分别打印字典里面的key值和value值
a =  {"name": "屠龙刀", "price": 10000, "cid": 1001, "count": 1}
print(a.keys())
print(a.values())

改:
for i in a:
    print(f"key值为：{i[0]}",end="   ")
    print(f"values值为：{i[1]}")
5.
打印倒立直角三角形：
* * * * *
* * * *
* * *
* *
*
for i in range(5, 0, -1):  # 外层循环，从5开始，到1结束，每次递减1，控制行数
    for j in range(1, i + 1):  # 内层循环，从1开始，到i+1结束，控制每行输出的 '*' 数量
        print("*", end=" ")
    print()


附加题：(挑选，并不评讲，我下一节课上传我做的代码，用算法做的)
打印等边三角形，菱形，空心菱形（地狱级别）
等边三角形：
    *
  * * *
* * * * *

菱形：
    *
  * * *
* * * * *
  * * *
    *

空心菱形：
*
* *
* *
* *
*


#主要数值分别输出奇数、偶数、3 / 5 / 7的倍数、2和3的公共倍数
a = 0
for a in range(0,100) :
    a=a+1
 #   print(i,end="，")
ji = list[range()]
    print(a)

# 输出1到100之间的数字，数值之间用 , 分开
numbers = list(range(1, 101))
print(','.join(map(str, numbers)))

# 输出奇数
odd_numbers = [num for num in numbers if num % 2 != 0]
print("奇数:", ','.join(map(str, odd_numbers)))

# 输出偶数
even_numbers = [num for num in numbers if num % 2 == 0]
print("偶数:", ','.join(map(str, even_numbers)))

# 输出3/5/7的倍数
special_numbers = [num for num in numbers if num % 3 == 0 or num % 5 == 0 or num % 7 == 0]
print("3/5/7的倍数:", ','.join(map(str, special_numbers)))

# 输出2和3的公共倍数
common_multiples = [num for num in numbers if num % 2 == 0 and num % 3 == 0]
print("2和3的公共倍数:", ','.join(map(str, common_multiples))










