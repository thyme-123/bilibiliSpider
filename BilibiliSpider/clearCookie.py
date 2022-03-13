import os
from python项目.BilibiliSpider.project import Setting
from project import functions

sure=input("该操作会删除登录数据，无法下载大会员专享视频和更高清晰度，是否确定删除(Y/N)>>")
if sure.lower()=="y":
    functions.removeDir(Setting.logindata)
    os.makedirs(Setting.logindata)