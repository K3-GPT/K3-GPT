1.字符编码
1.1  ASCII
一共127字母和一些数字,但是只能识别英文的字母
1.2  GBK
GBK，就是基于ASCII编码拓展处理，中文字符编码，只拓展了中文，可以看作中英文翻译
1.3  Unicode
Unicode(万国码)是把几乎通用的语言统一到一套字符编码上面去，基本实现全球通用语言
1.4  UTF-8(记住)
utf-8就是Unicode的瘦身版，是可变字节，
拓展：
python3.x就是默认字符编为utf-8，所有可以用中文起变量名

2.  散列类型
即无序序列，作用和有序序列是一样，都是储存数据
特征：就是没有顺序，没有下标值，没切片
2.1  有序序列：str，list，tuple
2.2  无序序列：set，dict

3.字典   dict
定义：字典和列表的功能差不多，都是储存各种各样的数据，  是和列表不一样，没有下标值

格式：字典名 = {key1: value1, key2: value2}
特征：键值对 ==》{key: value}

3.1  key值——键值： （唯一不变且不可重复）
固定数据类型：number（int，float），str，bool，tuple -》数值不能修改
标值一样的功能，识别位置
注：key值可操控，比下标值更灵活

3.2  value值——数值： 全部类型

拓展：
True作为key相当于数学运算，变成1，相同的key 会覆盖value，
key值的对比是  数学对比  不是  类型对比(重点)   数学角度  1.0 = 1

例：
3.3.1
{1: '1', (1,): 1, '1': '1'}
1，True，1.0三者相同
后面相同相同的key值不运行,只保留第一个

a ={1:"1", (1,):1, True: "1", 1.0: "1", "1":"1", 1:"1"}
print(a)
结果：
{1: '1', (1,): 1, '1': '1'}

3.3.2
True会数学运算，会变成数值int 1
a[True] => a[1]
a ={1:"1", (1,):1}
print(a[True])  #

4.字典方法:(增删改查)
4.1   增加/修改：
①输入的字典为  相同  key值，只会修改value值，也就是字面上的更新value
②输入的字典为  不同  key值，就是在字典最右边加上字典数据

4.1.1       update( )
格式：dict.update({key:value})       /     dict.update(dict)
          dict[key] = value （不推荐：若key值为 int，那么这写法和有序序列分不清）

例：
a = {"name": "kk", "age": 16}
a.update({"age": 18})
print(a)
a.update({"height": 170})
print(a)

a = {"name": "kk", "age": 16}
a["age"] = 18
print(a)
a["height"] = 170
print(a)

结果：
{'name': 'kk', 'age': 18}
{'name': 'kk', 'age': 18, 'height': 170}

4.1.2  setdefault( )   安全增加
dict.setdefault( )
==》setdefault= set（集合） + default（默认值）
默认值：None（空值数据类型），不写=默认值None
①有相同key值，没有任何改变
②没有相同key值，会增加

格式：
dict.setdefault(key,default)

例：
a = {1: 1, 2: 2, 3: 3}
a.setdefault(4)
print(a)
a.setdefault(5,5)
print(a)
a.setdefault(5,"5")
print(a)
print(type(a[5]))
结果：
{1: 1, 2: 2, 3: 3, 4: None}
{1: 1, 2: 2, 3: 3, 4: None, 5: 5}
{1: 1, 2: 2, 3: 3, 4: None, 5: 5}
<class 'int'>

4.1.3 add()  添加
格式：
dict.add()
例：
a = {1,3,4,5}
a.add(254)      # 随机添加位置(顺序添加仅方便阅读）
print(a)
结果：
{1, 3, 4, 5, 254}


4.2   删除：
4.2.1   pop()        列表pop原理差不多
格式：
dict.pop(key)
根据key值进行删除value
当value值没有，key也会消失，同存亡
例：
a = {"1": 1, "2": 2}
a.pop("1")
print(a)
结果：
{'2': 2}

4.2.2        popitem()      删除最后一个       随机删除==》无序序列
格式：
dict.popitem()
例：
a = {"1":1, "2": 2,True:45,"KEYI":"buyao",False:"asd"}
a.popitem()
print(a)

4.2.3
del     和有序序列一样
del 字典      (物理删除)
del 字典[key]    删除一个数值 ，没切片没有多个同时删除

4.2.4      清空数据
格式：
dict.clear()

4.2.5  remove( ), discard() 删除
①remove：不存在就报错           ==>  用于确定数值是否删除
②discard：不存在就是不报错    ==>  常用
格式：dict.remove(数值)， dict.discard(数值)

例：
a = {1,3,5,7,9}
a.remove(1) # 如果你
print(a)
a.discard(1)
print(a)

4.3     查
4.3.1        报错法
格式:
dict[key]

4.3.2      get(key,default)  默认值法
dict.get(key,default=None) default 就是默认值的意思

4.3.2.1     当key值存在
①如果没设置的default值，输出value值
②如果设置了default值，输出value值

4.3.3.2     当key值不存在
①如果没有设置default值，输出None值
②如果设置了default值，输出default值

注：
get查询数值
①存在：输出  value
②不存在：输出  None
③若字典有一些数值是None，可修改为特定值

例：
a = {"1": 65, "2": 24}
print(a.get("1"))             #①
print(a.get("3"))             #②
print(a.get("3",False))     #③

5.字典常用方法
5.1  items()    获取全部
获取字典 全部的key值和value值，而且以元组的形式放到列表里面展示
格式:
dict.items()
例：
用元组括起key和value，保证key，value不会被任何数值污染
a = {"1": 11, "2": 22,3:33,"si":44}
print(a.items())
结果：
dict_items([('1', 11), ('2', 22), (3, 33), ('si', 44)])

5.2          获取key/value
values() ，keys()
定义：
values(): 获取字典全部value值，输出 list
keys(): 获取字典全部的key值，输出 list

例：
a = {"1": 123, "2": 456,"san":789,6.3:987}
print(a.values())
print(a.keys())
结果：
dict_values([123, 456, 789, 987])
dict_keys(['1', '2', 'san', 6.3])


5.3  fromkeys( )     创建或者批量创建相同的数值字典
格式：
fromkeys(keys, default=None)
不设置default值，就：None
注：fromkeys本身是没有任何添加功能
例：
# 空字典
a = {}
b = (1,2,3,4,5)
a = a.fromkeys(b)
print("1:（）",a)

a = a.fromkeys(b,1)
print("2:",a)

a = {}
b = [1,3,5,7,9]
c = [2,4,6,8,10]
a = a.fromkeys(b,456)
d=a.fromkeys(c,789)
print("1:456",a)
print("2:789",d)
结果：
1:（） {1: None, 2: None, 3: None, 4: None, 5: None}
2: {1: 1, 2: 1, 3: 1, 4: 1, 5: 1}
1:456 {1: 456, 3: 456, 5: 456, 7: 456, 9: 456}
2:789 {2: 789, 4: 789, 6: 789, 8: 789, 10: 789}


6.  集合
没有index值，也没key值；只能用in或者not in 判断在不在
数值唯一不变且不可重复的
数值固定：str，number，bool，tuple（元组）
格式：
a = {x,x,x,x}
拓展：就是key值一般是要转换为集合的，来保证key的正确性

例：
①去重
a = [1,2,3,1,2,3]
a = set(a)
print(a)
print(type(a))
结果：
{1, 2, 3}
<class 'set'>
如果相同的数值会去掉，通常用在去重（查重，去掉重复）

② 定义空集合
a = set()
print(a)
print(type(a))
结果：
set()
<class 'set'>


7.3  交、并、差集
&   (交集)       |  两集合相同值          |
|    (并集)       |   两集合全部值          |
-    (差集)       | 左边有右边没有的值 |
例：
a = {1,2,3,4,5}
b = {3,4,5,6,7}
print(a & b)
print(a | b)
print(a - b)
print(b - a)
结果：
{3, 4, 5}
{1, 2, 3, 4, 5, 6, 7}
{1, 2}
{6, 7}

