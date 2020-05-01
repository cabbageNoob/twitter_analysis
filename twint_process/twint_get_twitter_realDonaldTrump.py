'''
@Descripttion: 
@version: 
@Author: Da Chuang
@Date: 2019-12-24 18:28:36
@LastEditors  : Da Chuang
@LastEditTime : 2019-12-29 20:06:32
'''

import twint
import os
import sys
sys.path.insert(0, os.getcwd())

'''Twint Config'''
c = twint.Config()
c.Proxy_host = '127.0.0.1'
c.Proxy_port = '9666'
c.Proxy_type = 'http'

def get_twitter_realDonaldTrump():
    '''
    @Descripttion: 
    @param {type} 
    @return: csv file about realDonaldTrump's tweets
    '''
    c.Username = 'realDonaldTrump'
    c.Store_csv = True
    c.Search = 'Chinese'  #爬取含某关键词推文时使用
    c.Since = '2017-01-20'
    c.Until = '2020-04-10'
    c.Custom["tweet"] = ["id", "username", "date",
                         "time", "tweet",  "replies_count", "retweets_count", "likes_count","mentions"]
    c.Output = 'D:/作业/毕设/project/twitter_analysis-master/data/tweet_related_realDonaldTrump/tweet_related_china.csv'
    print()
    twint.run.Search(c)

def main():
    get_twitter_realDonaldTrump()

if __name__ == '__main__':
    main()
