'''
@Descripttion: 
@version: 
@Author: Da Chuang
@Date: 2020-01-04 22:29:12
@LastEditors  : Da Chuang
@LastEditTime : 2020-01-04 22:34:13
'''
import twitter
import twint
import time
import numpy as np
import pandas as pd
import os
import json
import sys
sys.path.insert(0, os.getcwd())
import config
from utils import common_util

api = twitter.Api(consumer_key=config.CONSUMER_KEY, consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_SECRET, proxies=config.proxy)

def get_user(name):
    status = api.GetUser(screen_name=name, return_json=True)
    print(status)

if __name__ == '__main__':
    get_user('atsipras')
