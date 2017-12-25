# encoding=utf-8
import urllib2


def convert_to_builtin_type(obj):
    d = {}
    d.update(obj.__dict__)
    return d


class Welfare(object):
    name = ""
    description = ""
    createtime = ""


def down(num):
    import json
    import re
    import os
    import requests
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    circle = requests.get("http://gank.io/api/data/%E7%A6%8F%E5%88%A9/10/" + str(num))
    datas = json.loads(circle.text)
    result = datas["results"]
    print(len(result))
    for n in xrange(0, len(result)):
        try:
            bean = result[n]
            pattern = "(http:[^\s]*?(jpg|png|PNG|JPG|jpeg|JEPG))"
            imgs = re.findall(pattern, bean["url"])
            wel = Welfare()
            wel.name = os.path.basename(imgs[0][0])
            wel.description = bean["desc"]
            wel.createtime = bean["createdAt"]
            temp = "D:/spider/gankio/fuli/" + wel.name
            response = requests.get(bean["url"])
            with open(temp, 'wb') as f:
                f.write(response.content)
            url = "http://localhost:8080/welfare/register.do"
            data = json.dumps(wel.__dict__)
            headers = {'Content-Type': "application/json; charset=utf-8"}
            req = urllib2.Request(url=url, headers=headers, data=data)
            html = urllib2.urlopen(req).read().decode('utf-8')
            print (html)
        except IndexError:
            print("系统异常")


for i in xrange(0, 100):
    down(i)
