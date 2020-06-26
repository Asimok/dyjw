import matplotlib.pyplot as plt
import requests
from http.cookiejar import LWPCookieJar
# 保存Cookie
session = requests.Session()
# 创建cookie实例
session.cookies = LWPCookieJar('cookie')
head = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 "
                  "Safari/537.36"}

url_login = 'http://jwgl.nepu.edu.cn/Logon.do?method=logon'
url_verifyCode = 'http://www.tipdm.org/captcha.svl'
path = '/home/asimov/PycharmProjects/dyjw/data/'

# %%获取验证码

# 验证码保存路径
rq_verifyCode = requests.get(url_verifyCode)
with open(path + 'verifyCode.jpg', 'wb') as f:
    f.write(rq_verifyCode.content)
pic = plt.imread(path + 'verifyCode.jpg')
plt.imshow(pic)
plt.show()
verifyCode = input("请输入验证码\n")




# %%登录
login = {
    "USERNAME": '170703140113',
    "PASSWORD": '170703140113',
    "RANDOMCODE": verifyCode
}
rq_login = session.post(url_login, data=login, headers=head)

print(rq_login.status_code)
# 跳转网页
print(rq_login.url)
# 保存cookie
session.cookies.save(ignore_discard=True, ignore_expires=True)
# 加载保存的cookie
session.cookies.load(ignore_discard=True, ignore_expires=True)
# 用session保持登录状态
url_getXueqi = 'http://jwgl.nepu.edu.cn/tkglAction.do?method=kbxxXs'
newHtml = session.get(url_getXueqi, headers=head)
with open(path+'newHtml.html', 'w') as f:
    f.write(newHtml.content.decode('utf8'))
f.close()

