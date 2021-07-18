import requests
import time
import random
import smtplib
from email.mime.text import MIMEText
from email.header import Header

header = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Host': 'zsb.jmu.edu.cn',
    'If-Modified-Since': 'Sun, 18 Jul 2021 13:32:30 GMT',
    'If-None-Match': '"25d62-5c765da38fed2-gzip"',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


orgurl = 'http://zsb.jmu.edu.cn/info/1041/3912.htm'
mail_sender = ''
mail_receivers = ['']
mail_host = ""
mail_user = ""
mail_pass = ""


def getdata():
    res = requests.get(url=orgurl)
    res.encoding = 'utf-8'
    content = res.text
    j = content.rfind('本科批')
    o = 0
    t = -1
    for sb in range(1, j):
        i = j - sb
        if content[i] == '>':
            o += 1
        if o == 5:
            t = i
            break
    # print(content)
    if content[(t + 1):(t + 3)] == '福建':
        # SMTP
        mail_msg = content
        message = MIMEText(mail_msg, 'html', 'utf-8')
        message['From'] = Header("Peacher", 'utf-8')
        message['To'] = Header("Peacher", 'utf-8')
        subject = '福建本科批已出！集美大学2021年招生省份投档线'
        message['Subject'] = Header(subject, 'utf-8')
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(mail_host, 25)  # 465加密端口无法使用，不知道为什么
            smtpObj.login(mail_user, mail_pass)
            smtpObj.sendmail(mail_sender, mail_receivers, message.as_string())
            print("Accepted: 邮件发送成功")
        except smtplib.SMTPException:
            print("Error: 无法发送邮件")
        exit(0)
    print(content[(t + 1):(t + 3)])


while True:
    time.sleep(random.randint(5, 10))
    getdata()
