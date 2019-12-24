'''
@Descripttion: 
@version: 
@Author: Da Chuang
@Date: 2019-12-24 18:28:36
@LastEditors  : Da Chuang
@LastEditTime : 2019-12-24 19:02:45
'''

import twint
import os
import json
import sys
sys.path.insert(0, os.getcwd())
from utils import common_util
import config


'''Twint Config'''
c = twint.Config()
c.Proxy_host = '127.0.0.1'
c.Proxy_port = '1080'
c.Proxy_type = 'http'


def get_twitter_realDonaldTrump():
    '''
    @Descripttion: 
    @param {type} 
    @return: csv file about realDonaldTrump's tweets
    '''
    c.Username = 'realDonaldTrump'
    c.Store_csv = True
    c.Custom["tweet"] = ["id", "username", "date", "time", "tweet"]
    c.Output = './data/tweet_related_realDonaldTrump/realDonaldTrump.csv'
    twint.run.Search(c)

def main():
    get_twitter_realDonaldTrump()

if __name__ == '__main__':
    main()
