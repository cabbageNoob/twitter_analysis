'''
@Descripttion: 
@version: 
@Author: Da Chuang
@Date: 2019-12-24 18:28:36
@LastEditors: Da Chuang
@LastEditTime: 2020-03-15 20:56:14
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

    # c.Since = '2016-01-20'
    c.Since = '2019-01-01'
    c.Until = '2019-01-18'
    c.Custom["tweet"] = ["id", "username", "date",
                         "time", "tweet", "place","geo", "replies_count", "retweets_count", "likes_count"]
    c.Output = '../data/tweet_related_realDonaldTrump/realDonaldTrump_test_wy.csv'


    twint.run.Search(c)

def main():
    get_twitter_realDonaldTrump()

if __name__ == '__main__':
    main()
