'''
@Descripttion: get twitters related to China
@version: 
@Author: Da Chuang
@Date: 2019-12-11 22:45:48
@LastEditors: Da Chuang
@LastEditTime: 2019-12-12 22:51:40
'''
import os
import json
import sys
sys.path.insert(0, os.getcwd())
from utils import common_util
import twint
import twitter
import config


api = twitter.Api(consumer_key=config.CONSUMER_KEY, consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_SECRET, proxies=config.proxy)


'''Twint Config'''
c = twint.Config()
c.Proxy_host = '127.0.0.1'
c.Proxy_port = '1080'
c.Proxy_type = 'http'

names = list(common_util.readjson(config.TWINT_NODES_FILE).keys())


def get_tweet_related_china(names):
    '''
    @description: scrapy realDonaldTrump's tweets related to China and save output file
    @param {names} 
    @return: 
    '''
    for name in names:
        print(name)
        c = twint.Config()
        c.Proxy_host = '127.0.0.1'
        c.Proxy_port = '1080'
        c.Proxy_type = 'http'
        c.Username = name
        c.Search = 'China'
        c.Store_csv = True
        c.Custom["tweet"] = ["id", "username", "date", "time", "tweet"]
        c.Output = './data/tweet_related_china/' + name + ".csv"  #
        try:
            twint.run.Search(c)
        except Exception as e:
            print(e)
            continue


if __name__ == '__main__':
    get_tweet_related_china(names)
