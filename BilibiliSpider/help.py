"""
欢迎使用BilibiliSpider
"""

help_1="""
1.操作输入
bv 按BV号下载视频，视频以标题为名保存于download，自动将windos敏感字符和空格删除
av 按AV号下载视频，视频以标题为名保存于download，自动将windos敏感字符和空格删除
ep 按ep号下载番剧，视频以标题为名保存于download，自动将windos敏感字符和空格删除
md 按md号下载番剧，视频以标题为名保存于download目录下的番剧名称文件夹，自动将windos敏感字符和空格删除
au 按au号下载音乐，视频以标题为名保存于download，自动将windos敏感字符和空格删除
bvc 按fid下载收藏夹中的所有视频，视频以标题为名保存于download，自动将windos敏感字符和空格删除
bvuid 按uid下载uid下所有投稿视频，视频以标题为名保存于download，自动将windos敏感字符和空格删除
mduid 按uid下载uid下所有追番，视频以标题为名保存于download目录下的番剧名称文件夹，自动将windos敏感字符和空格删除
uiddrama 按uid下载uid下所有追剧，视频以标题为名保存于download目录下的番剧名称文件夹，自动将windos敏感字符和空格删除
tools 工具，未完成
"""

help_2="""
2.设置说明
设置文件为proje目录下的Seeting.py
Max_thread 多线程最大线程数
ra_size 每次最大下载量(byte)
ffmpeg ffmpeg路径
webdriver webdriver路径
download 保存路径
updata 缓存路径
coin 一键投币投币数(0,1,2)
select_like 投币同时点赞(点赞1,不点赞0)
complaint_text 一键举报内容
save_updata 视频下载缓存保留
logindata 登录数据(不可更改)
"""

help_3="""
3.文件列表
Main.py 主程序
help.py 帮助文件
login.py 登陆程序
data 登陆文件
download 下载文件
tools 第三方工具文件
  ffmpeg.exe ffmpeg，视频合成工具
  chromedirver.exe 谷歌浏览器控件
clearUpData 清理下载缓存
clearDownload 清理下载文件
clearCookie 清理Cookie
project 主文件
  __init__.py 骨架文件
  functions.py 辅助函数文件
  Setting.py 设置文件
  item 管道文件
    data 缓存文件夹
    Downloeader.py 下载器
    Saver.py 保存器
  robots 工具文件
    coin.py 投币工具
    complaint.py 举报工具
    deal.py 订阅工具
    like.py 点赞工具
    mkfid.py 创建收藏夹
    thumb.py 动态点赞工具
  spiders 爬虫
    auspider.py 音频爬虫
    avspider.py 视频爬虫
    bvspider.py 视频爬虫
    epspicer.py 番剧爬虫
    fidspider.py 收藏夹爬虫
    mdspider.py 番剧爬虫
    uidspider.py UID爬虫
"""

help="""
4.标准库列表
re
os
tqdm
json
threading
time
"""

help_5="""
5.第三方库列表
requests
lxml
jsonpath
cv2
qrcode
"""