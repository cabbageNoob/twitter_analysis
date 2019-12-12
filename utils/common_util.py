# -*- coding: UTF-8 -*-
'''
@Descripttion: common util function
@version: 
@Author: Da Chuang
@Date: 2019-12-12 16:58:43
@LastEditors: Da Chuang
@LastEditTime: 2019-12-12 22:19:38
'''

import json


def writejson2file(data, filename):
    '''
    @Descripttion: 
    @param {data}:
    @param {filename}:
    @return: 
    '''
    with open(filename, 'w', encoding='utf8') as outfile:
        data = json.dumps(data, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(data)


def readjson(filename):
    '''
    @Descripttion: 
    @param {filename} 
    @return: 
    '''
    with open(filename, 'rb') as outfile:
        return json.load(outfile)
