import re, string, random
import csv
from nltk.tag import pos_tag
from nltk.stem.wordnet import WordNetLemmatizer
from nltk import FreqDist
#语料库使用
from nltk.corpus import twitter_samples
from nltk.corpus import stopwords
from nltk import classify
from nltk import NaiveBayesClassifier
from nltk.tokenize import word_tokenize


stoplist = stopwords.words('english')

# 对词性进行标注
positive_tweets = twitter_samples.strings('positive_tweets.json')
negative_tweets = twitter_samples.strings('negative_tweets.json')
text = twitter_samples.strings('tweets.20150430-223406.json')
tweet_tokens = twitter_samples.tokenized('positive_tweets.json')[0]

# 规范化数据
pos_tag(tweet_tokens)

#对句子进行词性还原&移除噪声
def lemmatize_sentence(tokens):
    lemmatizer = WordNetLemmatizer()
    lemmatize_sentence = []
    for word,tag in pos_tag(tokens):

        if tag.startswith('NN'):
            pos = 'n'
        elif tag.startswith('VB'):
            pos = 'v'
        else:
            pos = 'a'

        lemmatize_sentence.append(lemmatizer.lemmatize(word,pos))
        lemmatizer = WordNetLemmatizer()

    return lemmatize_sentence

#print(lemmatize_sentence(tweet_tokens))

# 移除噪声
def remove_noise(tweet_tokens, stop_words = ()):
    cleaned_tokens = []

    for token, tag in pos_tag(tweet_tokens):
        token = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+#]|[!*\(\),]|'\
                       '(?:%[0-9a-fA-F][0-9a-fA-F]))+','', token)
        token = re.sub('//.*', '', token)
        token = re.sub('picitterm/.*', '', token)
        token = re.sub("(@[A-Za-z0-9_]+)","", token)
        token = re.sub("\’", "", token)
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

#移除停止词
positive_tweet_tokens = twitter_samples.tokenized('positive_tweets.json')
negative_tweet_tokens = twitter_samples.tokenized('negative_tweets.json')

positive_cleaned_tokens_list = []
negative_cleaned_tokens_list = []

for tokens in positive_tweet_tokens:
    positive_cleaned_tokens_list.append(remove_noise(tokens, stopwords))

for tokens in negative_tweet_tokens:
    negative_cleaned_tokens_list.append(remove_noise(tokens, stopwords))

#print(positive_tweet_tokens[500])
#print(positive_cleaned_tokens_list[500])

#确定单词密度
def get_all_words(cleaned_tokens_list):
    for tokens in cleaned_tokens_list:
        for token in tokens:
            yield token

all_pos_words = get_all_words(positive_cleaned_tokens_list)

freq_dist_pos = FreqDist(all_pos_words)
#print(freq_dist_pos.most_common(10))

#将标记转为字典
def get_tweets_for_model(cleaned_tokens_list):
    for tweet_tokens in cleaned_tokens_list:
        yield dict([token, True] for token in tweet_tokens)

positive_tokens_for_model = get_tweets_for_model(positive_cleaned_tokens_list)
negative_tokens_for_model = get_tweets_for_model(negative_cleaned_tokens_list)

#分割数据集以训练和测试模型
positive_dataset = [(tweet_dict, "Positive")
                    for tweet_dict in positive_tokens_for_model]
negative_dataset = [(tweet_dict, "Negative")
                    for tweet_dict in negative_tokens_for_model]

dataset = positive_dataset + negative_dataset

random.shuffle(dataset)

train_data = dataset[:7000]
test_data = dataset[7000:]

#构建和测试模型
classifier = NaiveBayesClassifier.train(train_data)
print("Accuracy is:",classify.accuracy(classifier,test_data))
print(classifier.show_most_informative_features(30))

#读数据库
results = []
posre = []
negre = []
locfile = 'D:/作业/毕设/project/twitter_analysis-master/data/tweet_related_realDonaldTrump/tweet_related_china.csv'
newlocfile = 'D:/作业/毕设/project/twitter_analysis-master/data/tweet_related_realDonaldTrump/tweet_related_china_with_posneg.csv'
with open(locfile,'r',encoding="utf-8") as file:
#    file = open(locfile,'r',encoding="utf-8")
    stus = csv.reader(file)
    with open(newlocfile, 'w',encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        i = 0
        for stu in stus:
           custom_tweet = stu[4]
           custom_tokens = remove_noise(word_tokenize(custom_tweet))
           # print(custom_tokens)
           a = classifier.prob_classify(dict([token, True] for token in custom_tokens))
           res = classifier.classify(dict([token, True] for token in custom_tokens))
           pos = a.prob("Positive")
           neg = a.prob("Negative")
           results.append(res)
           posre.append(pos)
           negre.append(neg)
           writer = csv.writer(f)
           if i == 0:
               stu.append('pos_neg')
               stu.append('pos')
               stu.append('neg')
           else:
               if abs(posre[i]-negre[i]) < 0.5:
                   stu.append('Neutral')
               else:
                   stu.append(results[i])
               stu.append(posre[i])
               stu.append(negre[i])
           i = i + 1
           writer.writerow(stu)

#custom_tokens = remove_noise(word_tokenize(custom_tweet))
#print(classifier.classify(dict([token, True] for token in custom_tokens)))