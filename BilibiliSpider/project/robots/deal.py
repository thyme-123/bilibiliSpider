import requests
from .. import Setting


class Deal():
    def __init__(self,aid,fid):
        self.aid=aid
        self.fid=fid

    def deal(self):
        headers = {'authority': 'api.bilibili.com',
                   'method': 'POST',
                   'path': '/x/web-interface/archive/like',
                   'scheme': 'https',
                   'accept': 'application/json, text/plain, */*',
                   'accept-encoding': 'gzip, deflate',
                   'accept-language': 'zh-CN,zh;q=0.8',
                   'cache-control': 'no-cache',
                   'content-length': '57',
                   'content-type': 'application/x-www-form-urlencoded',
                   'cookie': Setting.Cookie,
                   'origin': 'https://www.bilibili.com',
                   'pragma': 'no-cache',
                   'referer': 'https://www.bilibili.com/video/av' + str(self.aid),
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', }
        csrf = re.findall("bili_jct\=(.*?)\;", Setting.Cookie)
        data = {'rid': str(self.aid),
                'type': '2',
                'add_media_ids': self.fid,
                'del_media_ids': '',
                'jsonp': 'jsonp',
                'csrf': csrf, }
        r = requests.post(url=url, headers=headers, data=data)

    def undeal(self):
        headers = {'authority': 'api.bilibili.com',
                       'method': 'POST',
                       'path': '/x/web-interface/archive/like',
                       'scheme': 'https',
                       'accept': 'application/json, text/plain, */*',
                       'accept-encoding': 'gzip, deflate',
                       'accept-language': 'zh-CN,zh;q=0.8',
                       'cache-control': 'no-cache',
                       'content-length': '57',
                       'content-type': 'application/x-www-form-urlencoded',
                       'cookie': Setting.Cookie,
                       'origin': 'https://www.bilibili.com',
                       'pragma': 'no-cache',
                       'referer': 'https://www.bilibili.com/video/av' + str(self.aid),
                       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', }
        csrf = re.findall("bili_jct\=(.*?)\;", Setting.Cookie)
        data = {'rid': str(self.aid),
                    'type': '2',
                    'add_media_ids': '',
                    'del_media_ids': self.fid,
                    'jsonp': 'jsonp',
                    'csrf': csrf, }
        r = requests.post(url=url, headers=headers, data=data)