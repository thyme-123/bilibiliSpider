import project.functions

bilibili = '''                                                
    ,]^                           ]/                         | 
  @@@@^                        @@@@@                         | 
  /@@@^              =@@@      =@@@@              =@@@       | 作者：thyme
  =@@@^               @@@      ,@@@@               @@@       | 版本：1.1
   @@@^          //@@ @@@ ,@]@  @@@@          =@@@ /@@^,@]@` | 
   @@@@          =@@@ =@@`=@O@^ =@@@          =@O@`=@@^ @O@^ | 
   =@@@           [   =@@^ [,[  =@@@           [    @@^ [`[` | 
   =@@@           @@@^ @@^ @@@^  @@@^          @@@@ @@@ @@@^ | 
    @@@@@@@]]`    =@@@ @@/ @@@^  @@@@@@@]]`    =@@@ /@@ @@@^ | 
    @@@@@@@@@@@@@],@@@ =@@ @@@^  =@@@@@@@@@@@@/ @@@^=@@ =@@^ | 
    =@@@@^  ,@@@@@^/@@^=@@ =@@^  =@@@@@   /@@@@/=@@^=@@^=@@^ | 
    =@@@@@,@@@@@@` =@@^=@@^=@@^   @@@@@,/@@@@@/  @@^ @@^,@@^ | 
     @@@@@@@@/`             [[`   @@@@@@@@/[             [[` | 
                                                             | 
哔哩哔哩 (゜-゜)つロ 干杯~
'''
print(bilibili)
print("番剧:ep/md")
print("小视频:av/bv")
print("音乐:au")
print("其它类型见help或输入help")

serve=input("请输入下载类型>>")

if serve.lower()=="bv":
    import project.spiders.bvspider
    bvid=input("请输入BV>>")
    if bvid[0:2]!="BV" and len(bvid)==10:
        bvid="BV"+bvid
    Bv = project.spiders.bvspider.BV(bvid)
    Bv.getvideo()
elif serve.lower()=="av":
    import project.spiders.avspider
    aid=input("请输入AV>>")
    if aid[0:2]!="av":
        aid="av"+aid
    Av = project.spiders.avspider.AV(aid)
    Av.getvideo()
elif serve.lower()=="ep":
    import project.spiders.epspider
    ep=input("请输入EP>>")
    if ep[0:2]!="ep":
        ep="ep"+ep
    Ep=project.spiders.epspider.EP(ep)
    Ep.getvideo()
elif serve.lower()=="md":
    import project.spiders.mdspider
    md=input("请输入MD>>")
    if md[0:2] == "md":
        md = md[2:]
    Md=project.spiders.mdspider.MD(md)
    eplist=Md.run()
elif serve.lower()=="help":
    import help
    print(help.help_1)
elif serve.lower()=="au":
    import project.spiders.auspider
    sid=input("请输入AU>>")
    if sid[0:2]=="au":
        sid=sid[2:]
    AU=project.spiders.auspider.AU(sid)
    AU.getaudio()
elif serve.lower()=="bvc":
    import project.spiders.fidspider
    import project.spiders.bvspider
    fid=input("请输入fid>>")
    if fid[0:3]=="fid":
        fid=fid[3:]
    FID=project.spiders.fidspider.FID()
    bvlist=FID.getBVlist()
    for bvid in bvlist:
        BV=project.spiders.bvspider.BV(bvid)
        BV.getvideo()
elif serve.lower()=="bvuid":
    import project.spiders.uidspider
    import project.spiders.bvspider
    uid=input("请输入UP主uid>>")
    UID=project.spiders.uidspider.UID(uid)
    bvlist=UID.getBVlist()
    for bvid in bvlist:
        BV=project.spiders.bvspider.BV()
        BV.getvideo()
elif serve.lower()=="mduid":
    import project.spiders.uidspider
    import project.spiders.mdspider
    uid=input("请输入UP主uid>>")
    UID=project.spiders.uidspider.UID(uid)
    mdlist=UID.getMDlist()
    for md in mdlist:
        MD=project.spiders.mdspider.MD()
        MD.run()
elif serve.lower()=="uiddrama":
    import project.spiders.uidspider
    import project.spiders.mdspider
    uid = input("请输入UP主uid>>")
    UID = project.spiders.uidspider.UID(uid)
    mdlist = UID.getDramaLsit()
    for md in mdlist:
        MD = project.spiders.mdspider.MD()
        MD.run()
elif serve.lower()=="tools":
    tool=input("请输入工具类型>>")
    if tool.lower()=="changeav":
        aid = input("请输入AV>>")
        if aid[0:2] == "av":
            aid = aid[2:]
        bv=project.functions.changeAV(int(aid))
        print(bv)
        input()
    elif tool.lower()=="changebv":
        bvid = input("请输入BV>>")
        if bvid[0:2] != "BV":
            bvid = "BV"+bvid
        av=project.functions.changeBV(bvid)
        print(av)
        input()
    elif tool.lower()=="coinav":
        import project.robots.coin
        aid=input("请输入AV>>")
        if aid[0:2] == "av":
            aid = aid[2:]
        Coin=project.robots.coin.Coin(aid)
        Coin.coin()
    elif tool.lower()=="coinbv" or tool.lower()=="coin":
        import project.robots.coin
        bvid=input("请输入BV>>")
        if bvid[0:2] != "BV":
            bvid = "BV"+bvid
        aid=project.functions.changeBV(bvid)
        Coin = project.robots.coin.Coin(aid)
        Coin.coin()
    elif tool.lower()=="coinup":
        import project.robots.coin
        import project.spiders.uidspider
        uid = input("请输入UID>>")
        UP=project.spiders.uidspider.UID(uid)
        avlist=UP.getAVlist()
        for av in avlist:
            Coin=project.robots.coin.Coin(av)
            Coin.coin()
    elif tool.lower()=="coinfid":
        import project.robots.coin
        import project.spiders.fidspider
        fid = input("请输入fid>>")
        if fid[0:3] == "fid":
            fid = fid[3:]
        FID=project.spiders.fidspider.FID(fid)
        avlist=FID.getAVlist()
        for av in avlist:
            Coin=project.robots.coin.Coin(av)
            Coin.coin()
    elif tool.lower()=="coinmd":
        import project.robots.coin
        import project.spiders.mdspider
        md = input("请输入MD>>")
        UP = project.spiders.mdspider.MD(md)
        avlist = MD.getAVlist()
        for av in avlist:
            Coin = project.robots.coin.Coin(av)
            Coin.coin()
    elif tool.lower()=="likeav":
        import project.robots.like
        aid = input("请输入AV>>")
        if aid[0:2] == "av":
            aid = aid[2:]
        Like=project.robots.like.Like(aid)
        Like.like()
    elif tool.lower()=="unlikeav":
        import project.robots.like
        aid = input("请输入AV>>")
        if aid[0:2] == "av":
            aid = aid[2:]
        Like = project.robots.like.Like(aid)
        Like.unlike()
    elif tool.lower()=="likebv" or tool.lower()=="like":
        import project.robots.like
        bvid = input("请输入BV>>")
        if bvid[0:2] != "BV":
            bvid = "BV" + bvid
        aid = project.functions.changeBV(bvid)
        Like = project.robots.like.Like(aid)
        Like.like()
    elif tool.lower()=="unlikebv" or tool.lower()=="unlike":
        import project.robots.like
        bvid = input("请输入BV>>")
        if bvid[0:2] != "BV":
            bvid = "BV" + bvid
        av = project.functions.changeBV(bvid)
        Like = project.robots.like.Like(aid)
        Like.unlike()
    elif tool.lower()=="likefid":
        import project.robots.like
        import project.spiders.fidspider
        fid=input("请输入fid>>")
        if fid[0:3] == "fid":
            fid = fid[3:]
        FID=project.spiders.fidspider.FID(fid)
        avlist=FID.getAVlist()
        for av in avlist:
            Like=project.robots.coin.Like(av)
            Like.like()
    elif tool.lower()=="unlikefid":
        import project.robots.like
        import project.spiders.fidspider
        fid = input("请输入fid>>")
        if fid[0:3] == "fid":
            fid = fid[3:]
        FID = project.spiders.fidspider.FID(fid)
        avlist = FID.getAVlist()
        for av in avlist:
            Like = project.robots.coin.Like(av)
            Like.unlike()
    elif tool.lower()=="likeup":
        import project.robots.like
        import project.spiders.uidspider
        uid = input("请输入UID>>")
        UP = project.spiders.uidspider.UID(uid)
        avlist = UP.getAVlist()
        for av in avlist:
            Like = project.robots.like.Like(av)
            Like.like()
    elif tool.lower()=="unlikeup":
        import project.robots.like
        import project.spiders.uidspider
        uid = input("请输入UID>>")
        UP = project.spiders.uidspider.UID(uid)
        avlist = UP.getAVlist()
        for av in avlist:
            Like = project.robots.like.Like(av)
            Like.unlike()
    elif tool.lower()=="likemd":
        import project.robots.like
        import project.spiders.mdspider
        md = input("请输入MD>>")
        UP = project.spiders.mdspider.MD(md)
        avlist = MD.getAVlist()
        for av in avlist:
            Like = project.robots.like.Like(av)
            Like.like()
    elif tool.lower()=="unlikemd":
        import project.robots.like
        import project.spiders.mdspider
        md = input("请输入MD>>")
        UP = project.spiders.mdspider.MD(md)
        avlist = MD.getAVlist()
        for av in avlist:
            Like = project.robots.like.Like(av)
            Like.unlike()
    elif tool.lower()=="dealbv" or tool.lower()=="deal":
        deal(bv,fid)








