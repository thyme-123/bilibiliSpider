import os
from python项目.BilibiliSpider.project import Setting
from project import functions


sure=input("该操作会删除下载数据，是否确定删除(Y/N)>>")
if sure.lower()=="y":
    paths=os.listdir(Setting.download)
    for path in paths:
        functions.removeDir(Setting.download + os.sep + path)
    os.rmdir(Setting.download)
    os.mkdir(Setting.download)