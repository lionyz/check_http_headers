import requests
import urllib3
import argparse

"""
python version>3.4会
以下6行代码解决因证书问题报错，报错内容如下：
requests.exceptions.SSLError: HTTPSConnectionPool(host='tgjbej.cpic.com.cn', port=443): Max retries exceeded with url: / (Caused by SSLError(SSLError(1, '[SSL: DH_KEY_TOO_SMALL] dh key too small (_ssl.c:997)')))
"""
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += 'HIGH:!DH:!aNULL'
try:
    requests.packages.urllib3.contrib.pyopenssl.DEFAULT_SSL_CIPHER_LIST += 'HIGH:!DH:!aNULL'
except AttributeError:
    pass

http_head = [
    "X-Frame-Options",
    "X-Content-Type-Options",
    "X-XSS-Protection",
    "Content-Security-Policy",
    "Strict-Transport-Security",
    "Referrer-Policy",
    "X-Download-Options",
    "X-Permitted-Cross-Domain-Policies"]

user_agent = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:95.0) Gecko/20100101 Firefox/95.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate",
    "Connection":"close",
}

get_http_headlist = []

def get_url(url):
    url_html = requests.get(url=url,headers=user_agent,verify=False)
    for key in url_html.headers.keys():
        get_http_headlist.append(key)
    return get_http_headlist

def check_http_head(list_http_headers):
    for i in http_head:
        if i not in list_http_headers:
            print("HTTP %s 缺失"%i)
    

def main():
    parse = argparse.ArgumentParser()
    parse.description = 'input target url'
    parse.add_argument("-u","--input u",help="target url",dest="url",type=str,default=None)
    args = parse.parse_args()
    #url = "https://ywxbej.cpic.com.cn"
    list_http_headers = get_url(args.url)
    check_http_head(list_http_headers)

if __name__ == "__main__":
    main()