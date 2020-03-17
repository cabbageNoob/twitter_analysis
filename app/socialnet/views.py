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
import networkx as nx
from .forms import ShortestPathForm

@socialnet.route('/socialnetindex')
def socialnetindex():
    data = dict()
    nodes = common_util.readjson(config.TWITTER_NODES_FILE)
    edges = common_util.readjson(config.TWINT_EDGES_FILE)
    data['nodes'] = nodes
    data['edges'] = edges
    print(data)
    return render_template('socialnet/socialnetindex.html', data=json.dumps(data))

@socialnet.route('/socialman',methods=['GET', 'POST'])
def manQuery():
    pass

@socialnet.route('/shortestpath',methods=['GET', 'POST'])
def shortestpath():
    form = ShortestPathForm()
    data = dict()
    nodes = common_util.readjson(config.TWITTER_NODES_FILE)
    edges = common_util.readjson(config.TWINT_EDGES_FILE)
    data['nodes'] = nodes
    data['edges'] = edges
    G = nx.Graph()
    print(nodes)
    print(edges)
    id_id_map = {} # 从node的id字段到这个id所在的序号
    id_num_map = {}
    data = dict()
    data_nodes = []
    data_edges = []
    path = ""
    if form.validate_on_submit():
        name1 = form.name1.data
        name2 = form.name2.data
        id1 = -1
        id2 = -1
        for i in range(0,len(nodes)):
            print(nodes[i])
            G.add_node(i)
            id_id_map[nodes[i]['id']]=i
            if nodes[i]['label'] == name1:
                id1 = nodes[i]['id']
            elif nodes[i]['label'] == name2:
                id2 = nodes[i]['id']
        for i in range(0,len(edges)):
            one = edges[i]['from']
            two = edges[i]['to']
            if one in id_id_map and two in id_id_map:
                G.add_edge(id_id_map[one],id_id_map[two])

        if nx.has_path(G,id_id_map[id1],id_id_map[id2]):
            result = nx.shortest_path(G,id_id_map[id1],id_id_map[id2])
            print(result)
            path = str(result)
            path = path+"\n"
            nametemp = nodes[result[0]]['label']
            path = path + nametemp
            data_nodes.append(nodes[result[0]])
            lastid = nodes[result[0]]['id']
            newid = -1
            for j in range(1,len(result)):
                node_num = result[j]
                name = nodes[node_num]['label']
                path = path + "->" + name
                data_nodes.append(nodes[node_num])
                newid = nodes[result[j]]['id']
                temp = {}
                temp['from'] = lastid
                temp['to'] = newid
                data_edges.append(temp)
                lastid = newid
        else:
            print("No path between "+name1+" and "+name2)
            path = "No path between "+name1+" and "+name2

        print(data_nodes)
        print(data_edges)
        data['nodes'] = data_nodes
        data['edges'] = data_edges
        print(data)
    return render_template('socialnet/shortestpath.html',form=form,path=path,data=json.dumps(data))