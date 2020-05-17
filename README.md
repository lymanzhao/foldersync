# foldersync

文件夹后台同步工具

在mac系统，前台拷贝5T文件夹，经常出现意外以及奔溃，所以借助Python功能写了个文件夹同步脚本，比前台复制功能快30%以上，稳定。

终端运行：

python3 foldersync.py

请输入要源文件夹：/Volumes/DT8T/藏书

请输入目标文件夹：/Volumes/Elements/藏书

目标文件夹不存在自动创建

## 依赖

需要安装dirsync

pip install dirsync

https://github.com/tkhyn/dirsync

## 兼容

mac系统；

理论上linux都可以使用；

windows未测试。

## 不足
多进程失败，遗憾，不过已经比前台复制快很多了，先凑活用吧。
