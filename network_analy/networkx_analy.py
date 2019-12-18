'''
@Descripttion: 
@version: 
@Author: Da Chuang
@Date: 2019-12-18 22:25:45
@LastEditors  : Da Chuang
@LastEditTime : 2019-12-18 22:25:51
'''
import matplotlib.pyplot as plt
import os,sys
sys.path.insert(0, os.getcwd())

import config
from utils import common_util
import networkx as nx


def get_id_name(twitter_nodes):
    '''
    @Descripttion: get id_names lists
    @param {type} 
    @return: 
    '''    
    ids_names = {}
    for node in twitter_nodes:
        ids_names.setdefault(node['id'], node['label'])
    return ids_names


def get_graph(DG, twitter_nodes, twitter_edges):
    '''
    @Descripttion: add nodes for graph
    @param {type} 
    @return: 
    '''
    for node in twitter_nodes:
        DG.add_node(node['id'], name=node['label'])
    for edge in twitter_edges:
        DG.add_edge(edge['from'],edge['to'])
    

def main():
    '''
    @Descripttion: main function
    @param {type} 
    @return: 
    '''
    DG = nx.DiGraph()
    twitter_nodes = common_util.readjson(config.TWITTER_NODES_FILE)
    twitter_edges = common_util.readjson(config.TWITTER_EDGES_FILE)
    ids_names = get_id_name(twitter_nodes)
    get_graph(DG, twitter_nodes, twitter_edges)
    # nx.draw_networkx(DG,labels=ids_names,with_labels=True, font_weight='bold')
    # plt.show()
    # 聚集系数
    # print(nx.clustering(DG))
    # 社群 有向图未实现
    # print(list(nx.connected_components(DG)))
    id_degrees = sorted(dict(DG.degree).items(), key=lambda x: x[1], reverse=True)
    for id_degree in id_degrees[:10]:
        print(ids_names[id_degree[0]],id_degree[1])
    # sorted(d for n, d in )

if __name__ == '__main__':
    main()
