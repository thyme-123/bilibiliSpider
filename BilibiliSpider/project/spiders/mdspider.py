import requests
import json
import os
import jsonpath
import threading
from ..spiders import epspider
from .. import functions, Setting


class MD():
    """
    MD爬虫
    爬取MD相关信息
    """
    def __init__(self,md):
        self.md=md

    def run(self):
        """
        番剧爬虫启动函数，爬取番剧，以标题为名保存
        :return: 无返回值
        """
        headers = {'Accept': 'application/json, text/plain, */*',
                   'Accept-Encoding': 'gzip, deflate, sdch',
                   'Accept-Language': 'zh-CN,zh;q=0.8',
                   'Cache-Control': 'no-cache',
                   'Connection': 'keep-alive',
                   'Cookie': Setting.Cookie,
                   'Host': 'api.bilibili.com',
                   'Origin': 'https://www.bilibili.com',
                   'Pragma': 'no-cache',
                   'Referer': 'https://www.bilibili.com/bangumi/media/md' + str(self.md),
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', }
        getseason_id_url = 'https://api.bilibili.com/pgc/review/user?media_id=' + str(self.md)
        getseason_id_r = requests.get(url=getseason_id_url, headers=headers)
        getseason_id_r_json = json.loads(getseason_id_r.text)
        season_id = jsonpath.jsonpath(getseason_id_r_json, '$..season_id')[0]
        title=jsonpath.jsonpath(getseason_id_r_json, '$..title')[0]
        url = "https://api.bilibili.com/pgc/web/season/section?season_id=" + str(season_id)
        r = requests.get(url=url, headers=headers)
        r_json = json.loads(r.text)
        epids=jsonpath.jsonpath(jsonpath.jsonpath(r_json,'$..episodes')[0],"$..id")
        long_titles = jsonpath.jsonpath(r_json, "$..long_title")
        titles=jsonpath.jsonpath(r_json, "$..title")
        if not os.path.isdir(Setting.download + os.sep + functions.char((title))):
            os.mkdir(Setting.download + os.sep + functions.char((title)))
        ids=[]
        for epid in epids:
            if epid not in ids:
                ids.append(epid)
        for i in range(len(ids)):
            if not os.path.isfile("%s%s%s%s%s.mp4"%(Setting.download, os.sep, title, os.sep, long_titles[i])):
                if Setting.manyTask_thread==False:
                    EP=epspider.EP("ep%i"%ids[i],"%s%s"%(functions.char(title),os.sep),"第%s话_%s"%(str(titles[i+1]),functions.char(long_titles[i])))
                    EP.getvideo()
                else:
                    t=threading.Thread()
            else:
                print("%s 已下载"%(long_titles[i]))

    def getAvlist(self):
        """
        获取MD下所有AV号
        :return: AV号列表
        """
        headers = {'Accept': 'application/json, text/plain, */*',
                   'Accept-Encoding': 'gzip, deflate, sdch',
                   'Accept-Language': 'zh-CN,zh;q=0.8',
                   'Cache-Control': 'no-cache',
                   'Connection': 'keep-alive',
                   'Cookie': Setting.Cookie,
                   'Host': 'api.bilibili.com',
                   'Origin': 'https://www.bilibili.com',
                   'Pragma': 'no-cache',
                   'Referer': 'https://www.bilibili.com/bangumi/media/md' + str(self.md),
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', }
        getseason_id_url = 'https://api.bilibili.com/pgc/review/user?media_id=' + str(self.md)
        getseason_id_r = requests.get(url=getseason_id_url, headers=headers)
        getseason_id_r_json = json.loads(getseason_id_r.text)
        season_id = jsonpath.jsonpath(getseason_id_r_json, '$..season_id')[0]
        title_names = jsonpath.jsonpath(getseason_id_r_json, '$..title')[0]
        title_name = char(title_names)
        url = "https://api.bilibili.com/pgc/web/season/section?season_id=" + str(season_id)
        r = requests.get(url=url, headers=headers)
        r_json = json.loads(r.text)
        aids = jsonpath.jsonpath(r_json, '$..aid')
        return aids

