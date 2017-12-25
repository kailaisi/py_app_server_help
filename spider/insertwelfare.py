import urllib2


class Welfare(object):
    name = ""
    desc = ""
    creattime = ""


def down(num):
    import json
    import re
    import os
    import requests
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    circle = requests.get("http://gank.io/api/data/%E7%A6%8F%E5%88%A9/10/" + str(num))
    json = json.loads(circle.text)
    result = json["results"]
    print(len(result))
    for n in xrange(0, len(result)):
        bean = result[n]
        wel = Welfare
        wel.name = os.path.basename(bean["url"])
        wel.desc = bean["desc"]
        wel.creattime = bean["createdAt"]
        temp = "D:/spider/gankio/fuli/" + wel.name
        response = requests.get(bean["url"])
        with open(temp, 'wb') as f:
            f.write(response.content)
        url = "http://localhost:8080/user/register.do"
        data = json.dump(wel)
        headers = {'Content-Type': "application/json; charset=utf-8"}
        req = urllib2.Request(url=url, headers=headers, data=data)
        html = urllib2.urlopen(req).read().decode('utf-8')


for i in xrange(0, 1):
    down(i)
