# 第三章

http://172.16.198.15:9936/z03.html

# 一. 登录/退出

```
#用户名输入后，passwd输入不会显示

#n分钟后 关机
shutdown -h n

#n分钟后 重启
shutdown -h n

#取消
shutdown -c
```



# 二.修改密码

```
passwd
```



# 三. 目录命令

## 1 pwd      显示

## 2 cd          进入

## 3 mkdir   创建

### 		mkdir -p 多级创建

## 4 rmdir    删除

### 		rmdir -p 递归删除



## ①. P27 作业

```
#1
cd /bin
#2
cd /usr/tmp
#3
cd /usr/local/games
#4
cd /home/alice/books
#5
cd /home/alice/books/文学
```

![image-20241030193039249](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241030193039249.png)



## ②. P30 作业

```
#5--2
cd ../../../../usr/tmp
#2--5
cd ../../home/alice/books/文学
#5--4
cd ..
#4--5
cd /文学
#3--1
cd ../../../../bin
#1--3
cd ../usr/local/games
```

![image-20241030193101031](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241030193101031.png)



## ②. P35 随堂测

```
B    D
```

![image-20241030193159544](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241030193159544.png)



## ②. P39 作业

```
mkdir -p /home/alice/books/文学
mkdir -p /home/alice/books/小说
mkdir -p /home/alice/books/艺术
mkdir -p /home/alice/books/传记
mkdir -p /home/alice/tool
mkdir -p /home/alice/picutre
mkdir -p /home/bob
mkdir -p /home/eve
```

![image-20241030193506727](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241030193506727.png)



# 四.文件命令

## 1 touch								   创建

## 2 ls 									  	显示

### 		ls -a 所有

### 		ls -l  清单

### 		ls -r 反序

### 		ls -t 时间正序

### 		ls -h 文件大小



## 3 cp 									 	复制

### 		cp [操作] (源)(目标)

```
# 1.txt复制到  /home 改名2.txt
cp 1.txt /home/2.txt
```

### 		cp -r /a /b 复制递归文件夹4



## 4 rm										 删除

### 		rm [操作] (目标)

### 		rm -f	强制删除



## 5 mv										 移动

### 		mv (源) (目标)

```
# 3.txt移动到/home 改名4.txt
mv 3.txt /home/4.txt
```



## 6 ln 										  链接（快捷方式）

### 		ln [操作] (目标) (名字)

```
#创建软连接在/home 名为slinkdir
ln -s /home / slinkdir
```

## 7 cat     显示所有

```
#显示行号的显示所有
cat -n /etc/passwd
```

### 		head    头部

```
#显示前15行(默认前10行)
head -15 /etc/passwd
```

### 		tail		尾部

```
#显示后15行(默认后10行)
tail -15 /etc/passwd
```

### 		more	分页显示

```
#只能enter下一页
more /etc/ssh/sshd_config
```

### 		less   可翻页显示

```
#显示行号的显示，用↑↓翻页，q退出
less -N /etc/ssh/sshd_config
```



## 8 wc 										 统计

### 		wc -l	行数

### 		wc -c	字节数(大小)

### 		wc -w	字数

```
wc -lcw /etc/passwd
```

## ①P47 随堂测

```
C C
```

![image-20241030194730248](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241030194730248.png)

## ②P53 随堂测

```
#1
mkdir /tmp/dir1
mkdir /tmp/dir2

#2
touch -p /tmp/dir1/file1
touch -p /tmp/dir1/file2
touch -p /tmp/dir1/file3

#3
mkdir -p /tmp/dir2/zml1
mkdir -p /tmp/dir2/zml2
mkdir -p /tmp/dir2/zml3

#4
cp /tmp/dir1/file1 /tmp/dir2/zml2/fileback1

#5
mv /tmp/dir1/file2 /tmp/dir2/zml1/fileback2

#6
cp -a /tmp/dir2 /tmp/dir1

#7
ln -s /tmp/dir1/file3 linktofile3

#8
rm -rf /tmp/dir1 /tmp/dir2
```

![image-20241030201525527](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241030201525527.png)



## ③P60 随堂测

```
#1
mkdir /tmp/read

#2
cp /etc/ssh/sshd_config /tmp/read/testfile

#3
cat /tmp/read/testfile

#4
head -9 /tmp/read/testfile
#5
tail -7 /tmp/read/testfile
#6
more /tmp/read/testfile
#7
less /tmp/read/testfile
#8
rm -rf /tmp/read/testfile
#9
rmdir /tmp/read
```



![image-20241030230210764](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241030230210764.png)



# 五.通配符

## *	匹配0个/任意个字符

## ?	任意一个(有且仅一个)字符

```
ls -l	a*		以a开头
ls -l	*a		以a结尾		
ls -l	*a*		包含a的
ls -l	？a*		第 2 个字符为a
ls -l	？？a*    第 3 个字符为a
```



## ①P64随堂测

```
@1
ls -a /bin ab*
#2
ls -a /bin *c
#3
ls -a /bin *bug*
#4
ls -a /bin ???????m*
#5
ls -l /bin ?????s????
#6
ls -l /bin ?a??b?*
```

![image-20241030234911937](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241030234911937.png)



# 六. 文件压缩

## gzip  压缩/解压  .gz

## zip/unzip 压缩/解压 .zip

## tar  多文件打包压缩





















































