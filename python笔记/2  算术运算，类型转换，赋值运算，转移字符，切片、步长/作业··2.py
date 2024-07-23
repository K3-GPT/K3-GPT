'''
1.使用运算符代码计算一下式子：
214 + 265   341-125   264 × 356   214 ÷ 42  74² ÷ 23
算出5421÷564的整数商和余数

2.创建字符串为      小明说：“ 天气真热，去买西瓜吃！"   ，按照下面进行输出：
小明说："天气真热，去买西瓜吃！"

3.创建字符串为     小明说：\n“ 天气真热，\t去买西瓜吃！"     ，输出结果：

小明说：\n“ 天气真热，\t去买西瓜吃！"  注意：\n和\t要输出

4.字符串：i = “sdfsdfs”, 按照下面提示输出

# 请输出dfsd

# 请输出sdf

#请输出dfs

#请输出sfds

#请输出dsf

#请输出dd

#请输出sfdsfds

#请输出字符串a的字符串长度
'''
#第一题：
a = 214;b =265
print(a+b)
c = 214;c+=265
print(c)

e = 341;f = 125
print(e-f)
g = 341;g -= 125
print(g)

h = 264;i = 356
print(h*i)
j = 264;j *= 356
print(j)

k = 214;l = 42
print(k/l)
m = 214;m /= 42
print(m)

n = 74**2;o = 23
print(n/o)
p =74**2;p /= 23
print(p)

q = 5421;q //= 564
print(q)
r = 5421;r %= 564
print(r)
#第二题
a = r'小明说："天气真热，去买西瓜吃！"'
print(a)
#第三题
b = '小明说：\\n“ 天气真热，\\t去买西瓜吃！"'
print(b)
#第四题
a = "sdfsdfs"
#dfsd
print(a[1:5])
print(a[-6:-2])
# sdf
print(a[:3])
print(a[3:6])
print(a[-4:-1])
print(a[-7:-4])
#dfs
print(a[1:4])
print(a[4:7])
print(a[-6:-3])
print(a[-3:])
print(a[-3:-8:-2])
#sfds
print(a[:7:2])
print(a[:2:-1])
#dsf
print(a[1:6:2])
print(a[-3:-6:-1])
#dd
print(a[1:5:3])
print(a[-3:-7:-3])
#sfdsfds
print(a[::-1])
#len
print(len(a))