def down(num):
    import json
    import re
    import os
    import requests
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")
    circle = requests.get("http://gank.io/api/data/%E7%A6%8F%E5%88%A9/10/" + str(num))
    json = json.dumps(circle.text)
    print(json)
    pattern = "(http:[^\s]*?(jpg|png|PNG|JPG))"
    imgs = re.findall(pattern, json)
    for n in xrange(0, len(imgs)):
        print (imgs[n][0])
        path = imgs[n][0]
        filename = os.path.basename(path)
        temp = "D:/spider/gankio/fuli/" + filename
        response = requests.get(path)
        with open(temp, 'wb') as f:
            f.write(response.content)


for i in xrange(0, 100):
    down(i)
