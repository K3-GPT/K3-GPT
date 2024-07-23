'''
1.创建一个空列表li，在里面添加姓名，年龄，身高

list = []
print(list)
list = ["名字：kk","年龄：18","身高：2.3"]
print(list)

2.在列表li中，身高前面插入出生日期，在身高后面插入家庭地址

list.insert(2,"出生日期：1949.10.1")
list.insert(4,"中华人民共和国")
print(list)

3.查询列表li是否有包含出生日期

print("出生日期：1949.10.1" in list)

4.把列表li中的出生日期和家庭地址删除

list.pop(2)
list.pop(3)
print(list)
list.remove('身高：2.3')
list.remove('年龄：18')
list.remove('名字：kk')

5.清空列表li的数值，清空后删除列表

del list
print(list)

'''

#1
list = []
print(list)
list = ["名字：kk","年龄：18","身高：2.3"]
print(list)
#2
list.insert(2,"出生日期：1949.10.1")
list.insert(4,"中华人民共和国")
print(list)
#3
print("出生日期：1949.10.1" in list)
#4
list.pop(2)
list.pop(3)
print(list)
list.remove('身高：2.3')
list.remove('年龄：18')
list.remove('名字：kk')
#5
del list
print(list)