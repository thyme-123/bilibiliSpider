import os
import re

#版本
version=1.1
#日志路径
log_path=""
#多线程最大线程数
Max_thread=12
#多任务多线程
manyTask_thread=False
#并任务多线程
standTask_thread=False
#下载器多线程
downloaderTask_thread=False
#每次最大下载量(byte)
ra_size=4194304
#ffmpeg路径
ffmpeg= os.path.abspath(".") + os.sep + "tools" + os.sep + "ffmpeg.exe"
#webdriver路径
webdriver= os.path.abspath(".") + os.sep + "tools" + os.sep + "chromedriver.exe"
#保存路径
download= os.path.abspath(".") + os.sep + "download"
if not os.path.isdir(download):
    os.mkdir(download)
#缓存路径
updata= os.path.abspath(".") + os.sep + "project" + os.sep + "item" + os.sep + "data"
#if not os.path.isdir(updata):
    #os.mkdir(updata)
#一键投币投币数(0,1,2)
coin=2
#投币同时点赞(点赞1,不点赞0)
select_like=str(1)
#一键举报内容
complaint_text='内容虚假，涉及引战'
#视频下载缓存保留
save_updata=False
#登录数据
logindata= os.path.abspath(".") + os.sep + "data"
if not os.path.isdir(logindata):
    os.mkdir(logindata)
#创建收藏夹是否公开(公开0,不公开1)
privacy=0
#Cookie
if not os.path.isfile("%s%scookies.cod"%(logindata,os.sep)):
    print("登录获取更高清晰度")
    Cookie=""
else:
    Cookie= open("%s%scookies.cod"%(logindata,os.sep),"r").readline()
#UID
if Cookie=="":
    UID=""
else:
    try:
        UID=re.findall("DedeUserID= (.*?);",Cookie)[0]
    except:
        UID=""
