# encoding:utf-8
import requests
import json
token = 'c04f8d66e96046ff8d82e01c22ddb526' #在push+网站中可以找到
title= '上课提醒！！' #改成你要的标题内容
content ='课程名称：软件技术 时间：9点' #改成你要的正文内容
url = 'http://pushplus.hxtrip.com/customer/push/send'
data = {
    "token":token,
    "title":title,
    "content":content
}
body=json.dumps(data).encode(encoding='utf-8')
headers = {'Content-Type':'application/json'}
requests.post(url,data=body,headers=headers)
