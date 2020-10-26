#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @File       : fun.py
# @Description: 学习flask功能
# @Time       : 2020-10-23 上午 9:46
# @Author     : Hou

import os
import sys
import click
from flask import Flask, render_template
from flask import url_for
from flask_sqlalchemy import SQLAlchemy


# 配置数据库路径
WIN = sys.platform.startswith('win')
if WIN:
    prefix = 'sqlite:///'
else:
    prefix = 'sqlite:////'

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = prefix + os.path.join(app.root_path, 'data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # 关闭对模型修改的监控
db = SQLAlchemy(app)


# 构建数据
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))


class Scripture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lection = db.Column(db.String(100))
    year = db.Column(db.String(4))


@app.cli.command()
def forge():
    db.create_all()

    name = 'Kidron'
    scriptures = [
        {'content': 'God saw all that he had made, and it was very good.', 'year': '2010'},
        {'content': 'Then you will know the truth, and the truth will set you free.', 'year': '2019'},
        {'content': 'Dear children, keep yourselves from idols.', 'year': '2020'},
    ]
    user = User(name=name)
    db.session.add(user)
    for s in scriptures:
        scripture = Scripture(lection=s['content'],year=s['year'])
        db.session.add(scripture)
    db.session.commit()
    click.echo('Done')



@app.route('/user/<name>')
def create(name):
    return 'In the beginning God created the heavens and the earth.'


@app.route('/')
def index():
    user = User.query.first()
    scriptures = Scripture.query.all()
    return render_template('index.html', user=user, scriptures=scriptures)


if __name__ == '__main__':
    app.run(debug=True)  # 开发环境下不要使用