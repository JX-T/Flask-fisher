# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from flask import current_app
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook


class Gift(Base):
    # __tablename__ = 'gift'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def recent(cls):
        recent_gift = cls.query.filter_by(
            launched=False).group_by(
            cls.isbn).order_by(
            desc(cls.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).distinct().all()

        return recent_gift

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = cls.query.filter_by(uid=uid, launched=False).order_by(desc(cls.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        from app.models.wish import Wish
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(
            Wish.launched == False,
            Wish.isbn.in_(isbn_list),
            Wish.status == 1).group_by(
            Wish.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list
