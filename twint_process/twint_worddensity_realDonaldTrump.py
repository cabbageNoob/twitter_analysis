import re, string
import pymysql
from operator import itemgetter
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

stoplist = stopwords.words('English')

def remove_noise(tweet_tokens, stop_words = ()):
    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)
        token = re.sub("\’","",token)
        token = re.sub("…", "", token)
        token = re.sub("http", "", token)
        token = re.sub("”", "", token)
        token = re.sub("“", "", token)
        token = re.sub("``", "", token)
        token = re.sub("\''", "", token)
        token = re.sub("\...", "", token)

        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatizer = WordNetLemmatizer()
        token = lemmatizer.lemmatize(token, pos)

        if len(token) > 0 and token not in string.punctuation and token.lower() not in stoplist:
            cleaned_tokens.append(token.lower())
    return cleaned_tokens

#读数据库
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='twitter_realdonaldtrump', charset='utf8')
cursor = conn.cursor()
cursor.execute('select * from tweet_realdonaldtrump_chinesevirus_with_posneg')
data = cursor.fetchall()
cols = cursor.description
conn.commit()
conn.close()
df = list(data)
ress= [x[4] for x in df]
results = []
for stu in ress:
    custom_tokens = remove_noise(word_tokenize(stu))
    results.extend(custom_tokens)

dic = {}
for word in results:
    if word not in dic:
        dic[word] = 1
    else:
        dic[word] = dic[word] + 1

swd = sorted( dic.items(), key = itemgetter(1), reverse=True)

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='', db='twitter_realdonaldtrump', charset='utf8')
cursor = conn.cursor()
sql = "insert into realdonaldtrump_worddensity_chinesevirus(word, num) values(%s,%s)"
cursor.executemany(sql, swd)
conn.commit()
conn.close()

