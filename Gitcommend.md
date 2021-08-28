#git 常用代码

##git下载和上传
##新建分支

####git下载和上传
1. $ cd pi/raspberrypi/                            //进入准备好的文件夹
//先将gitcode仓库clone到本地
2. $ git clone https://gitee.com/wang-aogang/usv-based-on-raspberry

3. $ cd usv-based-on-raspberry                    //进入本地仓库文件

4. $ git config --global user.name "XXXX"         //自报家门 - 你的名字或昵称

5. $ git config --global user.email "yyy@qq.com"  //自报家门 - 你的联系邮箱

//这个时候你可以把你新建一个开发文件，如：index.php
//查看状态 git status

6. $ git add .             //当前所有文件添加到暂存区， . 表示全部更新，<file>表示更新指定文件

7. $ git commit -m "my site home"    //提交到本地仓库并备注提交信息，注意：-m和备注之间有空格

8. $ git remot add origin https://gitee.com/用户地址/gitcode.git    //添加远程仓库

9. $ git push origin master                       //将本地提交推送到远程仓库

####新建分支
$ git branch 查看本地所有分支
$ git checkout -b dev 建立一个新的本地分支dev
$ git checkout dev 切换到本地dev分支
$ git push --set-upstream origin buoy             //切换分支