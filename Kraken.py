#!/usr/bin/env python3

import sys
import platform
import time
import base64
import hashlib
import hmac
import urllib.request as urllib2

api_domain = "https://api.kraken.com"

# Example of calling public
def call_public():
    api_path = "/0/public/"
    api_method = "Trades"
    api_data = "pair=XBTUSD&since=1574067140000000000"
    api_request = urllib2.Request(api_domain + api_path + api_method + '?' + api_data)
    api_request.add_header("User-Agent", "Kraken REST API")
    api_reply = urllib2.urlopen(api_request).read()
    api_reply = api_reply.decode()
    print(api_reply)

# Example of calling private
def call_private():
    api_path = "/0/private/"
    api_method = "Balance"
    api_data = ""
    
    api_nonce = str(int(time.time()*1000))
    api_key = open("API_Public_Key").read().strip()
    api_secret = base64.b64decode(open("API_Private_Key").read().strip())
    
    api_postdata = api_data + "&nonce=" + api_nonce
    api_postdata = api_postdata.encode('utf-8')
    
    api_sha256 = hashlib.sha256(api_nonce.encode('utf-8') + api_postdata).digest()
    api_hmacsha512 = hmac.new(api_secret, api_path.encode('utf-8') + api_method.encode('utf-8') + api_sha256, hashlib.sha512)
    api_request = urllib2.Request(api_domain + api_path + api_method, api_postdata)
    api_request.add_header("API-Key", api_key)
    api_request.add_header("API-Sign", base64.b64encode(api_hmacsha512.digest()))
    api_request.add_header("User-Agent", "Kraken REST API")

    api_reply = urllib2.urlopen(api_request).read()
    api_reply = api_reply.decode()
    print(api_reply)

if __name__ == '__main__':
    print("Start")
    call_private()



    #
    # api_nonce = str(int(time.time()*1000))
    # api_postdata = api_data + "&nonce=" + api_nonce
    # api_postdata = api_postdata.encode('utf-8')
    # api_sha256 = hashlib.sha256(api_nonce.encode('utf-8') + api_postdata).digest()

    # api_path = "/0/public/"

    # api_hmacsha512 = hmac.new(api_secret, api_path.encode('utf-8') + api_method.encode('utf-8') + api_sha256, hashlib.sha512)
    # api_request = urllib2.Request(api_domain + api_path + api_method, api_postdata)

    # api_request.add_header("API-Key", api_key)
    # api_request.add_header("API-Sign", base64.b64encode(api_hmacsha512.digest()))
    # api_request.add_header("User-Agent", "Kraken REST API")

    

    
    # print(api_reply)