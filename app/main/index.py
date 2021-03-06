#!/usr/bin/python3
# @Time    : 2019-07-05
# @Author  : Kevin Kong (kfx2007@163.com)

from . import bp_main
from flask_login import login_required, current_user
from utils.view_util import render_template
from flask import redirect, url_for, request
from .views import common_list, common_edit
from app.model.menu import Menu
from .forms import MenuForm

# 根目录跳转
@bp_main.route('/', methods=['GET'])
@login_required
def root():
    return redirect(url_for('main.index'))


@bp_main.route('/menulist', methods=["GET"])
@login_required
def menulist():
    return common_list(Menu, "menu/menulist.html")


@bp_main.route('/menuedit', methods=["GET","POST"])
@login_required
def menuedit():
    return common_edit(Menu, MenuForm(), "menu/menuedit.html")

# 首页
@bp_main.route('/index', methods=['GET'])
@login_required
def index():
    return render_template('index.html', current_user=current_user)


@bp_main.route('/term')
@login_required
def get_term():
    id = request.args.get("id")
    return render_template("term.html", server_id=id)
