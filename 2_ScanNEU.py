import requests
import threading
import time
import random


header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'cookie': '_ntes_nnid=bd9cf2b27f6a91ac80fbb9d84c0cc34a,1624008525378; _ntes_nuid=bd9cf2b27f6a91ac80fbb9d84c0cc34a; timing_user_id=time_Yw5KofgIPi; UM_distinctid=17a4de79a15120e-09ba5c21dc15be-6373264-1bcab9-17a4de79a161248; _iuqxldmzr_=32; NMTID=00O9SYknaWESHlZSkEKp44NnKxf3fEAAAF6sfj_sw; WNMCID=rykfzg.1626483527736.01.0; WEVNSM=1.0.0; WM_NI=Xo33xil%2BS6BWPB256pozBU9nFdrbAM5vm%2FC0V1a1T2no0gc3WcVSMLy%2FN5Aa26wyljlADlAQMP6S4bMokyFqlbPEDsVb3j%2F7VBbVz0j3eRVAoQ9Z6sTXVYfcd%2FGNX108aEY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee8dc96b979da884ee598eb08bb7d14e978b8aaab6738bb098d8ee52968fbbaec72af0fea7c3b92a9cb1fdd4fb63b0f59dd7c15d949efed6b57cada68eb6bc6686bcbe83c447f7aaa3d0c23c96efafd2d73aaeb10088e23995bd9ab4d048bbf182d6c46bf2eab99aef62b09f8c8dc45b8f90fab4b76a8fb1a59ac57bb0bea0a6c77996befd8bae3d969eaeb7f93caaedabb3d54bad8ff7bbb57998889abae569a8f189afdb3bf4e8afa6dc37e2a3; WM_TID=%2FH5JQ2jH8xVFBVRVRBN%2BjJpH%2B8NBU%2BMS; playerid=63496476; ntes_kaola_ad=1; JSESSIONID-WYYY=ZKgZXG6AgAn%2B7J8hJtX0zyjoDH%2FB6Y5uyxo1CXwggat2EXAs7PhSN69B8nOYppXMIwZmZTCl4v3pSTy2VdDJwtgK8SdfKtyYP9aPU8oMvalqwgJOCCjjffD2cro2BDb0h5V4ulaheSvj1Al0NM7z35Mdl%2BEhqx2dzhaYdi2KSxWmCJN9%3A1626492291129; __csrf=3383ce544f9d6e2296d7b6a8b966e11d; MUSIC_U=bb6c60c31fe847ccb24885bb56f857f70dbfb9a24bc49efa631d0ae0e56bc15533a649814e309366',
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
