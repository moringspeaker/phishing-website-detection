from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
import os
import time

import requests
active_http_code=[100,101,200,201,202,203,204,205,206]
potential_active_http_code=[000,300,301,302,303,304,305,307]
def read():
    web_list=[]
    with open('./phishing-domains-ACTIVE.txt') as f:
        for line in f.readlines():
            web_list.append(str(line))
    return web_list

def catch(web_list):
    for i in range(0,len(web_list)-1):
        p=web_list[i].strip('\n')
        target='https://'+p
        try:
            headers = {
                       # 'Proxy-Connection': 'keep-alive',
                       # 'Host': web_list[i],
                       'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Mobile Safari/537.36',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                       'Accept-Encoding': 'gzip, deflate',
                       'Accept-Language': 'zh-TW,zh-CN;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6'
                       }
            r = requests.get(target,headers=headers,timeout=(5,10))
            print(r)
            if r.status_code in active_http_code or r.status_code in potential_active_http_code:
                with open('working_sites.txt', 'a') as fo:
                    fo.write(target + '\n')
            else:
                continue
        except :
            try:
                continue
            except:         #退出时输出断点
                w = target + str(i) + '\n'
                st = '  '+str(i+1)+w
                with open('log.txt', 'w') as f:
                    f.write(w)
                exit(0)

if __name__=='__main__':
    wl=read()
    catch(wl)