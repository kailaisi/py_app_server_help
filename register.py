# encoding=utf-8
import sys

reload(sys)
sys.setdefaultencoding("utf-8")
import json
import random
import string
import time
import urllib2

x = input("请输入需要注册的数量:")


# x=raw_input() #转换成字符串的

def h(i, y):
    user = str(random.randint(15100000000, 18199999999))
    pwd = str(random.randint(100000, 99999999))
    age = random.randint(1, 150)
    name = ''.join(random.sample(string.ascii_letters + string.digits, random.randint(5, 20)))
    address = "天津市南开区凯德大厦c座4楼" + str(random.randint(1, 15000))
    sex = str(random.randint(0, 1))
    url = "http://localhost:8080/user/register.do"
    data = {"address": address, "age": age, "password": pwd, "sex": sex, "username": name, "phone": user}
    data = json.dumps(data)
    headers = {'Content-Type': "application/json; charset=utf-8"}
    req = urllib2.Request(url=url, headers=headers, data=data)
    print data
    # html=urllib2.urlopen(req).read()
    # print(html)
    html = urllib2.urlopen(req).read().decode('utf-8')

    print(html)
    print("注册成功，账号为%s，密码为%s，目前注册到第%s,还剩%s个" % (user, pwd, i + 1, y - i - 1))
    f = open("e:\user.txt", "a")
    f.write(str(html) + "\n")
    f.close()


for i in range(x):
    h(i, x)
    # 延时
    time.sleep(0.02)
