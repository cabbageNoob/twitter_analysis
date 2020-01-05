'''
@Descripttion: 
@version: 
@Author: Da Chuang
@Date: 2020-01-05 16:15:39
@LastEditors  : Da Chuang
@LastEditTime : 2020-01-05 17:30:51
'''
from . import socialnet
from flask import render_template

import sys, os, json
sys.path.insert(0, os.getcwd())
from utils import common_util
import config


@socialnet.route('/socialnetindex')
def socialnetindex():
    data = dict()
    nodes = common_util.readjson(config.TWITTER_NODES_FILE)
    edges = common_util.readjson(config.TWINT_EDGES_FILE)
    data['nodes'] = nodes
    data['edges'] = edges
    return render_template('socialnet/socialnetindex.html', data=json.dumps(data))

@socialnet.route('/socialman',methods=['GET', 'POST'])
def manQuery():
    pass
