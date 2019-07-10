# -*- coding: utf-8 -*-
# __author__ = 'Miracle'
from app.view_models.book import BookViewModel


class MyWishes(object):
    def __init__(self, wishes_of_mine, gifts_count_list):
        self.wishes = []
        self.__wishes_of_mine = wishes_of_mine
        self.__gifts_count_list = gifts_count_list

        self.wishes = self.__parse()

    def __parse(self):
        temp_wishes = []
        for wish in self.__wishes_of_mine:
            my_wish = self.__matching(wish)
            temp_wishes.append(my_wish)
        return temp_wishes

    def __matching(self, wish):
        for gift_count in self.__gifts_count_list:
            if wish.isbn == gift_count['isbn']:
                count = gift_count['count']
                r = {
                    'wishes_count': count,
                    'book': BookViewModel(wish.book),
                    'id': wish.id
                }
                return r

