import requests
from .. import Setting


class Complaint():
    def __init__(self,cv):
        self.cv=cv

    def run(self):
        csrf = re.findall("bili_jct\=(.*?)\;", Setting.Cookie)
        data = {'aid': self.cv,
                'cid': '4',
                'reason': Setting.complaint_text,
                'images': '',
                'csrf': csrf, }
        headers = {'authority': 'api.bilibili.com',
                   'method': 'POST',
                   'path': '/x/article/complaints',
                   'scheme': 'https',
                   'accept': '*/*',
                   'accept-encoding': 'gzip, deflate',
                   'accept-language': 'zh-CN,zh;q=0.8',
                   'cache-control': 'no-cache',
                   'content-length': '152',
                   'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'cookie': Setting.Cookie,
                   'origin': 'https://www.bilibili.com',
                   'pragma': 'no-cache',
                   'referer': 'https://www.bilibili.com/read/cv' + cv,
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36', }
        r = requests.post(url=url, headers=headers, data=data)