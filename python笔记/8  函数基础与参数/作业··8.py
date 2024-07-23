1.
定义一个计算函数，输入相关的数值，进行四则运算（加减乘除）
未做完：
def num():
    while True:
        num = 0  # 初始化变量 e
        num1 = input("输入数值：")  # 获取用户输入的第一个数值
        while True:     #死循环，不输入1--4就不下一步
            num2 = input("输入运算法则：1 = +, 2 = -, 3 = *, 4 = /")  # 获取用户输入的运算符号
            num2 = int(num2)  # 将用户输入的运算符号转换为整数类型
            if num2 not in [1, 2, 3, 4]:  # 检查用户输入的运算符号是否合法
                print("请重新输入")
            else:
                break

        if num2 == 1:
            print(num1 + "+")  # 执行加法运算
        elif num2 == 2:
            print(num1 + "-")  # 执行减法运算
        elif num2 == 3:
            print(num1 + "*")  # 执行乘法运算
        elif num2 == 4:
            print(num1 + "/")  # 执行除法运算

        num3 = input("输入第二个数值")  # 获取用户输入的第二个数值
        num3 = int(num3 + num1)  # 将第二个数值与第一个数值相加
        print("结果为：", int(num3))  # 输出计算结果
        break

num()  # 调用函数


2.
把之前(从切片业开始)
的作业进行封装成函数（），然后进行调用运行，一道题一道题封装

H:\python笔记   kk.py


#四则运算
def bc(*四则):
   #加
    结果= 0
    for i in 四则:
        结果 += i
    print(f"加法结果为{结果}")

    # 减
    结果 = 四则[0]
    #len输出10 （1,10） =》1-9
    # 下标值从0开始-0-9
    for i in range(1, len(四则)):
        结果 -= 四则[i]
    print(f"减法结果为{结果}")


# 乘
结果 = 四则[0]
for i in range(1, len(四则)):
    结果 *= 四则[i]
print(f"乘法结果为{结果}")

# 除
结果 = 四则[0]
# len是什么意思=》长度，args10个，；len输出10 （1,10） =》1-9
# 下标值从0开始-0-9
for i in range(1, len(四则)):
    结果 /= 四则[i]
print(f"除法结果为{结果}")
bc(1, 2, 3, 4, 5, 6)
















