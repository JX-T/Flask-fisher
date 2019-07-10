# -*- coding: utf-8 -*-
# __author__ = 'Miracle'


def is_isbn_or_key(word):
    """

    :param word:
    :return:
    """
    # isbn13 13个0到9的数字
    # isbn10 10个0到9的数字，含有一些‘-’
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    # 多条件判断语句，1、把可能为假的条件放在前面    2、把耗时的条件放在后面
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key


def get_isbn(data_dict):
    isbn = data_dict.get('isbn')
    if not isbn:
        isbn = data_dict.get('isbn13')
        if not isbn:
            isbn = data_dict.get('isbn10')
    return isbn

