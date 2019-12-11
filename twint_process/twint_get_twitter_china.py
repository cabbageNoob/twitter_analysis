# -*- coding: UTF-8 -*-
# Author:
# Date: 19-12-11
# Brief: get twitters related to China
import twitter
import twint
import config
import os
import json
import sys
sys.path.insert(0, os.getcwd())


api = twitter.Api(consumer_key=config.CONSUMER_KEY, consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_SECRET, proxies=config.proxy)


'''Twint Config'''
c = twint.Config()
c.Proxy_host = '127.0.0.1'
c.Proxy_port = '1080'
c.Proxy_type = 'http'

'''scrapy realDonaldTrump's tweets related to China and save output file'''


def get_tweet_related_china():
    c.Username = 'realDonaldTrump'
    c.Search = 'China'
    # c.Store_json=True
    c.Store_csv = True
    c.Replies = True
    c.Custom["tweet"] = ["id", "date", "time", "tweet"]
    # c.Output = 'DonaldTrump.json'
    c.Output = "DonaldTrump_reply.csv"
    twint.run.Search(c)


if __name__ == '__main__':
    get_tweet_related_china()
