例：
def 装饰器(func):
    def inner(*args, **kwargs):
        print("正在计算中")
        func(*args, **kwargs)
        print("计算结束")
    return inner
@装饰器
def add(number1, number2, number3):
    print(f"结果为{number1+number2+number3}")

@装饰器
def sub(number1, number2):
    print(f"结果{number1-number2}")

@装饰器
def info():
    print(f"xxxxxxx")

@装饰器
def Dict(**kwargs):
    print(f"Dict:{kwargs}")

add(1, 2, 3)
sub(1, 2)
info()
Dict(a=1)
