# encoding:utf-8
import requests
token = 'c04f8d66e96046ff8d82e01c22ddb526' #在push+网站中可以找到
title= '上课提醒！！' #改成你要的标题内容
content ='课程名称：软件技术 \n 时间：10点' #改成你要的正文内容
url = 'http://pushplus.hxtrip.com/customer/push/send?token='+token+'&title='+title+'&content='+content
requests.get(url)
