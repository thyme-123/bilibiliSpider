from ..item import Downloader
from ..item import Saver
import requests
import json
import jsonpath
import re
from .. import functions, Setting


class AV():
    """
    AV爬虫
    爬取AV号对应视频
    单P视频以标题为名保存，多P视频以标题加集数为名保存
    """
    def __init__(self,aid,title="",path=""):
        self.aid=aid
        self.title=title
        self.path=path

    def getvideo(self):
        """
        AV爬虫启动函数，爬取格式为mp4
        :return: 无返回值
        """
        api_cid = 'https://api.bilibili.com/x/web-interface/view?aid=' + self.aid[2:]
        r_cid = requests.get(api_cid)
        js = json.loads(r_cid.text)
        if jsonpath.jsonpath(js,"$..message")[0]=="稿件不可见":
            print("稿件不可见")
            return None
        cids = jsonpath.jsonpath(js, '$..cid')[1:]
        if self.title=="":
            self.title = jsonpath.jsonpath(js, "$..title")[0]
        print(self.title)
        print("开始下载")
        if len(cids)==1:
            urlhtml = 'https://www.bilibili.com/video/' + self.aid
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
            js=re.findall(r'<script>window\.__playinfo__=(.*?)</script>',r.text)[0]
            htjson=json.loads(js)
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
            rxp = Downloader.download(url=baseUrl, headers=headersbaseUrl)
            Saver.saver(functions.char(self.title), rxp, "mp4")
            ryp = Downloader.download(url=backupUrl, headers=headersbackupUrl)
            Saver.saver(functions.char(self.title), ryp, "mp3")
            Saver.combine(functions.char(self.title),self.path)
        else:
            p=1
            for cid in cids:
                urlhtml = 'https://www.bilibili.com/video/' + self.aid+"?p="+str(p)
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
                js = re.findall(r'<script>window\.__playinfo__=(.*?)</script>', r.text)[0]
                htjson = json.loads(js)
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
                rxp = Downloader.download(url=baseUrl, headers=headersbaseUrl)
                Saver.saver(functions.char(self.title+"(%i)"%(p)), rxp, "mp4")
                ryp = Downloader.download(url=backupUrl, headers=headersbackupUrl)
                Saver.saver(functions.char(self.title+"(%i)"%(p)), ryp, "mp3")
                Saver.combine(functions.char(self.title+"(%i)"%(p)),self.path)
                p+=1
