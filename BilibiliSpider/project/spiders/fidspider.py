import requests
import re
import jsonpath
import json

class FID():
    """
    FID爬虫
    爬取FID相关信息
    """
    def __init__(self,fid):
        self.fid=fid

    def getBVlist(self):
        """
        启动函数，返回BV号列表
        :return: BV号列表
        """
        pn = 1
        bvlist = []
        start_url = "https://api.bilibili.com/x/v3/fav/resource/list?media_id=" + self.fid + "&ps=20&keyword=&order=mtime&type=0&tid=0&jsonp=jsonp&pn="
        while 1:
            url = start_url + str(pn)
            r = requests.get(url=url)
            if len(r.text) <= 620:
                break
            else:
                jsonr = json.loads(r.text)
                md = jsonpath.jsonpath(jsonr, '$..bvid')
                for i in md:
                    bvlist.append(i)
            pn = pn + 1
        return bvlist

    def getAVlist(self):
        """
        启动函数，返回AV号列表
        :return: AV号列表
        """
        pn = 1
        avlist = []
        start_url = "https://api.bilibili.com/x/v3/fav/resource/list?media_id=" + self.fid + "&ps=20&keyword=&order=mtime&type=0&tid=0&jsonp=jsonp&pn="
        while 1:
            url = start_url + str(pn)
            r = requests.get(url=url)
            if len(r.text) <= 620:
                break
            else:
                jsonr = json.loads(r.text)
                md = jsonpath.jsonpath(jsonr, '$..id')[1:]
                for i in md:
                    avlist.append(i)
            pn = pn + 1
        return avlist