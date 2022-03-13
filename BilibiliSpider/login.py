import requests
import os
import re
import time
from python项目.BilibiliSpider.project import Setting
import qrcode
import cv2 as cv

headers={
   "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36",
}
logUrl="https://passport.bilibili.com/login"
getUrl="https://passport.bilibili.com/qrcode/getLoginUrl"
s=requests.session()
s.get(url=logUrl,headers=headers)
time.sleep(1)
res=s.get(url=getUrl,headers=headers)
oauthKey=re.findall("\"oauthKey\"\:\"(.*?)\"",res.text)[0]
url=re.findall("\"url\"\:\"(.*?)\"",res.text)[0]
data = {
        'oauthKey': oauthKey,
        'gourl': '',
}
getcookieURl="https://passport.bilibili.com/qrcode/getLoginInfo"
try:
    cv.destroyAllWindows()
except:
    pass
qrCode = qrcode.QRCode()
qrCode.add_data(url)
qrCode = qrCode.make_image()
qrCode.save("%s%sqrCode.png"%("data",os.sep))
img = cv.imread("%s%sqrCode.png"%("data",os.sep), 1)
cv.imshow("Login", img)
cv.waitKey()
time.sleep(1)
c2 = s.post(url=getcookieURl,headers=headers,data=data)
c3=s.get("https://space.bilibili.com/")
c4=s.post(url="https://passport.bilibili.com/qrcode/getLoginInfo",data={'oauthKey': '17bc7e4e162e82ff174af9b6f42736fd',
'gourl': 'https://www.bilibili.com/?rt=V%2FymTlOu4ow%2Fy4xxNWPUZ7QrO8i%2FDaRlDVdVLVChtSU%3D'})
cookies_dict=str(s.cookies.get_dict())
cookie=cookies_dict.replace("{","")
cookie=cookie.replace("}","")
cookie=cookie.replace(",",";")
cookie=cookie.replace(":","=")
cookie=cookie.replace("'","")
with open("%s%scookies.cod"%(Setting.logindata, os.sep), "w") as f:
    f.write(cookie)
    print(cookie)
os.remove("%s%sqrCode.png"%("data",os.sep))



