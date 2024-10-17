# Hadoop

## 文档遵循由上而下的顺序



# 下载软件和镜像

```
1.从 ftp://172.16.170.50/ 中的文件夹 VM已安装好的镜像中 下载 Centos_7.zip并解压到相关文件夹
2.打开VM （win10 用VM 15，win11 用 VM 16），找到解压后的VMX文件拖入软件。
账号和密码都为 root。

没有校园网就联系我，使用阿里云盘快传(新账号无法使用长期分享功能，后续跟新)
```

# 1.docker虚拟机使用方法

[docker虚拟机使用方法](https://docs.qq.com/doc/DZWhuYldPUXJORmRx)

```
#查看镜像  
docker images   
```

![image-20241016232657394](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241016232657394.png)

```
1.
下载docker仓库中的镜像
#格式：docker pull   镜像名    镜像名： 名称：标签
#注:本ISO的名称为: centos8  标签为:latest  且在VM运行后，可能会卡住，建议重开一个终端
docker pull   centos8:latest

2.
#运行容器后不退出
#-i    让容器的标准输入保持打开
# -t   让Docker分配一个终端并绑定在容器的标准输入上
docker run -it centos8:latest /bin/bash

3.
#查看所有容器，运行到此，就会这样：  docker ps #未启动的看不到 
docker ps -a 
```

![image-20241016233659603](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241016233659603.png)

```
4.
#现在试着推出 
exit
#想要再次进入容器，则需要先打开，后进入
docker start ac311ff7d7fb 
docker exec -it ac311ff7d7fb  /bin/bash    #实际使用发现  docker run -it centos8:latest /bin/bash  也可以
```

```
#5.
#假设现在有好几个容器，需要删除，则需要先exit退出，stop停止后rm，然后按上 根据 ID 删除不建议使用"删除所有容器"
#格式：docker   rm   容器ID
exit
docker ps -a 
docker stop ac311ff7d7fb
docker rm ac311ff7d7fb 			#此刻就把刚刚用的容器删掉了，就需要回到 2. 直到 4.
```

```
6.
#给容器改名  
#                    自定义
#方法1
docker run -itd --name=kk centos8:latest /bin/bash
docker exec -it kk  /bin/bash
```

![image-20241017000653315](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017000653315.png)

```
#改好名后，就可以直接用名字进入，和4.中进入一样道理
#但此刻容器名仍是ID，所以可以用方法2 注意:运行方法1后，不能直接运行方法2
#方法2  
docker run -itd  --name=kk  --hostname=hadoop1 centos8:latest /bin/bash
docker exec -it kk  /bin/bash
```

![image-20241017002513757](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017002513757.png)



# 2.linux写文件的几种方法

[linux写文件的几种方法](https://docs.qq.com/doc/DZVJydFREWlhld3dD)

```
#文本编辑
#1.  vim  自动创建文件
#假设要在/opt中写一个1.txt的文件，里面写《静夜诗》  
cd /opt
vim 1.txt      #注:运行后，需要按任意键开始插入
《静夜诗》 

#退出的两种方式：
ESC键-->:wq  保存
ESC键-->:q!  不保存

#2.  nano  
cd /opt
nano 2.txt 
《静夜诗》 
ctrl键+x-->y

#3. echo 重定向输出
#格式: echo  'ok'  > 文件名
#创建新文件 2.txt 并写入123
echo  '123'  >  2.txt

#在2.txt 最后追加写入  456
echo '789'  >>  2.txt

#4.cat   查看
cat 1.txt

#如果用 cat > 2.txt 重定向输入，则是覆盖型输入,输入完成后，enter-->ctrl+d
```



# 3.搭建单机模式Hadoop-----首次开工

[搭建单机模式Hadoop-----首次开工](https://docs.qq.com/doc/DZUFMV1J5WUdHbnhZ)

```
#因为导入的镜像中就已经自带Centos8 的镜像，所以无需下载
#1.
#首先进入先前已经改过名字的容器
docker exec -it kk /bin/bash

#2.
#修改软件安装源		(注：因需要访问 vault.centos.org 的 CentOS 历史存档源,所以需要 联网)
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
yum makecache
```

![image-20241017110943633](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017110943633.png)

```
#3.
#安装 OpenJDK 8 和 SSH 服务		(软件包都需要从 yum 源下载安装，也需要联网)
yum install -y  java-1.8.0-openjdk-devel    openssh-clients     openssh-server
```

![image-20241017111034151](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017111034151.png)

```
#4.
#启用 SSH 服务  记得先exit
systemctl enable sshd && systemctl start sshd

#退出，停止，然后保存为镜像(后续则无需再执行3. 4. = 无需联网)
docker stop kk

#格式：docker commit   容器名    镜像名
docker commit kk java_ssh
```

![image-20241017113150310](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017113150310.png)

```
#5.
#Hadoop 安装
#创建 Hadoop 单机容器
docker run -d --name=hadoop_1 --privileged java_ssh /usr/sbin/init  

#6.
#下载 Hadoop
#校园网用户直接使用FTP
wget  ftp://172.16.170.50/hadoop-3.1.4.tar.gz
```

## #其他用户从我的云盘下载压缩包到实体机，然后通过共享文件夹传入到虚拟机        (目前问题为解决 请直接跳转到 8.)

## 一，打开虚拟机的文件共享

![image-20241017114548005](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017114548005.png)



## 二，在实体机中，方便寻找的位置创建一个文件夹

![image-20241017114409135](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017114409135.png)



## 三，设置为 共享文件夹

![image-20241017114637764](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017114637764.png)



## 四，回到VM 设置路径，名称自定义(不建议用中文)

![image-20241017114746191](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017114746191.png![image-20241017114853254](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017114853254.png)





## 五，到终端进行路径挂载（重启后重新挂载）

```
#挂载
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/gongxinag -o allow_other
                                       #挂载点
#访问               tab键
ls /mnt/gongxinag/共享文件夹
```

![image-20241017125754341](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017125754341.png)



## 六，cp主机的文件到容器中

```
#在容器中先创建一个解压路径
mkdir /usr/local/hadoop
exit

#CP
#格式： docker cp                       <主机文件路径> <容器名>:<容器内路径>
docker cp /mnt/gongxiang/共享文件夹/hadoop-3.1.4.tar.gz kk:/
```





```
#7.
#解压文件
docker exec -it kk /bin/bash
tar -xzf hadoop-3.1.4.tar.gz
mv hadoop-3.1.4 /usr/local/hadoop  

echo 'export HADOOP_HOME=/usr/local/hadoop' >> /etc/bashrc 
echo 'export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin' >> /etc/bashrc 
source  /etc/bashrc

#运行后，如果运行 echo $HADOOP_HOME 的结果是 /usr/local/hadoop 则成功
```



```
#8.
#解压
tar -zxvf hadoop-3.1.4.tar.gz
#移动到常用路径
mv    hadoop-3.1.4     /usr/local/hadoop     
#配置环境变量
echo 'export HADOOP_HOME=/usr/local/hadoop' >> /etc/bashrc 
echo 'export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin' >> /etc/bashrc 
exit
docker exec -it kk /bin/bash
echo 'export JAVA_HOME=/usr' >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh 
echo 'export HADOOP_HOME=/usr/local/hadoop' >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh

#配置后，如果运行 后的内容如下，则正常 
hadoop
```

![image-20241017171800226](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017171800226.png)

```
hadoop version
```

![image-20241017171847963](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017171847963.png)

```
#运行 PI
hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.4.jar     
```



# 4.搭建单机模式Hadoop-----认识环境变量

[搭建单机模式Hadoop-----认识环境变量](https://docs.qq.com/doc/DZUNIdVViWGNMSGZr)









