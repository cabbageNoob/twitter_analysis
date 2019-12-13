# -*- coding: UTF-8 -*-
'''
@Descripttion: flask run function
@version: 
@Author: Da Chuang
@Date: 2019-12-10 09:33:16
@LastEditors: Da Chuang
@LastEditTime: 2019-12-13 23:03:04
'''
import sys, os, json, re
sys.path.insert(0, os.getcwd())
from utils import common_util
import config
from flask import Flask, render_template, redirect, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    data = dict()
    nodes = common_util.readjson(config.TWITTER_NODES_FILE)
    edges = common_util.readjson(config.TWITTER_EDGES_FILE)
    data['nodes'] = nodes
    data['edges'] = edges
    return render_template("graph_show.html", data=json.dumps(data))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)
