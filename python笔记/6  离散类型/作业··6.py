1.创建一个字典，分别添加{"tuple" : (1,2,3,4)}、{“list”:[1,2,3,4]}以及{“dict”:None},key自己定义
a={"First":1}
a.update ({"tuple" : (1,2,3,4)})
a.update({"list":[1,2,3,4]})
a.update({"dict":None})
print(a)

2.根据上面的字典。分别删除{"tupe" : (1,2,3,4)}、{“list”:[1,2,3,4]}以及{“1”:None}，
a.pop("tuple")
a.pop("list")
a.pop("dict")
print(a)

3.创建一个集合A和一个集合B，分别输出并集、交集和差集
a ={"First","Su","kk",12,25,66}
b={31,85,45,244,15,785,66,25,True,False,"kk"}
print("ab交集：",a&b)
print("ab并集：",a|b)
print("ab差集：",a-b)

4.创建一个字典{"1":2,"2":2,"3":2},把里面的value值全部改成None     用 遍历 添加
a = {"1": 2, "2": 2, "3": 2}
for b in a:
    a[b] = None
print(a)