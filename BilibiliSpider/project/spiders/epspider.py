from ..item import Downloader
from ..item import Saver
from lxml import etree
import requests
import json
import jsonpath
import re
import threading
import time
import os
from .. import functions, Setting


class EP():
    """
    EP爬虫
    爬取EP号对应视频
    以标题为名保存
    """
    def __init__(self,ep,path="",title=""):
        self.ep=ep
        self.title=title
        self.path=path

    def getvideo(self):
        """
        EP爬虫启动函数，爬取格式为mp4
        :return: 无返回值
        """
        print("%s%s%s%s.mp4" % (Setting.download, os.sep, self.path, self.title))
        urlhtml = 'https://www.bilibili.com/bangumi/play/' + self.ep
        headersa = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Encoding': 'gzip, deflate, sdch',
                    'Accept-Language': 'zh-CN,zh;q=0.8',
                    'Cache-Control': 'no-cache',
                    'Connection': 'keep-alive',
                    'Cookie': Setting.Cookie,
                    'Host': 'www.bilibili.com',
                    'Pragma': 'no-cache',
                    'Upgrade-Insecure-Requests': '1',
                    'User-Agent': 'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.112 Safari/537.36', }
        r = requests.get(url=urlhtml, headers=headersa)
        if r.status_code==404:
            return None
        js=re.findall('window.__playinfo__=(.*?)</script>',r.text)[0]
        htjson=json.loads(js)
        html=etree.HTML(r.text)
        if self.title=="":
            self.title = html.xpath('//h1/@title')[0]
        print(self.title)
        print("开始下载")
        video = jsonpath.jsonpath(htjson, '$..data.dash.video')[0][0]
        baseUrls = jsonpath.jsonpath(video, '$..baseUrl')
        audio = jsonpath.jsonpath(htjson, '$..data.dash.audio')[0][0]
        baseupUrls = jsonpath.jsonpath(audio, '$..baseUrl')
        baseUrl = baseUrls[0]
        backupUrl = baseupUrls[0]
        headersbaseUrl = {'authority': 'cn-ahhn-cmcc-v-02.bilivideo.com',
                          'method': 'GET',
                          'path': baseUrl,
                          'range': 'bytes=0-1',
                          'scheme': 'https',
                          'accept': '*/*',
                          'accept-encoding': 'identity',
                          'accept-language': 'zh-CN,zh;q=0.9',
                          'cache-control': 'no-cache',
                          'origin': 'https://www.bilibili.com',
                          'pragma': 'no-cache',
                          'referer': 'https://www.bilibili.com/',
                          'sec-fetch-dest': 'empty',
                          'sec-fetch-mode': 'cors',
                          'sec-fetch-site': 'cross-site',
                          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
        headersbackupUrl = {'authority': 'cn-ahhn-cmcc-v-02.bilivideo.com',
                          'method': 'GET',
                          'path': backupUrl,
                          'range': 'bytes=0-1',
                          'scheme': 'https',
                          'accept': '*/*',
                          'accept-encoding': 'identity',
                          'accept-language': 'zh-CN,zh;q=0.9',
                          'cache-control': 'no-cache',
                          'origin': 'https://www.bilibili.com',
                          'pragma': 'no-cache',
                          'referer': 'https://www.bilibili.com/',
                          'sec-fetch-dest': 'empty',
                          'sec-fetch-mode': 'cors',
                          'sec-fetch-site': 'cross-site',
                          'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
        if Setting.standTask_thread==False:
            rxp = Downloader.download(url=baseUrl, headers=headersbaseUrl)
            Saver.saver(functions.char(self.title), rxp, "mp4")
            ryp = Downloader.download(url=backupUrl, headers=headersbackupUrl)
            Saver.saver(functions.char(self.title), ryp, "mp3")
            Saver.combine(functions.char(self.title),self.path)
        else:
            dav={"aideo":False,
                 "video":False,}
            tv=threading.Thread(target=lambda url,headers,title,dav:Saver.saver(functions.char(title), Downloader.download(url=url, headers=headers), "mp4",dav),args=(baseUrl,headersbaseUrl,self.title,dav))
            ta=threading.Thread(target=lambda url,headers,title,dav:Saver.saver(functions.char(title), Downloader.download(url=url, headers=headers), "mp3",dav),args=(backupUrl,headersbackupUrl,self.title,dav))
            tv.start()
            ta.start()
            while dav["aideo"]!=True or dav["video"]!=True:
                time.sleep(1)
            Saver.combine(functions.char(self.title), self.path)

