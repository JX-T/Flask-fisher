# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from sqlalchemy import Column, Integer, ForeignKey, String, Boolean, desc, func
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from app.spider.yushu_book import YuShuBook


class Wish(Base):
    # __tablename__ = 'wish'

    id = Column(Integer, primary_key=True)
    uid = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    isbn = Column(String(13), nullable=False)
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_wishes(cls, uid):
        wishes = cls.query.filter_by(uid=uid, launched=False).order_by(desc(cls.create_time)).all()
        return wishes

    @classmethod
    def get_gift_counts(cls, isbn_list):
        from app.models.gift import Gift
        count_list = db.session.query(func.count(Gift.id), Gift.isbn).filter(
            Gift.launched == False,
            Gift.isbn.in_(isbn_list),
            Gift.status == 1).group_by(
            Gift.isbn).all()
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first


if __name__ == '__main__':
    print(type(Wish))
    print(globals()['Wish'].code)

