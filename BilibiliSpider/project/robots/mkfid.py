import requests
from .. import Setting
import jsonpath
import json

class NEWFID():
    def __init__(self):
        self.name=input("请输入收藏夹名称")
        self.intro=input("请输入简介")

    def run(self):
        url="https://api.bilibili.com/x/v3/fav/folder/add"
        headers={"authority":"api.bilibili.com",
                 "method":"POST",
                 "path":"/x/v3/fav/folder/add",
                 "scheme":"https",
                 "accept":"*/*",
                 "accept-encoding":"gzip, deflate, br",
                 "accept-language":"zh-CN,zh;q=0.9",
                 "cache-control":"no-cache",
                 "content-length":"73",
                 "content-type":"application/x-www-form-urlencoded",
                 "cookie": Setting.Cookie,
                 "origin":"https://space.bilibili.com",
                 "pragma":"no-cache",
                 "referer":"https://space.bilibili.com/",
                 "sec-fetch-dest":"empty",
                 "sec-fetch-mode":"cors",
                 "sec-fetch-site":"same-site",
                 "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
                 }
        csrf = re.findall("bili_jct\=(.*?)\;", Setting.Cookie)
        data={'title': self.name,
              'intro': self.intro,
              'privacy': Setting.privacy,
              'cover':'',
              'csrf': csrf,}
        res=requests.post(url=url,headers=headers,data=data)
        jsondata=json.loads(res.text)
        fid=jsonpath.jsonpath("$..id",jsondata)
        return fid

class DELFID():
    def __init__(self,fid):
        self.fid=fid

    def run(self):
        url="https://api.bilibili.com/x/v3/fav/folder/del"
        headers={"authority":"api.bilibili.com",
                 "method":"POST",
                 "path":"/x/v3/fav/folder/del",
                 "scheme":"https",
                 "accept":"application/json, text/plain, */*",
                 "accept-encoding":"gzip, deflate, br",
                 "accept-language":"zh-CN,zh;q=0.9",
                 "cache-control":"no-cache",
                 "content-length":"70",
                 "content-type":"application/x-www-form-urlencoded",
                 "cookie": Setting.Cookie,
                 "origin":"https://space.bilibili.com",
                 "pragma":"no-cache",
                 "referer":"https://space.bilibili.com/",
                 "sec-fetch-dest":"empty",
                 "sec-fetch-mode":"cors",
                 "sec-fetch-site":"same-site",
                 "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
                }
        csrf=re.findall("bili_jct\=(.*?)\;", Setting.Cookie)
        data={'media_ids': self.fid,
              'jsonp': 'jsonp',
              'csrf': csrf,}
        res=requests.post(url=url,headers=headers,data=data)

