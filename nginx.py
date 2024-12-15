#nginx.py 2024/11/17 by Imari
#nginxのバージョンを取得するプログラム
#今回読んだバージョンか、引数にした以前取ったバージョンのどっちかを文字列で返す
#それをバージョン管理のテキストに書き込むようにmain側でいじる
#動作確認のためにメイン関数にしてるけど使うときは関数の方に直すこと。
#returnとかのコメントも外す


import numpy
import os
import time
import requests
import urllib
import re
import sys
from bs4 import BeautifulSoup


#def version_check(old_version, old_date):
if __name__ == "__main__":
    
    #old_version = re.findall("nginx-(.*)\n", old_version)
    
    url_base = "https://nginx.org"

    html_base = requests.get(url_base).text

    soup_base = BeautifulSoup(html_base, "html5lib")

    news_table = soup_base.find_all("table", class_="news")[0]

   
    for a_each in news_table.find_all("tr"):
        text_cand = a_each.get_text()

        #print("****\n")
        #print(text_cand)

        #nginx-***とか2024-****で情報を取得して更新
        #mainlineという記述の有無でフラグ管理しよう


        now_version = re.findall("nginx-(.*)\n", text_cand)
        #print("now_version:", now_version)

        mainline_judge = re.findall("mainline", text_cand)#ここstableで欲しい情報手に入る
        #print("judge:", mainline_judge)

        if (len(mainline_judge) != 0) and (len(now_version) != 0):
            #print("ok!\n")

            #old_version = re.split("[.]", old_version)
            old_version = re.split("[.]", "1.22.1")
            now_version = re.split("[.]", now_version[0])

            for i in range(len(old_version)):
                if old_version[i] < now_version[i]:
                    print("version apdated!\n")
                    #print(now_version)

                    now_version = ".".join(now_version)
                    now_date = re.findall("(.*)\nnginx", text_cand)

                    print(str("nginx-"+now_version), now_date)
                    #return str("nginx-"+now_version)), now_date
        

    #return str("nginx-"+old_version)), old_date
            

    
  

    






