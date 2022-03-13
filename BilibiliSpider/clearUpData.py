import os
from python项目.BilibiliSpider.project import Setting
from project import functions

sure=input("该操作会删除缓存数据，是否确定删除(Y/N)>>")
if sure.lower()=="y":
    paths=os.listdir(Setting.updata)
    for path in paths:
        functions.removeDir(Setting.updata + os.sep + path)
    os.rmdir(Setting.updata)
    os.mkdir(Setting.updata)