# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
import json

from flask import flash, render_template
from flask_login import current_user

from app.forms.book import SearchForm
from app.models.gift import Gift
from app.models.wish import Wish
from app.view_models.book import BookViewModel, BookCollection
from app.view_models.trade import TradeInfo
from app.web import web
from flask.json import jsonify, request

from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook


@web.route('/book/search/')
def search():
    """
    q : 普通关键字  isbn
    page: 翻页
    :return:
    """
    # 获取请求参数
    # q = request.args['q']
    # page = request.args['page']

    # 将 flask 的不可变字典转换成常见的可变字典
    # a = request.args.to_dict()

    # 验证层-验证请求参数
    form = SearchForm(request.args)
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)

        # dict 序列化
        # API

        # python不能直接序列化对象

        # __dict__返回实例变量字典
        # books.__dict__
        result = json.dumps(books, default=lambda o: o.__dict__)

        # return jsonify(result)
        # return json.dumps(result), 200, {'content-type': 'application/json'}
    else:
        # return jsonify(form.errors)
        flash('搜索的关键字不符合要求，请重新输入关键字')

    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    has_in_gifts = False
    has_in_wishes = False

    # 取书籍详情数据
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)

    if current_user.is_authenticated:
        if Gift.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_gifts = True
        if Wish.query.filter_by(uid=current_user.id, isbn=isbn, launched=False).first():
            has_in_wishes = True

    trade_gifts = Gift.query.filter_by(isbn=isbn, launched=False).all()
    trade_wishes = Wish.query.filter_by(isbn=isbn, launched=False).all()

    trade_gifts_model = TradeInfo(trade_gifts)
    trade_wishes_model = TradeInfo(trade_wishes)

    return render_template('book_detail.html', book=book,
                           wishes=trade_wishes_model, gifts=trade_gifts_model,
                           has_in_gifts=has_in_gifts, has_in_wishes=has_in_wishes)

