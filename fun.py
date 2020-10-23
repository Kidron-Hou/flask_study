#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : fun.py
# @Description: 学习flask功能
# @Time       : 2020-10-23 上午 9:46
# @Author     : Hou

from flask import Flask, render_template
from flask import url_for

app = Flask(__name__)

name = 'Kidron'
scriptures = [
    {'content': 'God saw all that he had made, and it was very good.', 'year': '2010'},
    {'content': 'Then you will know the truth, and the truth will set you free.', 'year': '2019'},
    {'content': 'Dear children, keep yourselves from idols.', 'year': '2020'},
]


@app.route('/word')
def hello_world():
    return '<h1>Hello Totoro!</h1><img src="http://helloflask.com/totoro.gif">'


@app.route('/user/<name>')
def create(name):
    return 'In the beginning God created the heavens and the earth.'


@app.route('/')
def index():
    return render_template('index.html', name=name, scriptures=scriptures)


if __name__ == '__main__':
    app.run(debug=True)  # 开发环境下不要使用