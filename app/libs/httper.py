# -*- coding: utf-8 -*-
# __author__ = 'Miracle'


import requests


class HTTP(object):
    @staticmethod
    def get(url, return_json=True):
        r = requests.get(url)
        # restful
        # json
        if r.status_code != 200:
            return {} if return_json else ""
        return r.json() if return_json else r.text


