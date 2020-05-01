from app import get_logger, get_config
import math,json
from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import utils
from utils import common_util
import config
import networkx as nx
from ..models import textdatecount,worddensitys,worddensity_mention,Posneg,worddensity_china,worddensity_chinesevirus
from .forms import ShortestPathForm
from . import main

logger = get_logger(__name__)
cfg = get_config()

# 通用列表查询
def common_list(DynamicModel, view):
    # 接收参数
    action = request.args.get('action')
    id = request.args.get('id')
    page = int(request.args.get('page')) if request.args.get('page') else 1
    length = int(request.args.get('length')) if request.args.get('length') else cfg.ITEMS_PER_PAGE

    # 删除操作
    if action == 'del' and id:
        try:
            DynamicModel.get(DynamicModel.id == id).delete_instance()
            flash('删除成功')
        except:
            flash('删除失败')

    # 查询列表
    query = DynamicModel.select()
    total_count = query.count()

    # 处理分页
    if page: query = query.paginate(page, length)

    dict = {'content': utils.query_to_list(query), 'total_count': total_count,
            'total_page': math.ceil(total_count / length), 'page': page, 'length': length}
    return render_template(view, form=dict, current_user=current_user)


# 通用单模型查询&新增&修改
def common_edit(DynamicModel, form, view):
    id = request.args.get('id', '')
    if id:
        # 查询
        model = DynamicModel.get(DynamicModel.id == id)
        if request.method == 'GET':
            utils.model_to_form(model, form)
        # 修改
        if request.method == 'POST':
            if form.validate_on_submit():
                utils.form_to_model(form, model)
                model.save()
                flash('修改成功')
            else:
                utils.flash_errors(form)
    else:
        # 新增
        if form.validate_on_submit():
            model = DynamicModel()
            utils.form_to_model(form, model)
            model.save()
            flash('保存成功')
        else:
            utils.flash_errors(form)
    return render_template(view, form=form, current_user=current_user)


# 根目录跳转
@main.route('/', methods=['GET'])
@login_required
def root():
    return redirect(url_for('main.index'))


# 首页
@main.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('index.html', current_user=current_user)

@main.route('/twittercount', methods=['GET', 'POST'])
@login_required
def twittercount():
    allstatistic = textdatecount.query.all()
    date = []
    num = []
    for i in allstatistic:
        date.append(i.date)
        num.append(i.num)
    return render_template('twittercount.html', date=date, num=num)

@main.route('/twittertime', methods=['GET', 'POST'])
@login_required
def twittertime():
    return render_template('twittertime.html')

@main.route('/worddensity', methods=['GET', 'POST'])
@login_required
def worddensity():
    allword = worddensitys.query.all()
    words = []
    nums = []
    j = 0
    for i in allword:
        words.append(i.word)
        nums.append(i.num)
        if j > 100:
            break;
        j = j+1;
    return render_template('worddensity.html', word=words, num=nums)

@main.route('/iddensity', methods=['GET', 'POST'])
@login_required
def iddensity():
    allword2 = worddensity_mention.query.all()
    words2 = []
    nums2 = []
    j = 0
    for i in allword2:
        words2.append(i.word)
        nums2.append(i.num)
        if j > 100:
            break;
        j = j + 1;
    #num = allword.num
    return render_template('iddensity.html',word2=words2, num2=nums2)

@main.route('/tweetemotion', methods=['GET', 'POST'])
@login_required
def tweetemotion():
    allstatistic = Posneg.query.all()
    pos = 0
    neg = 0
    neu = 0
    pos_neg = []
    posrate = []
    negrate = []
    tweet = []
    date = []
    for i in allstatistic:
        if i.pos_neg == "Negative":
            neg += 1
        elif i.pos_neg == "Neutral":
            neu += 1
        else:
            pos += 1
        pos_neg.append(i.pos_neg)
        tweet.append(i.tweet)
        posrate.append(i.pos)
        negrate.append(-i.neg)
        date.append(i.date)
    return render_template('tweetemotion.html',tweet=tweet,pos=pos,neg=neg,neu=neu,posrate=posrate,negrate=negrate,pos_neg=pos_neg,date=date)

@main.route('/emotion_and_data', methods=['GET', 'POST'])
@login_required
def emotion_and_data():
    return render_template('emotion_and_data.html')

@main.route('/staticdata', methods=['GET', 'POST'])
@login_required
def staticdata():
    allstatistic = Posneg.query.all()
    likes_count = []
    replies_count = []
    retweets_count = []
    date = []
    tweet = []
    j = 0
    for i in allstatistic:
        tweet.append(i.tweet)
        likes_count.append(i.likes_count)
        replies_count.append(i.replies_count)
        retweets_count.append(i.retweets_count)
        date.append(i.date)
        j=j+1
    print(j)
    return render_template('staticdata.html',tweet=tweet,likes_count=likes_count, replies_count=replies_count, retweets_count=retweets_count, date=date)

@main.route('/tweet_about_china', methods=['GET', 'POST'])
@login_required
def tweet_about_china():
    allword = worddensity_china.query.all()
    words = []
    nums = []
    j = 0
    for i in allword:
        words.append(i.word)
        nums.append(i.num)
        if j > 100:
            break;
        j = j + 1;
    return render_template('tweet_about_china.html', word=words, num=nums)

@main.route('/tweet_about_virus', methods=['GET', 'POST'])
@login_required
def tweet_about_virus():
    allword2 = worddensity_chinesevirus.query.all()
    words2 = []
    nums2 = []
    j = 0
    for i in allword2:
        words2.append(i.word)
        nums2.append(i.num)
        if j > 100:
            break;
        j = j + 1;
    return render_template('tweet_about_virus.html', word2=words2, num2=nums2)

@main.route('/socialnetwork', methods=['GET', 'POST'])
@login_required
def socialnetwork():
    data = dict()
    nodes = common_util.readjson(config.TWITTER_NODES_FILE)
    edges = common_util.readjson(config.TWINT_EDGES_FILE)
    data['nodes'] = nodes
    data['edges'] = edges
    print(data)
    return render_template('socialnetwork.html', data=json.dumps(data))

@main.route('/socialnetworkshortpath', methods=['GET', 'POST'])
@login_required
def socialnetworkshortpath():
    form = ShortestPathForm()
    data = dict()
    nodes = common_util.readjson(config.TWITTER_NODES_FILE)
    edges = common_util.readjson(config.TWINT_EDGES_FILE)
    data['nodes'] = nodes
    data['edges'] = edges
    G = nx.Graph()
    # print(nodes)
    # print(edges)
    id_id_map = {}  # 从node的id字段到这个id所在的序号
    id_num_map = {}
    data = dict()
    data_nodes = []
    data_edges = []
    path = ""
    cluster = ""
    cluster2 = ""
    if form.validate_on_submit():
        name1 = form.name1.data
        name2 = form.name2.data
        id1 = -1
        id2 = -1
        for i in range(0, len(nodes)):
            # print(nodes[i])
            G.add_node(i)
            id_id_map[nodes[i]['id']] = i
            if nodes[i]['label'] == name1:
                id1 = nodes[i]['id']
            elif nodes[i]['label'] == name2:
                id2 = nodes[i]['id']
        for i in range(0, len(edges)):
            one = edges[i]['from']
            two = edges[i]['to']
            if one in id_id_map and two in id_id_map:
                G.add_edge(id_id_map[one], id_id_map[two])

        if nx.has_path(G, id_id_map[id1], id_id_map[id2]):
            result = nx.shortest_path(G, id_id_map[id1], id_id_map[id2])
            print(result)
            path = path + "最短路径："
            path = str(result)
            nametemp = nodes[result[0]]['label']
            path = path + nametemp
            data_nodes.append(nodes[result[0]])
            lastid = nodes[result[0]]['id']
            newid = -1
            cluster = cluster + "第一位政要的聚集系数："
            cluster2 = cluster2 + "第二位政要的聚集系数："
            cluster = cluster + str(nx.clustering(G)[id_id_map[id1]])
            cluster2 = cluster2 + str(nx.clustering(G)[id_id_map[id2]])
            # print(cluster)
            for j in range(1, len(result)):
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
            print("No path between " + name1 + " and " + name2)
            path = "No path between " + name1 + " and " + name2

        # print(data_nodes)
        # print(data_edges)
        data['nodes'] = data_nodes
        data['edges'] = data_edges
        # print(data)

    return render_template('socialnetworkshortpath.html', form=form, path=path, data=json.dumps(data),
                           clustering=cluster,clustering2=cluster2)