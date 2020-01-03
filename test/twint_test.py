'''
@Descripttion: 
@version: 
@Author: Da Chuang
@Date: 2019-12-30 11:32:16
@LastEditors  : Da Chuang
@LastEditTime : 2019-12-30 22:08:48
'''

import os
import json
import sys
sys.path.insert(0, os.getcwd())
import twint
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
    c.Search='china'
    c.Store_csv = True
    # c.Hide_output = True
    # c.Replies=True
    c.Custom["tweet"] = ["id", 'conversation_id',"created_at", "username", "date",
                         "time", "tweet", "place", "geo", "replies_count", "retweets_count", "likes_count", "mentions", "photos", \
                             "hashtags","cashtags","retweet","quote_url","video"]
    c.Output = './data/tweet_related_realDonaldTrump/china_test_2.csv'
    twint.run.Search(c)


def get_user_realDonaldTrump():
    '''
    @Descripttion: get realDonaldTrump's details informations
    @param {type} 
    @return: 
    '''    
    c.Username = 'realDonaldTrump'
    c.Store_csv = True
    c.Hide_output = True
    c.Custom['user']=["id","username","bio","location","url","tweets","following","followers","likes","media","private","verified"]
    c.Output = './data/tweet_related_realDonaldTrump/realDonaldTrump_user_test.csv'
    twint.run.Lookup(c)
    
def main():
    get_twitter_realDonaldTrump()
    # get_user_realDonaldTrump()

if __name__ == '__main__':
    main()


