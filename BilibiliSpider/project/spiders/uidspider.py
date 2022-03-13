import requests
import json
import jsonpath
import time
from .. import Setting


class UID():
    def __init__(self,uid):
        self.uid=uid

    def getMDlist(self):
        pn = 1
        mdlist = []
        headers = {'Accept': '*/*',
                   'Accept-Encoding': 'gzip, deflate, sdch',
                   'Accept-Language': 'zh-CN,zh;q=0.8',
                   'Cache-Control': 'no-cache',
                   'Connection': 'keep-alive',
                   'Cookie': Setting.Cookie,
                   'Host': 'api.bilibili.com',
                   'Pragma': 'no-cache',
                   'Referer': 'https://space.bilibili.com/' + self.uid + '/bangumi',
                   'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36", }
        start_url = "https://api.bilibili.com/x/space/bangumi/follow/list?type=1&vmid=" + self.uid + "&pn="
        while True:
            url = start_url + str(pn)
            r = requests.get(url=url, headers=headers)
            if len(r.text) <= 78:
                break
            else:
                jsonr = json.loads(r.text)
                md = jsonpath.jsonpath(jsonr, '$..media_id')
                for i in md:
                    mdlist.append(i)
                stop()
            pn = pn + 1
        return mdlist

    def getBVlist(self):
        pn = 1
        bvlist = []
        start_url = "https://api.bilibili.com/x/space/arc/search?mid=" + self.mid + "&ps=100&tid=0&pn="
        while True:
            url = start_url + str(pn)
            r = requests.get(url=url)
            if len(r.text) <= 200:
                break
            else:
                jsonr = json.loads(r.text)
                md = jsonpath.jsonpath(jsonr, '$..bvid')
                print(md)
                for i in md:
                    bvlist.append(i)
            pn = pn + 1
        return bvlist

    def getDramaLsit(self):
        pn=1
        mdlist=[]
        start_utl="https://api.bilibili.com/x/space/bangumi/follow/list?type=2&follow_status=0&ps=15&vmid="+self.uid+"&pn="
        while True:
            url=start_url+str(pn)+"&ts"+str(time.time())
            r=requests.get(url=url)
            if len(r.text)<=76:
                break
            else:
                jsonr = json.loads(r.text)
                md = jsonpath.jsonpath(jsonr, '$..media_id')
                for i in md:
                    mdlist.append(i)
                stop()
            pn = pn + 1
        return mdlist

    def getDynamic(self):
        start_url="https://api.vc.bilibili.com/dynamic_svr/v1/dynamic_svr/space_history?visitor_uid=" + Setting.UID + "&need_top=1&platform=web&host_uid=" + self.uid
        offset_dynamic_id = 0
        id_list=[]
        while True:
            print("%s&offset_dynamic_id=%s"%(start_url,offset_dynamic_id))
            r=requests.get(url="%s&offset_dynamic_id=%s"%(start_url,offset_dynamic_id))
            jsonr=json.loads(r.text)
            try:
                cards=jsonpath.jsonpath(jsonr,"$..cards")[0]
            except:
                return id_list
            for i in range(len(cards)):
                card=cards[i]
                dynamic_id_str=jsonpath.jsonpath(card,"$.desc.dynamic_id_str")[0]
                id_list.append(dynamic_id_str)
                if i+1==len(cards):
                    offset_dynamic_id=dynamic_id_str

    def getAVlist(self):
        pn = 1
        avlist = []
        start_url = "https://api.bilibili.com/x/space/arc/search?mid=" + self.uid + "&ps=100&tid=0&pn="
        while True:
            url = start_url + str(pn)
            r = requests.get(url=url)
            if len(r.text) <= 200:
                break
            else:
                jsonr = json.loads(r.text)
                md = jsonpath.jsonpath(jsonr, '$..aid')
                for i in md:
                    avlist.append(i)
            pn = pn + 1






