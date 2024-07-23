作业
1.一家公司有如下岗位（集合）：
    经理 ："曹操","刘备","孙权"
    技术 ："曹操","刘备","张飞","关羽"
要求：
1. 使用集合存储以上信息.
2. 是经理也是技术的都有谁?(集合交集)
3. 是经理也不是技术的都有谁?
4. 不是经理是技术的都有谁?
5. 身兼一职的都有谁?
6. 公司总共有多少人数?

a={"曹操","刘备","孙权"}
b={"曹操","刘备","张飞","关羽"}
print(f"是经理也是技术:{a&b}")
print(f"是经理不是技术{a-b}")
print(f"不是经理的技术{b-a}")
print(f"身兼一职{(b-a)|(a-b)}")
print(f"共有:{len(a|b)}人")

讲：
def func():
    a = {"曹操", "刘备", "孙权"}
    b = {"曹操", "刘备", "张飞", "关羽"}
    print(f"是经理也是技术的都有{a & b}")
    print(f"是经理也不是技术的都有{a - b}")
    print(f"是经理也不是技术的都有{b - a}")
    print(f"身兼一职的都有{(a | b) - (a & b)}")
    print(f"公司总共有{len(a | b)}")
func()

2、用户输入一个数字,判断(1~12)属于哪个季节
def 季节():
    a = "春"
    b = "夏"
    c = "秋"
    d = "冬"
    return a, b, c, d
def 月份():
    e = int(input("输入判断的月份:"))
    return e
def 判断():
    a, b, c, d = 季节()
    while True:
        e = 月份()
        if e > 12 or e < 1:
            print("请输入正确数字（1--12）")
        elif 3 <= e <= 5:
            print(f"当前季节为：{a}季")
            break
        elif 6 <= e <= 8:
            print(f"当前季节为：{b}季")
            break
        elif 9 <= e <= 11:
            print(f"当前季节为：{c}季")
            break
        else:
            print(f"当前季节为：{d}季")
            break
判断()

讲：
def func():
    user = int(input("请输入你的月份"))
    while 1:
        if 1 <= user <= 12:
            break
        user = int(input("请输入你的月份"))
    if 1 <= user <= 3:
        print("春季")
    elif 4 <= user <= 6:
        print("夏季")
    elif 7 <= user <= 9:
        print("秋季")
    else:
        print("冬季")
func()