import os
from .. import Setting

ffmpeg= Setting.ffmpeg
download= Setting.download
updata= Setting.updata

def saver(name,res,typ,dic=None):
    """
    保存器
    :param name: 文件名
    :param res: 响应
    :param typ: 文件类型
    :param dic: 路径，正常为无，路径为有用于保存番剧(md及其相关接口)
    :return: 无返回值
    """
    if typ=="mp4":
        mp4_saver(name,res,dic)
    if typ=="mp3":
        mp3_saver(name,res,dic)
    if typ=="m4a":
        m4a_saver(name,res)

def mp4_saver(name,res,dic):
    """
    MP4文件保存器，保存于data缓存文件夹
    :param name: 文件名
    :param res: 响应
    :param dic: 路径，正常为无，路径为有用于保存番剧(md及其相关接口)
    :return: 无返回值
    """
    with open("%s%s%s.mp4"%(updata,os.sep,name),"wb") as f:
        while True:
            try:
                content=next(res)
                f.write(content.content)
            except:
                break
    if dic!=None:
        dic["video"]=True

def mp3_saver(name,res,dic):
    """
    MP3文件保存器，保存于data缓存文件夹
    :param name: 文件名
    :param res: 响应
    :param dic: 路径，正常为无，路径为有用于保存番剧(md及其相关接口)
    :return: 无返回值
    """
    with open("%s%s%s.mp3"%(updata,os.sep,name),"wb") as f:
        while True:
            try:
                content = next(res)
                f.write(content.content)
            except:
                break
    if dic!=None:
        dic["aideo"]=True

def combine(name,path):
    """
    MP4、MP3文件合成器，保存于download文件夹
    :param name: 文件名
    :param path: 文件路径
    :return: 无返回值
    """
    print("正在合并视频和音频...")
    os.system("%s -loglevel quiet -i %s -i %s -c:v copy -c:a copy %s && exit" % (ffmpeg,"%s%s%s.mp4"%(updata,os.sep,name), "%s%s%s.mp3"%(updata,os.sep,name), "%s%s%s%s.mp4"%(download,os.sep,path,name)))
    print("%s.mp4 合并完成！" % name)
    if Setting.save_updata==False:
        os.remove("%s%s%s.mp4"%(updata,os.sep,name))
        os.remove("%s%s%s.mp3"%(updata,os.sep,name))

def m4a_saver(name,res):
    """
    M4a文件保存器
    :param name: 文件名
    :param res: 响应
    :return: 无返回值
    """
    with open("%s%s%s.m4a" % (Setting.download, os.sep, name), "wb") as f:
        f.write(res.content)
        print("下载完成")