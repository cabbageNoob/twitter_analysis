# -*- coding: UTF-8 -*-
# Author: cjh（492795090@qq.com）
# Date: 19-12-10
# Brief: use twint to get the relationships
import os,json
import twint
import twitter,time
import pandas as pd
import numpy as np
proxy = {"http": "http://127.0.0.1:1080", "https": "https://127.0.0.1:1080"}

ACCESS_TOKEN = '1111937967235522560-N1Mzfz3TaWu9sw85jtITG6XvcXn8Cf'
ACCESS_SECRET = 'IKBfbt4jWJtX4DTByH1ITW7i74qpRS0Nuh8LaGeGogZSa'
CONSUMER_KEY = '5BZN0EFUNqMHQpfnj82MXMmej'
CONSUMER_SECRET = '0BEJ4ZtvVfneDslkztTgNTGTvBD53l2G7zgnh4Ok5J3RHGEdVk'
api = twitter.Api(consumer_key=CONSUMER_KEY, consumer_secret=CONSUMER_SECRET,
                  access_token_key=ACCESS_TOKEN, access_token_secret=ACCESS_SECRET, proxies=proxy)

pwd_path = os.path.abspath(os.path.dirname(__file__))

TWITTER_NAMES_FILE = os.path.join(pwd_path, '../twitter_process/clean_Twitter.csv')
TWITTER_NODES_FILE = os.path.join(pwd_path, './result/twitter_nodes.json')
TWITTER_EDGES_FILE = os.path.join(pwd_path, './result/twitter_edges.json')

'''Twint Config'''
c = twint.Config()
c.Proxy_host = '127.0.0.1'
c.Proxy_port = '1080'
c.Proxy_type = 'http'


def writejson2file(data, filename):
    with open(filename, 'w', encoding='utf8') as outfile:
        data = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(data)


def readjson(filename):
    with open(filename, 'rb') as outfile:
        return json.load(outfile)

# name_id字典
name_id = readjson(TWITTER_NODES_FILE)

'''get the twitter names'''


def get_twitter_names():
    # pandas读入
    data = pd.read_csv(TWITTER_NAMES_FILE)
    names = list(np.array(data['twitter@']))
    names = [name[1:] for name in names]
    return names




'''get the node informations'''


def get_nodes(names):
    twitter_nodes = dict()
    for name in names:
        try:
            status = api.GetUser(screen_name=name, return_json=True)
        except Exception as identifier:
            print(identifier, name)
            continue
        twitter_nodes.setdefault(name, status.get('id'))
    writejson2file(twitter_nodes, TWITTER_NODES_FILE)

'''get the relationship informations'''


def get_relationships(names):
    twitter_edges = list()
    print('names',names)
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
    writejson2file(twitter_edges, TWITTER_EDGES_FILE)


'''get followings from a name'''


def get_followings(name):
    c = twint.Config()
    c.Proxy_host = '127.0.0.1'
    c.Proxy_port = '1080'
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
    # get_nodes(twitter_names)
    get_relationships(twitter_names)
    # print(twitter_names)
    # test1()
    # get_id('realDonaldTrump')
    # followings = get_followings('antonimartipeti')
    # print(followings)
    # print(len(followings))
 
   

