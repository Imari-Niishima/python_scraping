#Apache.py 2024/11/4 by Imari
#Apacheのバージョンを取得するプログラム
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


def version_check(apache_version):
#if __name__ == "__main__":
    url_base = "https://httpd.apache.org/"

    html_base = requests.get(url_base).text

    soup_base = BeautifulSoup(html_base, "html5lib")

    for a_each in soup_base.find_all("h1"):
        text_cand = a_each.get_text()

        #print(text_cand)
        #sys.exit()

        

        none_check = re.search("Released", text_cand)

        if (none_check is not None) == True:

            #now_version = re.findall("httpd (.*) Released", apache_version)
            pre_version = re.findall("httpd (.*) Released", "Apache httpd 2.2.12 Released 2022-07-17")
            now_version = re.findall("httpd (.*) Released", text_cand)
            
            pre_version = re.split("[.]", pre_version[0])
            now_version = re.split("[.]", now_version[0])

            
            #この処理はバージョンを受け取ってから考える？
            #
            for i in range(len(pre_version)):
                if pre_version[i] < now_version[i]:
                    print("version apdated!\n")
                    print(text_cand.rstrip("¶"))
                    return text_cand.rstrip("¶")
            
    #メイン関数で試すときはこの下にコメント
    return apache_version
            

    
  

    






