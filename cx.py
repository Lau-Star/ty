# coding=utf-8
import requests

key = "SCU96822Teacece914c94643dea76cf03bf3750755eb399b023adf" # your-key
url = "https://sc.ftqq.com/%s.send"%(key)
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'}

payload = {'123': '上课提醒！！', 'desp': '上课时间：800'}
requests.post(url, params=payload, headers=headers)
