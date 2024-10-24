

# Hadoop

## 文档遵循由上而下的顺序



# 下载软件和镜像

```
1.从 ftp://172.16.170.50/ 中的文件夹 VM已安装好的镜像中 下载 Centos_7.zip并解压到相关文件夹
2.打开VM （win10 用VM 15，win11 用 VM 16），找到解压后的VMX文件拖入软件。
账号和密码都为 root。

没有校园网就联系我，使用阿里云盘快传(新账号无法使用长期分享功能，后续跟新)
```

# 一.docker虚拟机使用方法

[docker虚拟机使用方法](https://docs.qq.com/doc/DZWhuYldPUXJORmRx)

```
#查看镜像  
docker images   
```

![image-20241016232657394](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241016232657394.png)

## #1. 下载docker仓库中的镜像

```
#格式：docker pull   镜像名    镜像名： 名称：标签
#注:本ISO的名称为: centos8  标签为:latest  且在VM运行后，可能会卡住，建议重开一个终端
docker pull   centos8:latest
```



## #2. 运行容器

```
#运行容器后不退出
#-i    让容器的标准输入保持打开
# -t   让Docker分配一个终端并绑定在容器的标准输入上
docker run -it centos8:latest /bin/bash
```



## #3. 查看容器

```
#查看所有容器，运行到此，就会这样：  docker ps #未启动的看不到 
docker ps -a 
```

![image-20241016233659603](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241016233659603.png)



## #4. 退出与重进

```
exit
#如果关闭了容器，则需要先打开，后进入
docker start ac311ff7d7fb 
docker exec -it ac311ff7d7fb  /bin/bash  
```



## #5. 停止、删除容器

```
#假设现在有好几个容器，需要删除，则需要先exit退出，stop停止后rm，然后根据 ID 删除。不建议使用"删除所有容器"
#格式：docker   rm   容器ID
exit
docker ps -a 
docker stop ac311ff7d7fb
docker rm ac311ff7d7fb 			#此刻就把刚刚用的容器删掉了，就需要回到 2. 直到 4.
```



## #6. 给容器改名 (以后启动就不需再输 ID)

```
#方法1   推荐使用方法2
#                 自定义      版本           地址
docker run -itd --name=kk centos8:latest /bin/bash
docker exec -it kk  /bin/bash
#改好名后，就可以直接用名字进入，和4.中进入一样道理
```

![image-20241017000653315](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017000653315.png)

```
#但此刻,容器名仍是ID，所以可以用方法2 
#注意:运行方法1后，不能直接运行方法2,因为已经给刚刚的容器命名，需要删除后重建

#方法2  
docker run -itd  --name=kk  --hostname=hadoop1 centos8:latest /bin/bash
docker exec -it kk  /bin/bash
```

![image-20241017002513757](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017002513757.png)



## #7. IP （这个没看懂，跳过）

```
#查看IP 
ip  address
#如果没有
yum  install  initscripts  -y
```





# 二.linux写文件的几种方法

[linux写文件的几种方法](https://docs.qq.com/doc/DZVJydFREWlhld3dD)

## #文本编辑

## #1.  vim  自动创建文件

```
#假设要在/opt中写一个1.txt的文件，里面写《静夜诗》  
cd /opt
vim 1.txt      #注:运行后，需要按任意键开始插入
《静夜诗》 

#退出的两种方式：
ESC键-->:wq  保存
ESC键-->:q!  不保存
```



## #2.  nano  

```
cd /opt
nano 2.txt 
《静夜诗》 
ctrl键+x-->y
```



## #3.  echo 重定向输出

```
#格式: echo  'ok'  > 文件名
#创建新文件 2.txt 并写入123
echo  '123'  >  2.txt

#在2.txt 最后追加写入  456
echo '789'  >>  2.txt

#4.cat   查看
cat 1.txt

#如果用 cat > 2.txt 重定向输入，则是覆盖型输入,输入完成后，enter-->ctrl+d
```



# 三.搭建单机模式Hadoop-----首次开工

[搭建单机模式Hadoop-----首次开工](https://docs.qq.com/doc/DZUFMV1J5WUdHbnhZ)

## #1. 进入容器

```
#因为导入的镜像中就已经自带Centos8 的镜像，所以无需下载
#首先进入先前已经改过名字的容器
docker exec -it kk /bin/bash
```



## #2. 修改软件安装源(在容器中)

```
#注：因需要访问 vault.centos.org 的 CentOS 历史存档源,所以 需要 联网
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
yum makecache
```

![image-20241017110943633](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017110943633.png)



## #3. 安装 OpenJDK 8 和 SSH 服务(在容器中)

```
#软件包都需要从 yum 源下载安装，需要 联网
yum install -y  java-1.8.0-openjdk-devel    openssh-clients     openssh-server
```

![image-20241017111034151](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017111034151.png)



## #4. 启用 SSH 服务 

```
exit
systemctl enable sshd && systemctl start sshd

#退出，停止，然后保存为镜像(后续则无需再执行#3. #4. = 无需联网)
docker stop kk

#格式：docker commit   容器名    镜像名
docker commit kk java_ssh
```

![image-20241017113150310](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017113150310.png)



## #5. Hadoop 安装

```
#创建 Hadoop 单机容器
docker run -d --name=hadoop_1 --privileged java_ssh /usr/sbin/init  
```



## #6. 下载 Hadoop

```
#校园网用户直接使用FTP
wget  ftp://172.16.170.50/hadoop-3.1.4.tar.gz
```



## #7. 非校园网用户下载方式 (CP法)

#其他用户从我的云盘下载压缩包到实体机，然后通过共享文件夹传入到虚拟机        (用校园网FTP的同学可直接跳转到 四.)

### ① 打开虚拟机的文件共享

![image-20241017114548005](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017114548005.png)



### ② 在实体机中，方便寻找的位置创建一个文件夹

![image-20241017114409135](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017114409135.png)



### ③ 设置为 共享文件夹

![image-20241017114637764](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241017114637764.png)



### ④ 回到VM 设置路径，名称自定义(不建议用中文)

![image-20241019010831385](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241019010831385.png)





### ⑤ 到终端进行路径挂载（重启后可能需要重新挂载）

```
#挂载
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs/ -o allow_other
                                       #挂载点
#如果报错        
#  fuse: mountpoint is not empty
#  fuse: if you are sure this is safe, use the 'nonempty' mount option
sudo umount /mnt/hgfs/                                      

#访问挂载点有没有 hadoop-3.1.4.tar.gz 文件               tab键
ls /mnt/hgfs/Folder/
```

![image-20241019011042144](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241019011042144.png)



### ⑥ CP 主机的文件

```
#建议先CP到 Linux 中的 / 
ls /mnt/hgfs/Folder
cp /mnt/hgfs/Folder/hadoop-3.1.4.tar.gz /
ls /mnt/hgfs/Folder
```

![image-20241019011121826](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241019011121826.png)

```
#再 docker cp 到容器里
#格式： docker cp             <主机文件路径> <容器名>:<容器内路径>
docker cp /mnt/hgfs/Folder/hadoop-3.1.4.tar.gz kk:/
```

![image-20241019011938807](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241019011938807.png)



```
#进入容器开始解压，在此之前别忘了先打开
docker start kk
docker exec -it kk /bin/bash
ls 

#如果 ls 有 hadoop-3.1.4.tar.gz 文件，就成功了
```

![image-20241019012334021](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241019012334021.png)



### ⑦ 解压   (在容器中)

```
tar -zxvf hadoop-3.1.4.tar.gz
#移动到常用路径
mv    hadoop-3.1.4     /usr/local/hadoop     
#配置环境变量  这一段要一步一步来
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
hadoop jar /usr/local/hadoop/share/hadoop/mapreduce/hadoop-mapreduce-examples-3.1.4.jar pi 500 500        
```



# 四.搭建单机模式Hadoop-----认识环境变量

[搭建单机模式Hadoop-----认识环境变量](https://docs.qq.com/doc/DZUNIdVViWGNMSGZr)

## #1.安装 which工具

```
#在容器中，安装一个工具 which
yum install  which  -y

#查看容器位置
which  hadoop
#因为在 ⑦ mv hadoop-3.1.4 /usr/local/hadoop的时候已经移动到这了
```

![image-20241020224609312](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241020224609312.png)



## #2.习题4   写一段开机自启动的欢迎词

```
************************************
欢迎登录南充职业技术学院云计算机平台
************************************

#在容器中：
cd /etc/profile.d/
touch welcome.sh
vi welcome.sh 

#!/bin/bash
echo "************************************"
echo "Welcome to log in to the cloud computing platform of Nanchong Vocational and Technical College"
echo "************************************"

#ESC键 => :wq
exit
docker exec -it kk  /bin/bash 
#如果出现欢迎词则成功了
```

![image-20241020230146519](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241020230146519.png)

## #3. 文章总结

```
以下是TXYZ对整篇文档的总结
1. which 命令和 whereis 命令
   - `which` 命令用于查找可执行文件的位置,它会在 `PATH` 环境变量指定的目录中搜索。
   - `whereis` 命令用于查找文件的位置,它会在标准位置中搜索,包括 `PATH` 环境变量指定的目录。

2. 为什么 Hadoop 会安装在 /usr/local 目录下
   - `/usr/local` 目录通常用于存放本地安装的程序,这样可以与系统自带的软件包区分开来。
   - 将 Hadoop 安装在 `/usr/local/hadoop` 目录下是一个常见的做法,这样可以方便管理和维护。

3. 设置环境变量
   - 使用 `export` 命令可以设置环境变量,使其在当前 shell 会话中生效。
   - 为了让环境变量在系统启动时自动生效,可以将设置语句写入 `/etc/profile.d/` 目录下的 shell 脚本中。这样,每次登录系统时,这些脚本都会被执行,环境变量也会被设置。

4. PATH 环境变量
   - `PATH` 环境变量包含了一系列目录路径,用于告诉系统在哪里查找可执行文件。
   - 当你执行一个命令时,系统会按照 `PATH` 变量中的目录顺序进行搜索,直到找到该命令为止。
   - 可以使用 `export PATH=$PATH:/new/path` 的方式将新的目录添加到 `PATH` 变量中。


问题1: 我们在 /etc/profile.d/ 目录中放入了一个开机启动的文件 xxx.sh,能不能用 which 命令找到它的路径,为什么?

回答: 不能

· 在 `/etc/profile.d/` 目录中放置的 `xxx.sh` 文件,是在系统启动时自动执行的 shell 脚本。

· 这个脚本中可以设置各种环境变量,包括 `PATH` 变量。

· 由于 `/etc/profile.d/` 目录是系统默认的环境变量设置目录,因此 `which` 命令是无法直接找到这个脚本的位置的。`which` 命令只能查找 `PATH` 变量中包含的目录。
```



# 五.手动安装java、ssh

## #1. 重新创建一个名为 bbc 的容器

```
#为了方便区分，现在重新创建一个名为 bbc 的容器
docker run -d --name=bbc   --privileged   centos8     /usr/sbin/init
docker exec -it bbc /bin/bash

#先进入容器试试能不能yum makecache这个文件
#如果yum 不了文件，那就进行重写地址：
mkdir -p /etc/docker
tee /etc/docker/daemon.json <<'EOF'
{
"registry-mirrors": ["https://docker.m.daocloud.io","https://huecker.io","https://dockerhub.timeweb.cloud","https://noohub.ru"]
}
EOF

#enter键

exit
systemctl daemon-reload
service docker restart
```



## #2. 修改软件安装源

```
#此时所有的容器都被关掉了，要先打开刚刚创建的bbc容器
docker start bbc
docker exec -it bbc /bin/bash

#修改软件安装源
sed -i 's/mirrorlist/#mirrorlist/g' /etc/yum.repos.d/CentOS-*
sed -i 's|#baseurl=http://mirror.centos.org|baseurl=http://vault.centos.org|g' /etc/yum.repos.d/CentOS-*
yum makecache
```



## #3. 准备软件和安装环境

### ① CP法

```
#在容器中 创建用于存放软件包的目录
mkdir  /opt/packages       
mkdir  /opt/programs 

#退出容器挂载，详细见 五， 也可先挂载后进入容器创建目录再退出复制
exit
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs/ -o allow_other

#复制到 根 和刚刚创建的容器中的路径
cp /mnt/hgfs/Folder/jdk-8u211-linux-x64.tar.gz /
docker cp //jdk-8u211-linux-x64.tar.gz bbc:/opt/packages     

# 进入容器解压
docker exec -it bbc  /bin/bash   
tar -zxvf  /opt/packages/jdk-8u211-linux-x64.tar.gz   -C  /opt/programs  
#  -C 指定解压路径


```



### ② 校园网法

```
#和6. 一样从 FTP 下载文件
#在容器中
wget   -P   /opt/packages/    ftp://172.16.170.50/jdk-8u211-linux-x64.tar.gz  
#  -P 指定保存路径
# 解压
tar -zxvf  /opt/packages/jdk-8u211-linux-x64.tar.gz   -C  /opt/programs  
#  -C 指定解压路径
```



## #4. 配置环境变量 (在容器中)

```
vi  /etc/profile.d/my_java.sh

export JAVA_HOME=/opt/programs/jdk1.8.0_211
export PATH=$PATH:$JAVA_HOME/bin

#ESC键 => :wq
exit
docker exec -it kk  /bin/bash   

#查看是否配置成功
export 
java   -version  
```



![image-20241021002823911](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241021002823911.png)





## #5. 安装 SSH 工具 

```
#openssh-server :服务端， openssh-clients :客户端
yum install -y   openssh-clients     openssh-server   

#启用 SSH 服务
systemctl enable sshd && systemctl start sshd

#设置密码为 bbc
echo  'root:bbc' | chpasswd
 
#为减小镜像体积，删除无用压缩包
#保存容器bbc为镜像bbc_java_ssh供以后使用。
rm  -rf  /opt/packages/jdk-8u211-linux-x64.tar.gz   #删除压缩包
exit          
docker stop bbc   
docker commit bbc bbc_java_ssh     
docker  images
```





# 六.安装 hadoop

[安装 hadoop——按教科书再做](https://docs.qq.com/doc/DZXdudUtOc29xVUxU)

```
习题6
制作镜像  java_ssh_hadoop
```

## #1. 创建容器

```
#使用前面创建好的镜像 java_ssh 来创建容器
docker run -d --name=bbc -h bbc --privileged java_ssh /usr/sbin/init   
```

## #2. 安装软件

### ①CP法  （未完善）

```
#退出容器挂载，详细见 五， 也可先挂载后进入容器创建目录再退出复制
exit
sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs/ -o allow_other

#复制到 根 和刚刚创建的容器中的路径
cp /mnt/hgfs/Folder/hadoop-2.7.6.tar.gz /
docker cp //hadoop-2.7.6.tar.gz bbc:/opt/packages     

# 进入容器解压
docker exec -it bbc  /bin/bash   
mkdir /opt/programs  
tar -zxvf  /opt/packages/hadoop-2.7.6.tar.gz -C  /opt/programs  
#  -C 指定解压路径


sudo mount -t fuse.vmhgfs-fuse .host:/ /mnt/hgfs/ -o allow_other
                                       #挂载点
#如果报错        
#  fuse: mountpoint is not empty
#  fuse: if you are sure this is safe, use the 'nonempty' mount option
sudo umount /mnt/hgfs/                



```



### ②校园网法

```
#进入容器
docker exec -it bbc /bin/bash
wget    -P   /opt/packages/   ftp://172.16.170.50/hadoop-2.7.6.tar.gz
#如果不能 wget，就yum   如果 yum 半天，那就 重启
yum install wget
wget    -P   /opt/packages/   ftp://172.16.170.50/hadoop-2.7.6.tar.gz

# 解压安装包 解压到 /opt/programs  目录中
mkdir /opt/programs
tar -zxvf /opt/packages/hadoop-2.7.6.tar.gz -C /opt/programs
ls /opt/programs/hadoop-2.7.6/
```

![image-20241021231627815](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241021231627815.png)



## #3.  设置系统环境变量

```
touch /etc/profile.d/my_hadoop.sh 
cat > /etc/profile.d/my_hadoop.sh   << 'eof' 
export HADOOP_HOME=/opt/programs/hadoop-2.7.6
export PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin
eof

cat  /etc/profile.d/my_hadoop.sh
exit
docker exec -it bbc /bin/bash
echo   $HADOOP_HOME
```

![image-20241021232946279](C:\Users\24390\AppData\Roaming\Typora\typora-user-images\image-20241021232946279.png)



## #4. 修改hadoop程序的文件hadoop-env.sh

```
#比较两次cat的最后几行，如果有 echo的两行，则正确
cat    $HADOOP_HOME/etc/hadoop/hadoop-env.sh 
echo "export JAVA_HOME=/opt/programs/jdk1.8.0_211" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh
echo "HADOOP_HOME=/opt/programs/hadoop-2.7.6" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh
cat    $HADOOP_HOME/etc/hadoop/hadoop-env.sh 
```



## #5. 运行测试

```
yum install  which  -y
hadoop version

#删除多余压缩文件，封装成镜像
rm /opt/packages/hadoop-2.7.6.tar.gz
exit
docker stop  bbc
docker commit bbc java_ssh_hadoop
docker images

#可能报错，但不影响：
/opt/programs/hadoop-2.7.6/bin/hadoop: line 166: /opt/programs/jdk1.8.0_211/bin/java: No such file or directory
```



 
