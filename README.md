# 基于树莓派的的USV

#### 介绍
以树莓派4B为核心搭建一个无人船平台

#### 功能介绍


#### 软件架构
软件架构说明


#### 安装教程

1.  git clone https://gitee.com/wang-aogang/usv-based-on-raspberry
2.  cd usv-based-on-raspberry/Threading
3.  python3 Thread.py

#### 使用说明

1.  远程视频传输功能需要用到mjpg_streamer来实现，使用摄像头前请查看代码camera_thread.py，确保正确调用mjpg_streamer
2.  由于无线数传模块，GPS模块和九轴传感器模块都是通过USB与树莓派连接,所以在调试前先查看代码确保ttyUSB*对应的是正确的器件
3.  

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request


#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)
