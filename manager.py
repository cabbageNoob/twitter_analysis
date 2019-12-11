# -*- coding: UTF-8 -*-
# Author: 
# Date: 19-12-10
# Brief:
import json
import re
import sys
import os
sys.path.insert(0, os.getcwd())
import config

from flask import Flask, render_template, redirect, request
app = Flask(__name__)


def readjson(filename):
    with open(filename, 'rb') as outfile:
        return json.load(outfile)

@app.route("/", methods=["GET", "POST"])
def index():
    data=dict()
    nodes = readjson(config.TWITTER_NODES_FILE)
    edges = readjson(config.TWITTER_EDGES_FILE)
    data['nodes'] = nodes
    data['edges'] = edges
    return render_template("graph_show.html",data=json.dumps(data))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)
