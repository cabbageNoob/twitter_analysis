# -*- coding: UTF-8 -*-
'''
@Descripttion: 
@version: 
@Author: Da Chuang
@Date: 2019-12-10 09:52:57
@LastEditors: Da Chuang
@LastEditTime: 2019-12-14 19:25:25
'''
import os
import sys
sys.path.insert(0, os.getcwd())

import numpy as np
import pandas as pd
import time, json
import twitter
import config
from utils import common_util

# create the object, assign it to a variable


api = twitter.Api(consumer_key=config.CONSUMER_KEY, consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_SECRET, proxies=config.proxy)

twitter_names = list()
twitter_countries = list()


def get_twitter_names():
    '''
    @Descripttion: get the twitter names
    @param {type} 
    @return: 
    '''
    # pandas读入
    data = pd.read_csv(config.TWITTER_NAMES_FILE)
    names = list(np.array(data['twitter@']))
    countries = list(np.array(data['country']))
    return names, countries


def get_nodes(names, countries):
    '''
    @Descripttion: get the node informations
    @param {type} 
    @return: 
    '''
    twitter_nodes = list()
    for name, country in zip(names, countries):
        node = dict()
        try:
            status = api.GetUser(screen_name=name, return_json=True)
        except Exception as identifier:
            print(identifier, name)
            continue
        node.setdefault('id', status.get('id'))
        node.setdefault('label', status.get('name'))
        node.setdefault('shape', 'circularImage')
        node.setdefault('image', status.get('profile_image_url'))
        node.setdefault('title', country)
        twitter_nodes.append(node)
    common_util.writejson2file(twitter_nodes, config.TWITTER_NODES_FILE)


def get_relationships(names):
    '''
    @Descripttion: get the norelationship informations
    @param {type} 
    @return: 
    '''
    twitter_edges = list()
    for one_index, one_name in enumerate(names):
        print(one_index, one_name)
        for two_index in range(one_index+1, len(names)):
            try:
                relationship = api.ShowFriendship(
                    source_screen_name=one_name, target_screen_name=names[two_index])
            except twitter.error.TwitterError as e:
                print(e, one_index)
                time.sleep(60 * 3)
                continue
            except StopIteration:
                break
            if (relationship['relationship']['source']['following']):
                edge = dict()
                edge.setdefault(
                    'from', relationship['relationship']['source']['id'])
                edge.setdefault(
                    'to', relationship['relationship']['target']['id'])
                twitter_edges.append(edge)
            if (relationship['relationship']['source']['followed_by']):
                edge = dict()
                edge.setdefault(
                    'from', relationship['relationship']['target']['id'])
                edge.setdefault(
                    'to', relationship['relationship']['source']['id'])
                twitter_edges.append(edge)
    common_util.writejson2file(twitter_edges, config.TWITTER_EDGES_FILE)


def test():
    blocks = api.ShowFriendship(source_screen_name='@realDonaldTrump',
                                target_screen_name='@jiahao60906194')  # 'Donald J. Trump'
    print("blocks", blocks)


if __name__ == '__main__':
    twitter_names, twitter_countries = get_twitter_names()
    # print(twitter_names)
    get_nodes(twitter_names,twitter_countries)
    # twitter_names = ['@ashrafghani', '@SalahRabbani', '@bnishaniZyrtare', '@ediramaal', '@ditmirbushati', '@fhollande', '@antonimartipeti', '@mauriciomacri', '@ZMnatsakanyan', '@TurnbullMalcolm',
    #                  '@HonJulieBishop']
    # get_relationships(twitter_names)
    # test()
