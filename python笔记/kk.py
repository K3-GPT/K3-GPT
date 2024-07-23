def  切片例子():
    a = "sdfsdfs"
    # dfsd
    print("输出dfsd")
    print(a[1:5])
    print(a[-6:-2])
    # sdf
    print("输出sdf")
    print(a[:3])
    print(a[3:6])
    print(a[-4:-1])
    print(a[-7:-4])
    # dfs
    print("输出dfs")
    print(a[1:4])
    print(a[4:7])
    print(a[-6:-3])
    print(a[-3:])
    print(a[-3:-8:-2])
    # sfds
    print("输出sfds")
    print(a[:7:2])
    print(a[:2:-1])
    # dsf
    print("输出dsf")
    print(a[1:6:2])
    print(a[-3:-6:-1])
    # dd
    print("输出dd")
    print(a[1:5:3])
    print(a[-3:-7:-3])
    # sfdsfds
    print("输出sfdsfds")
    print(a[::-1])
    # len
    print("输出整个列表长度")
    print(len(a))

def 列表例子():
    print("1.创建一个空列表li，在里面添加姓名，年龄，身高")
    li = []
    print(li)
    li = ["名字：kk", "年龄：18", "身高：2.3"]
    print(li)
    print(end="\n")

    print("2.在列表li中，身高前面插入出生日期，在身高后面插入家庭地址")
    li.insert(2, "出生日期：1949.10.1")
    li.insert(4, "中华人民共和国")
    print(li)
    print(end="\n")

    print("3.查询列表li是否有包含出生日期")
    print("出生日期：1949.10.1" in li)
    print(end="\n")
    print("4.把列表li中的出生日期和家庭地址删除")
    li.pop(2)
    li.pop(3)
    print(li)
    li.remove('身高：2.3')
    li.remove('年龄：18')
    li.remove('名字：kk')
    print(end="\n")


def  字符串方法例子():
    print("1. 下面字母输出全小写、全大写"
          "(1) hello word"   
             "(2)HELLO WORD")

    a = "hello world"
    print(a.upper())
    print(a.lower())
    print(end="\n")

    print("2. 按照要求进行输出")
    print('（1）"asw2ewwsdf":把所有里面的【w】改为【i】输出')
    print('（2）"123456789":以【5】字符为切割点，进行切分为2段')
    print('（3）"我好饿啊!!!!":把后面的【!】清除掉并查找里面的【饿】的字符')

    b = "asw2ewwsdf"
    print(b.replace("w", "i"))

    c = "123456789"
    print(c.split("5", 2))

    d = "我好饿啊!!!!"
    print(d.rstrip("!"))
    print(d.find("饿"))
    print(end="\n")

    print("3.把下面的字符串安装特定的格式化要求输出")
    print('（1）创建变量a，b。分别赋值"高"，"帅"。然后进行放到字符串里面进行输出：字符串输出例如[我又高又帅]')
    print('（2）使用format把Name和Age放到字符串进行输出。例如：【我今年26岁，我是梓良老师】')
    print('（3）创建heigh（身高）变量，赋值178.67123，分别用%s,%d,%.2f进行输出')

    e = "高"
    f = "帅"
    g = "我很%s" % e
    h = "也很%s" % f
    print(g + h)
    print("我不仅{}还{}".format("高", "帅"))

    print("我今年{0}岁，名字叫{1}".format(18, "kk"))

    high = 178.67123
    print("身高：%s" % high)
    print("身高：%d" % high)
    print("身高：%23.2f" % high)


def  离散类型例子():
    print('1.创建一个字典，分别添加{"tuple" : (1,2,3,4)}、{“list”:[1,2,3,4]}以及{“dict”:None},key自己定义')
    i = {"First": 1}
    i.update({"tuple": (1, 2, 3, 4)})
    i.update({"list": [1, 2, 3, 4]})
    i.update({"dict": None})
    print(i)
    print(end="\n")

    print('2. 根据上面的字典。分别删除{"tupe" : (1,2,3,4)}、{“list”:[1,2,3,4]}以及{“1”:None}')
    i.pop("tuple")
    i.pop("list")
    i.pop("dict")
    print(i)
    print(end="\n")

    print("3.创建一个集合A和一个集合B，分别输出并集、交集和差集")
    a = {"First", "Su", "kk", 12, 25, 66}
    b = {31, 85, 45, 244, 15, 785, 66, 25, True, False, "kk"}
    print("ab交集：", a & b)
    print("ab并集：", a | b)
    print("ab差集：", a - b)
    print(end="\n")

    print('4.创建一个字典{"1":2,"2":2,"3":2},把里面的value值全部改成None     用 遍历 添加')
    a = {"1": 2, "2": 2, "3": 2}
    for b in a:
        a[b] = None
    print(a)
    print(end="\n")

def  控制流程例子1():
    print("1.创建变量，从1到100进行输出，数值之间用【, 】分开")
    for a in range(0, 100):
        print(a, end="，")

    print("2.根据第一题进行改进，主要数值分别输出奇数、偶数、3 / 5 / 7的倍数、2和3的公共倍数")
    print("方法一：（奇数偶数）")
    for a in range(1, 101, 2):
        print(a, end="，")
    print(end="\n")
    for a in range(2, 101, 2):
        print(a, end="，")

    print("方法二：")
    for a in range(1, 101):
        if a % 2 != 0:
            print(a, end="，")
    print(end="\n")
    for a in range(1, 101):
        if a % 2 == 0:
            print(a, end="，")
        print(end="\n")

    print("3.1  输出2和3的公共倍数")
    for a in range(1, 101):
        if a % 2 == 0 and a % 3 == 0:
            print(a, end="，")

    print(end="\n")

    print("3.2  输出3     5     7的倍数")
    for a in range(1, 101):
        print(a * 3, end="，")
    print(end="\n")

    for a in range(1, 101):
        print(a * 5, end="，")
    print(end="\n")

    for a in range(1, 101):
        print(a * 7, end="，")
    print(end="\n")

    print("改：")
    for i in range(1, 101):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            print(i, end=" ")

    print(end="\n")

    print("4.根据第一题再进行改进，数值输出到80就停止输出")
    for a in range(1, 101):
        print(a, end="，")
        while a == 80:
            continue

def 控制流程例子2():
    print('5.创建一个字典    {"name": "屠龙刀", "price": 10000, "cid": 1001, "count": 1},     分别打印字典里面的key值和value值')
    a = {"name": "屠龙刀", "price": 10000, "cid": 1001, "count": 1}
    for i in a.items():
        print(f"key值:{i[0]}", end=" ")
        print(f"value值:{i[1]}")

    print(end="\n")
    print("6.打印倒立直角三角形：")
    print("* * * * *")
    print("* * * *")
    print("* * *")
    print("* *")
    print("*")
    print("展示：")
    for i in range(5, 0, -1):
        for j in range(1, i + 1):
            print("*", end=" ")
        print()

def   WhileTrue经典案例():
    while True:
        age_input = input("请输入用户年龄：")
        try:
            b = int(age_input)
            break  # 如果成功转换为整数，跳出循环
        except ValueError:
            print("请输入一个整数！")
