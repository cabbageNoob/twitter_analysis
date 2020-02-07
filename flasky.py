'''
@Descripttion: 
@version: 
@Author: Da Chuang
@Date: 2020-01-05 16:15:39
@LastEditors  : Da Chuang
@LastEditTime : 2020-01-05 17:17:58
'''
import os
from app import create_app

app=create_app(os.getenv('FLASK_CONFIG') or 'default')

if __name__=='__main__':
    app.run(host='127.0.0.1',debug=True,port=8080)