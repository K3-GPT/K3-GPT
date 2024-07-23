函数作用域与名称空间 作业
1.创建一个函数func1,实现提示输入密码，创建一个密码全局变量password，创建另一个函数func2，实现当输入的密码=全局变量密码password就输出登录成功、

password = 456852
def ac():
    print("请输入密码")
    def bc():
        while True:
            b=int(input("密码："))
            if b == password:
                print("登录成功")
            else:
                print("密码错误,请重新输入")
    bc()
ac()

讲：
password = 24
def func1():
    a = int(input("输入密码"))  # 提示用户输入密码，并将其转换为整数保存到变量a中
    b = a + 12  # 将用户输入的密码加上12保存到变量b中
    return b  # 返回处理后的密码
def func2(b):
    if b == password:  # 检查处理后的密码是否与预设密码匹配
        print("登录成功")  # 如果匹配，打印"登录成功"
func2(func1())  # 调用func1获取处理后的密码，并将其传递给func2进行验证

2.在函数2创建一个局部变量user提示输入，然后输出user变量数值

def cc():
    global user
    user  = 125
    print(user)
cc()

3. 把昨天的四则运算改为匿名函数

def dc():  # 匿名四则计算
    加法 = lambda *四则运算: sum(四则运算)
    减法 = lambda *四则运算: 四则运算[0] - sum(四则运算[1:])
    # 从下标为0的数开始计算，依次剪到末尾
    乘法 = lambda *四则运算: 四则运算[0] if len(四则运算) == 1 else 四则运算[0] * 乘法(*四则运算[1:])
    '''
         # 流程
         1. 第一次调用：ec(1, 2, 3, 4, 5, 6) 参数长度大于1，执行1 * 乘法( 2, 3, 4, 5, 6)
         2. 第二次调用：ec(2, 3, 4, 5, 6)参数长度大于1，执行2 * 乘法( 3, 4, 5, 6)
         3. ....
         4. 第六次调用：ec(6)参数长度等于1，返回6

         #递归回溯：
         第六次返回结果 6 回到第五次，计算 5 * 6 = 30
         第五次返回结果 30 回到第四次，计算 4 * 30 = 120
         ......
         第二次返回结果 720 回到第一次，最终结果是 1 * 720 = 720
    '''
    除法 = lambda *args: args[0] if len(args) == 1 else args[0] / 除法(*args[1:])

    def ec(*四则运算):
        print(f"加法结果为 {加法(*四则运算)}")
        print(f"减法结果为 {减法(*四则运算)}")
        print(f"乘法结果为 {乘法(*四则运算)}")
        print(f"除法结果为 {除法(*四则运算)}")
    ec(1, 2, 3, 4, 5, 6)
dc()

讲：
password = 123456
def func1():
    # 实现提示输入密码
    global passwd       #外部可以调用
    passwd = int(input("输入密码"))
def func2():
    if passwd == password:
        print("登录成功")
    user = input("请输入用户名")
    print(user)     #外部不可调用

# 调用输出return值
func1()
func2()
print(f"输****: {passwd}")
