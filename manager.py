# -*- coding: UTF-8 -*-
import json
import re
import sys
import os
sys.path.insert(0, os.getcwd())

from flask import Flask, render_template, redirect, request
app = Flask(__name__)
pwd_path = os.path.abspath(os.path.dirname(__file__))

TWITTER_NODES_FILE = os.path.join(pwd_path, './twitter_process/result/twitter_nodes.json')
TWITTER_EDGES_FILE = os.path.join(pwd_path, './twitter_process/result/twitter_edges.json')


def readjson(filename):
    with open(filename, 'rb') as outfile:
        return json.load(outfile)

@app.route("/", methods=["GET", "POST"])
def index():
    data=dict()
    nodes = readjson(TWITTER_NODES_FILE)
    edges = readjson(TWITTER_EDGES_FILE)
    data['nodes'] = nodes
    data['edges'] = edges
    return render_template("graph_show.html",data=json.dumps(data))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)
