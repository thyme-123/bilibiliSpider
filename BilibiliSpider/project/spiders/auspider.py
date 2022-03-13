import requests
import re
from .. import functions, Setting
from ..item import Saver

class AU():
    """
    AU爬虫
    爬取AU号对应音频
    """
    def __init__(self,sid):
        self.sid=sid

    def getaudio(self):
        """
        爬虫启动函数
        :return: 无返回值
        """
        url_title = "https://www.bilibili.com/audio/music-service-c/web/song/info?sid=" + self.sid
        headers_title = {'authority': 'www.bilibili.com',
                         'method': 'GET',
                         'path': '/audio/music-service-c/web/song/of-coll?pn=1&ps=100&sid=' + self.sid,
                         'scheme': 'https',
                         'accept': '*/*',
                         'accept-encoding': 'gzip, deflate, br',
                         'accept-language': 'zh-CN,zh;q=0.9',
                         'cache-control': 'no-cache',
                         'cookie': Setting.Cookie,
                         'pragma': 'no-cache',
                         'referer': 'https://www.bilibili.com/audio/mycollection/' + self.sid,
                         'sec-fetch-dest': 'empty',
                         'sec-fetch-mode': 'cors',
                         'sec-fetch-site': 'same-origin',
                         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36', }
        titlec = requests.get(url=url_title, headers=headers_title)
        title = re.findall(r"title\"\:\"(.*?)\"", titlec.text)[0]
        print(title)
        print("开始下载")
        start_url = "https://www.bilibili.com/audio/music-service-c/web/url?sid=" + self.sid
        headers_start = {'authority': 'www.bilibili.com',
                         'method': 'GET',
                         'path': '/audio/music-service-c/web/url?sid=' + self.sid,
                         'scheme': 'https',
                         'accept': 'application/json, text/plain, */*',
                         'accept-encoding': 'gzip, deflate, br',
                         'accept-language': 'zh-CN,zh;q=0.9',
                         'cache-control': 'no-cache',
                         'cookie': Setting.Cookie,
                         'pragma': 'no-cache',
                         'referer': 'https://www.bilibili.com/audio/mycollection/' + self.sid,
                         'sec-fetch-dest': 'empty',
                         'sec-fetch-mode': 'cors',
                         'sec-fetch-site': 'same-origin',
                         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36', }
        au_r = requests.get(url=start_url, headers=headers_start)
        url = re.findall(r"cdns\"\:\[\"(.*?)\"", au_r.text)[0]
        headers_url = {'authority': 'upos-sz-mirrorks3.bilivideo.com',
                       'method': 'GET',
                       'path': url[39:],
                       'scheme': 'https',
                       'accept': '*/*',
                       'accept-encoding': 'identity;q=1, *;q=0',
                       'accept-language': 'zh-CN,zh;q=0.9',
                       'cache-control': 'no-cache',
                       'pragma': 'no-cache',
                       'range': 'bytes=0-',
                       'referer': 'https://www.bilibili.com/',
                       'sec-fetch-dest': 'audio',
                       'sec-fetch-mode': 'no-cors',
                       'sec-fetch-site': 'cross-site',
                       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36', }
        video = requests.get(url=url, headers=headers_url)
        Saver.saver(functions.char(title),video,"m4a")
