import urllib
import re
from urllib import request
import os
import threading

'''
加入多线程
'''


# response = request.urlopen("http://dict.youdao.com")
# html = response.read()
# response.geturl()
def makedir(dirpath):
    if not os.path.exists(dirpath):
        os.makedirs(dirpath)


def gethtml(url):
    req = request.Request(url)
    req.add_header('User-Agent', "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0")
    response = request.urlopen(req)
    html = response.readlines()
    return html


def getsearch(pattern, data):
    return re.search(pattern, str(data), re.M | re.S).group()


def getimgfromindex(save_dir, html2, pattern_title, pattern2, url2, index, pagelist):
    title = None
    for line2 in html2:
        if title == None:
            title_search = re.search(pattern_title, str(line2, encoding='utf-8'))
            if title_search != None:
                title = title_search.group(1)
                titlelist = title.split(" ")
                title = "_".join(titlelist)
                imgdir = os.path.join(save_dir, title)
                makedir(imgdir)
                # print(titlelist)
                print(title)
        # print(line2)
        line_2 = re.findall(pattern2, str(line2))
        if (len(line_2)) > 0:
            # print(line_2)
            # line_2_ = list(map(int, line_2))
            line_2_ = [int(x) for x in line_2]
            # print(line_2_)
            line_2_max = max(line_2_)
            # print(line_2_max)
            for i in range(2, line_2_max + 1):
                pagelist.append(f"{url2}/{i}.html")
    # print(pagelist)
    # exit(1119)
    # 解析每一页的图片

    # src = "https://tjg.hywly.com/a/1/38556/1.jpg"

    for pageurl in pagelist:
        # print(pageurl)
        # exit(1205)
        try:
            html3 = gethtml(pageurl)
        except:
            with open("error.txt", 'a') as f:
                print(pageurl, file=f)
        # https://tjg.hywly.com/a/1/38556/1.jpg
        pattern3 = f'<img src="(https://tjg.hywly.com/a/1/{index}/\d+.jpg)"'

        for line3 in html3:
            # print(f"line3:{line3}")

            # line_2 = pattern2.findall(str(line2))
            # print(str(line3))
            line_3 = re.findall(pattern3, str(line3))
            # print(len(line_3))
            # 每一页的图片只有一行
            if len(line_3) > 0:

                for picurl in line_3:
                    # print(f"picurl:{picurl}")
                    # exit(1202)
                    # imgname = picurl.split("/")[-1]
                    imgname = f"{title}-{picurl.split('/')[-1]}"

                    savepath = os.path.join(imgdir, imgname)


                    img = gethtml(picurl)
                    # print(os.path.exists(savepath))
                    # exit(1227)

                    if not os.path.exists(savepath):
                        with open(savepath, 'wb') as f:
                            f.writelines(img)
                        print(os.path.abspath(savepath))
                    else:
                        print(imgname)


if __name__ == '__main__':
    print()
    ids = 2426
    name = "柴婉艺"
    save_dir = rf"./tujigu/{name}_{ids}"
    ids2 = 27225
    url2 = f"https://www.tujigu.com/a/{ids2}"
    # url2 = "https://www.tujigu.com/a/25786/"


    # 解析每一位的索引
    i = 0
    tlist = []

    pagelist = []




    # 解析页码
    pagelist.append(url2)
    index = url2.split("/")[-1]
    print(f"url2:{url2}")
    html2 = gethtml(url2)
    pattern_title = "<h1>(.*)</h1>"
    pattern2 = f"{url2}/(\d*).html"
    getimgfromindex(save_dir, html2, pattern_title, pattern2, url2, index, pagelist)
    # exit()
    # t = threading.Thread(target=getimgfromindex,
    #                      args=[save_dir, html2, pattern_title, pattern2, url2, index, pagelist])
    # tlist.append(t)
    # i += 1
    # # getimgfromindex()
    # t.start()
    # if i % 10 == 0:
    #     for t_ in tlist:
    #         t_.join()
