# -*- coding: utf-8 -*-
'''
@Descripttion: 
@version: 
@Author: Da Chuang
@Date: 2019-12-11 10:40:21
@LastEditors: Da Chuang
@LastEditTime: 2019-12-12 22:16:08
'''

import os
# twitter api
proxy = {"http": "http://127.0.0.1:8580", "https": "https://127.0.0.1:8580"}

ACCESS_TOKEN = '1111937967235522560-N1Mzfz3TaWu9sw85jtITG6XvcXn8Cf'
ACCESS_SECRET = 'IKBfbt4jWJtX4DTByH1ITW7i74qpRS0Nuh8LaGeGogZSa'
CONSUMER_KEY = '5BZN0EFUNqMHQpfnj82MXMmej'
CONSUMER_SECRET = '0BEJ4ZtvVfneDslkztTgNTGTvBD53l2G7zgnh4Ok5J3RHGEdVk'

pwd_path = os.path.abspath(os.path.dirname(__file__))
# twitter origin names file
TWITTER_POLICES_NAME_FILE = os.path.join(
    pwd_path, './data/origin_twitter_names/人物Twitter对应表英文.xlsx')
# twitter 政要名单csv文件
TWITTER_NAMES_FILE = os.path.join(
    pwd_path, './data/clean_twitter_names/clean_Twitter.csv')
# twitter nodes json文件
TWITTER_NODES_FILE = os.path.join(
    pwd_path, './twitter_process/result/twitter_nodes.json')
# twitter edges json文件
TWITTER_EDGES_FILE = os.path.join(
    pwd_path, './twitter_process/result/twitter_edges.json')

# twint nodes json文件
TWINT_NODES_FILE = os.path.join(
    pwd_path, './twint_process/result/twint_nodes.json')
# twint nodes json文件
TWINT_EDGES_FILE = os.path.join(
    pwd_path, './twint_process/result/twint_edges.json')

#flasky
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI ='mysql+pymysql://root@127.0.0.1:3306/twitter_analysis'

config = {
    'default': DevelopmentConfig
}
