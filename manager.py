# -*- coding: UTF-8 -*-
import json
import re
import sys
import os
sys.path.insert(0, os.getcwd())

from flask import Flask, render_template, redirect, request

app = Flask(__name__)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)
