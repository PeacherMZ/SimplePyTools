import requests
import threading
import time
import random


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': '',
    'accept-encoding': '',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cache-control': 'max-age=0',
    'referer': 'https://music.163.com/',
    'sec-ch-ua': '" Not;A Brand";v="99", "Google Chrome";v="91", "Chromium";v="91"',
    'sec-ch-ua-mobile': '?0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1'
}
orgurl = 'https://music.163.com/user/home?id='
myid = 1464044062


def scan_ne(start, end):
    for i in range(int(start), int(end)):
        time.sleep(random.randint(1, 3))
        url = orgurl + str(myid+i)
        print(url)
        res = requests.get(url=url, headers=header)
        res.encoding = 'utf-8'
        content = str(res.content)
#        print(content)
        j = content.rfind('nickname:"')
        print(j)
        if j == -1:
            continue
        name = ''
        for k in range(j+10, j+1000):
            if content[k] == '"':
                break
            name += content[k]
        if name == 'PeacherMZ':
            continue
        fname = name.encode().decode("unicode_escape").encode('raw_unicode_escape').decode()
        with open('res.txt', 'a') as add:
            add.write(fname+'\n')
        print(fname)


T1 = threading.Thread(target=scan_ne, args=(89, 120))
T1.start()
#T2 = threading.Thread(target=scan_ne, args=())
