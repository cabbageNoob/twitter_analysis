'''
@Descripttion: 
@version: 
@Author: Da Chuang
@Date: 2019-12-30 22:23:16
@LastEditors  : Da Chuang
@LastEditTime : 2019-12-30 22:32:00
'''
import twint
from collections import Counter

'''Twint Config'''
c = twint.Config()
c.Proxy_host = '127.0.0.1'
c.Proxy_port = '1080'
c.Proxy_type = 'http'

mothers = twint.Config()
mothers.Proxy_host = '127.0.0.1'
mothers.Proxy_port = '1080'
mothers.Proxy_type = 'http'
mothers.Username = "realDonaldTrump"
# mothers.Since = "2019-08-04"
# mothers.Until = "2019-09-08"
# mothers.Lang = 'en'
# mothers.Pandas = True
mothers.Store_csv = True
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
replies.To = "realDonaldTrump"
# replies.Hide_output = True
twint.run.Search(replies)
df = twint.storage.panda.Tweets_df

fetchedReplies = Counter(df['conversation_id'])
for tweet in Replies:
    print(tweet, "\t{}\t{}\t".format(Replies[tweet], fetchedReplies[tweet]))
