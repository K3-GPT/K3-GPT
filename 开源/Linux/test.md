# 1.

1.在家目录新建自己姓名拼音+2999的子目录(如:zhangsan2999),进入该目录并创建两个子目录，目录名分别为dir11和dir22

```
cd ~
mkdir -p yuankailun2999
cd yuankailun2999
mkdir dir11 
mkdir dir22
```

2.进入dir11目录,在dir11中创建一个空文件,文件名为自己姓名拼音(如:zbangsam)，并使用列表形式显示dir11下所有文件的详细信息

```
cd dir11
touch yuankailun
ls -l
```

3.将该文件移动到dir22目录下并更名为backfiler

```
mv yuankailun ../dir22/backfiler
cd ../dir22
ls -l
```

4.将/bin/目录下文件名第3个字符为a且文件名长度为4个字符的所有文件，复制到 dir11目录下，并使用列表形式显示 dir11 下所有文件的详细信息。

```
cd ../dir11
find /bin/  -name "??a?" -exec cp {} ./ \;
ls -l ./
```

5.将/bin/目录下文件名以a开头且以e结束的所有文件复制到dir22目录下，并使用列表形式显示dir22下所有文件的详细信息

```
find /bin/  -name "a*e" -exec cp {} ../dir22/ \;
ls -l ../dir22
```

6.将/etc/passwd 文件复制到 dir11目录下，并改名为pwpw2023

```
cd /dir11
cp /etc/passwd ./pwpw2023
```

7.显示该文件的前9行。

```
head -n 9 ./pwpw2023
```

8.进入 dir22目录，创建文件pwpw2024的软链接文件，取名为thelink，然后使用列表形式显示dir22下所有文件的详细信息

```
cd dir22
ln -s pwpw2024 thelink
ls -l
```

9.将文件 pwpw2024 压缩为 pwpw.zip 文件，然后解压缩到 dir11 目录

```
zip pwpw.zip pwpw2024
unzip pwpw.zip -d /dir11
```

10.退出 dir22 目录，然后将 dir22 目录下的所有文件打包并压缩，取名为dir2.tar.gz

```
cd ..
tar -czf dir2.tar.gz dir22
ls -l dir2.tar.gz
```

11.新建目录 dir33，将 dir2.tar.gz 解压缩并还原到目录 dir33 下

```
mkdir dir33
tar -xzf dir2.tar.gz -C dir33
ls -l dir33
```

12.不询问直接删除 dir11、dir22和 dir33 这三个目录

```
rm -rf dir11 dir22 dir33
```

# 2.

进入/bin/目录，使用find命令进行如下操作

```
cd /bin
```

13.查找所有文件名以 ab开头的文件

```
find /bin -name "ab*"
```

14.查找文件名长度为6的所有文件

```
find /bin/  -name '??????'
```

15.查找 size 大于 50k 的文件

```
find /bin/  -size +50k
```

16.查找所有文件名不包含a和b的文件

```
find /bin/  ! -name '*a*' ! -name '*b*'
```

# 3.

使用 grep,命令，对文件“a1.txt”进行如下操作:

17.显示所有语文教师的行数据

```
grep "语文教师" a1.txt
```

18.显示所有姓江的老师的行数据

```
grep "江" a1.txt
```

19.显示编号为20-39 的行数据

```
grep -n “[50-59]" a1.txt
```

20.显示属地不是西充的行数据

```
grep -nnot "市直"  a1.txt
```

21.显示电话号码以18开头的行数据

```
grep -n "电话号码" -a '^18" a1.txt
```

22.显示电话号码结尾为偶数的行数据

```
grep -n "电话号码" -a '[02468]$' a1.txt
```

23.新建一个用户组 thecolor，新建一个用户 red0l，用户所属用户组为thecolor，并为该用户设置密码。

```
groupadd thecolor
useradd -m -g thecolor red0l
passwd red0l
```

24.使用默认参数新建red02用户并设置密码,将red02添加到 thecolor组中

```
useradd red02
passwd red02
gpasswd -a red02 thecolor
```

25.在/tmp目录下新建子目录a0001，将目录所属用户改为red02，将目录所属用户组改为 thecolor

```
mkdir /tmp/a0001
chown red02:thecolor /tmp/a0001
```

26.在/tmp,目录下新建普通文件a0002，修改该文件权限，要求所属用户及用户组权限为读、写、执行，其他用户为只读权限（用二进制方式）

```
touch /tmp/a0002
chmod 774 /tmp/a0002
```

