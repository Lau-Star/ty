# -*- coding: utf8 -*-
import os
import time
import urllib3
import asyncio
import re
import json
import requests
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


# =================配置区start===================

# server酱
server_chan_sckey = os.environ["CHAOXING_SERVER"]  # 申请地址http://sc.ftqq.com/3.version
server_chan = {
	'status': os.environ["CHAOXING_SERVEROR"] ,  # 如果关闭server酱功能，请改为False
	'url': 'https://sc.ftqq.com/{}.send'.format(server_chan_sckey)
}

# activeid保存文件路径
activeid_path = "activeid.txt"

# =================配置区end===================


class AutoSign(object):

def server_chan_send(msg):
	"""server酱将消息推送至微信"""
	desp = ''
	for d in msg:
		desp = '|  **课程名**  |   {}   |\r| :----------: | :---------- |\r'.format(d['name'])
		desp += '| **签到时间** |   {}   |\r'.format(d['date'])
		desp += '| **签到状态** |   {}   |\r'.format(d['status'])

	params = {
		'text': '上课提醒！！',
		'desp': desp
	}

	requests.get(server_chan['url'], params=params)

if __name__ == '__main__':
	print(local_run())
