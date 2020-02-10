'''
@Descripttion: 
@version: 
@Author: Da Chuang
@Date: 2019-12-30 22:23:16
@LastEditors  : Da Chuang
@LastEditTime : 2020-01-10 17:53:39
'''
import twint
from collections import Counter
import os

pwd_path = os.path.abspath(os.path.dirname(__file__))
test_csv=os.path.join(pwd_path,'../data/reply_test/reply2.csv')
# '''Twint Config'''
# c = twint.Config()
# c.Proxy_host = '127.0.0.1'
# c.Proxy_port = '1080'
# c.Proxy_type = 'http'

# # realDonaldTrump
# # 1215406817297088512
# c.Username = 'realDonaldTrump'
# c.Store_csv = True
# c.Custom["tweet"] = ["id", "conversation_id"]
# c.Output = test_csv
# twint.run.Search(c)

mothers = twint.Config()
mothers.Proxy_host = '127.0.0.1'
mothers.Proxy_port = '1080'
mothers.Proxy_type = 'http'
mothers.Username = "JoeySalads"
# mothers.Since = "2019-09-04"
# mothers.Until = "2019-09-08"
# mothers.Lang = 'en'
# mothers.Pandas = True
# mothers.Pandas_clean = True
mothers.Store_csv = True
mothers.Output = test_csv
# mothers.Hide_output = True
twint.run.Search(mothers)
df = twint.storage.panda.Tweets_df
Replies = {x: y for x, y in zip(df['conversation_id'], df['nreplies'])}

replies = twint.Config()
replies.Proxy_host = '127.0.0.1'
replies.Proxy_port = '1080'
replies.Proxy_type = 'http'
# replies.Since = "2019-09-04"
# replies.Until = "2019-09-10"
replies.Pandas = True
replies.To = "@JonAcuff"
replies.Hide_output = True
twint.run.Search(replies)
df = twint.storage.panda.Tweets_df

fetchedReplies = Counter(df['conversation_id'])
for tweet in Replies:
    print(tweet, "\t{}\t{}\t".format(Replies[tweet], fetchedReplies[tweet]))
