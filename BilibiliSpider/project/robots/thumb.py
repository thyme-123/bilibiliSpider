import requests
from .. import Setting


class Thumb():
    def __init__(self,id):
        self.id=id

    def thumb(self):
        url="https://api.vc.bilibili.com/dynamic_like/v1/dynamic_like/thumb"
        csrf = re.findall("bili_jct\=(.*?)\;", Setting.Cookie)
        data={'uid': Setting.UID,
              'dynamic_id': self.id,
              'up': '1',
              'csrf_token': csrf,
              'csrf': csrf,}
        headers={'authority': 'api.vc.bilibili.com',
                 'method': 'POST',
                 'path': '/dynamic_like/v1/dynamic_like/thumb',
                 'scheme': 'https',
                 'accept': 'application/json, text/plain, */*',
                 'accept-encoding': 'gzip, deflate, br',
                 'accept-language': 'zh-CN,zh;q=0.9',
                 'cache-control': 'no-cache',
                 'content-length': '130',
                 'content-type': 'application/x-www-form-urlencoded',
                 'cookie': Setting.Cookie,
                 'origin': 'https://t.bilibili.com',
                 'pragma': 'no-cache',
                 'referer': 'https://t.bilibili.com/',
                 'sec-fetch-dest': 'empty',
                 'sec-fetch-mode': 'cors',
                 'sec-fetch-site': 'same-site',
                 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
        r=requests.post(url=url,headers=headers,data=data)

    def unthumb(self):
        url = "https://api.vc.bilibili.com/dynamic_like/v1/dynamic_like/thumb"
        csrf = re.findall("bili_jct\=(.*?)\;", Setting.Cookie)
        data = {'uid': Setting.UID,
                'dynamic_id': self.id,
                'up': '2',
                'csrf_token': csrf,
                'csrf': csrf, }
        headers = {'authority': 'api.vc.bilibili.com',
                   'method': 'POST',
                   'path': '/dynamic_like/v1/dynamic_like/thumb',
                   'scheme': 'https',
                   'accept': 'application/json, text/plain, */*',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-language': 'zh-CN,zh;q=0.9',
                   'cache-control': 'no-cache',
                   'content-length': '130',
                   'content-type': 'application/x-www-form-urlencoded',
                   'cookie': Setting.Cookie,
                   'origin': 'https://t.bilibili.com',
                   'pragma': 'no-cache',
                   'referer': 'https://t.bilibili.com/',
                   'sec-fetch-dest': 'empty',
                   'sec-fetch-mode': 'cors',
                   'sec-fetch-site': 'same-site',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'}
        r = requests.post(url=url, headers=headers, data=data)
