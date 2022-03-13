import requests
from .. import Setting
from tqdm import tqdm

def download(url,headers):
    """
    下载器，下载数据，返回分段响应生成器
    :param url: 请求url
    :param headers: 请求头
    :return: 返回响应生成器
    """
    head=requests.get(url=url,headers=headers).headers
    size=int(head["Content-Range"].replace("bytes 0-1/",""))
    print("总大小:",size)
    for i in tqdm(range(0, size, Setting.ra_size)):
        if i+ Setting.ra_size>size:
            headers["range"]="bytes=%i-"%(i)
        else:
            headers["range"] = "bytes=%i-%i" % (i, i + Setting.ra_size - 1)
        res=getContent(url,headers)
        yield  res


def getContent(url,headers):
    """
    循环请求器，返回分段响应
    :param url: 请求URL
    :param headers: 请求头
    :return: 响应
    """
    while True:
        try:
            res=requests.get(url=url,headers=headers)
            return res
        except:
            pass


