# -*- coding: UTF-8 -*-
# Author: 
# Date: 19-12-10
# Brief:

# create the object, assign it to a variable
import twitter
import os,sys
import json
import time
import pandas as pd
import numpy as np
sys.path.insert(0, os.getcwd())
import config

api = twitter.Api(consumer_key=config.CONSUMER_KEY, consumer_secret=config.CONSUMER_SECRET,
                  access_token_key=config.ACCESS_TOKEN, access_token_secret=config.ACCESS_SECRET, proxies=config.proxy)

twitter_names = list()
twitter_countries = list()

def writejson2file(data, filename):
    with open(filename, 'w', encoding='utf8') as outfile:
        data = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(data)


def readjson(filename):
    with open(filename, 'rb') as outfile:
        return json.load(outfile)


'''get the twitter names'''


def get_twitter_names():
    # pandas读入
    data = pd.read_csv(config.TWITTER_NAMES_FILE)
    names = list(np.array(data['twitter@']))
    countries = list(np.array(data['country']))
    return names,countries


'''get the node informations'''


def get_nodes(names,countries):
    twitter_nodes = list()
    for name,country in zip(names,countries):
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
    writejson2file(twitter_nodes, config.TWITTER_NODES_FILE)


'''get the norelationship informations'''


def get_relationships(names):
    twitter_edges = list()
    for one_index, one_name in enumerate(names):
        print(one_index,one_name)
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
    writejson2file(twitter_edges, config.TWITTER_EDGES_FILE)


def test():
    blocks = api.ShowFriendship(source_screen_name='@realDonaldTrump',
                                target_screen_name='@jiahao60906194')  # 'Donald J. Trump'
    print("blocks", blocks)


if __name__ == '__main__':
    twitter_names, twitter_countries = get_twitter_names()
    # print(twitter_names)
    # get_nodes(twitter_names,twitter_countries)
    # twitter_names = ['@ashrafghani', '@SalahRabbani', '@bnishaniZyrtare', '@ediramaal', '@ditmirbushati', '@fhollande', '@antonimartipeti', '@mauriciomacri', '@ZMnatsakanyan', '@TurnbullMalcolm',
    #                  '@HonJulieBishop']
    get_relationships(twitter_names)
    # test()
