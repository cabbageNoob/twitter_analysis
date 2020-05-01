'''
@Descripttion: 
@version: 
@Author: Da Chuang
@Date: 2019-12-10 18:06:36
@LastEditors: Da Chuang
@LastEditTime: 2020-03-16 15:21:21
'''

import os
import sys
sys.path.insert(0, os.getcwd())
import config
import twint, twitter
import pandas as pd
import numpy as np
from utils import common_util


api = twitter.Api(consumer_key=config.CONSUMER_KEY, consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_SECRET, proxies=config.proxy)


'''Twint Config'''
c = twint.Config()
c.Proxy_host = '127.0.0.1'
c.Proxy_port = '9666'
c.Proxy_type = 'http'


# name_id字典
name_id = common_util.readjson(config.TWINT_NODES_FILE)
print(type(name_id))

def get_twitter_names():
    '''
    @description: get the twitter names
    @param {null} 
    @return: 
    '''
    # pandas读入
    data = pd.read_csv(config.TWITTER_NAMES_FILE, error_bad_lines=False)
    names = list(np.array(data['twitter@']))
    print(names)
    names = [name[1:] for name in names]
    return names


def get_nodes(names):
    '''
    @description: get the node informations
    @param {names} 
    @return: 
    '''
    twitter_nodes = dict()
    for name in names:
        try:
            status = api.GetUser(screen_name=name, return_json=True)
        except Exception as identifier:
            print(identifier, name)
            continue
        twitter_nodes.setdefault(name, status.get('id'))
    common_util.writejson2file(twitter_nodes, config.TWINT_NODES_FILE)


def get_relationships(names):
    '''
    @description: get the relationship informations
    @param {names} 
    @return: 
    '''
    twitter_edges = list()
    for one_name in names:
        print(names.index(one_name), one_name)
        try:
            followings = get_followings(one_name)
        except Exception as e:
            print(e)
            continue
        for two_name in names:
            if two_name in followings:
                edge = dict()
                print('from', one_name)
                print('to', two_name)
                edge.setdefault('from', name_id[one_name])
                edge.setdefault('to', name_id[two_name])
                twitter_edges.append(edge)
    common_util.writejson2file(twitter_edges, config.TWINT_EDGES_FILE)


def get_followings(name):
    '''
    @description: get followings from a name
    @param {name} 
    @return: 
    '''
    c = twint.Config()
    c.Proxy_host = '127.0.0.1'
    c.Proxy_port = '9666'
    c.Proxy_type = 'http'
    c.Username = name
    c.Hide_output = True
    c.Pandas = True
    c.Pandas_clean = True
    twint.run.Following(c)
    followed = twint.storage.panda.Follow_df["following"].tolist()[0]
    twint.storage.panda.Follow_df = None
    return followed


if __name__ == '__main__':
    twitter_names = get_twitter_names()
    print(twitter_names)
    get_nodes(twitter_names)
    get_relationships(twitter_names)
    # print(twitter_names)
    # test1()
    # get_id('realDonaldTrump')
    # followings = get_followings('antonimartipeti')
    # print(followings)
    # print(len(followings))
