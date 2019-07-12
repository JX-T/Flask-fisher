# -*- coding: utf-8 -*-
# __author__ = 'Miracle'

# -*- coding: utf-8 -*-
__author__ = 'bliss'

from enum import Enum


class PendingStatus(Enum):
    """交易状态"""
    Waiting = 1
    Success = 2
    Reject = 3
    Redraw = 4
    # gifter_redraw = 5

    @classmethod
    def pending_str(cls, status, you_are):
        key_map = {
            cls.Waiting: {
                'requester': '等待对方邮寄',
                'gifter': '等待你邮寄'
            },
            cls.Reject: {
                'requester': '对方已拒绝',
                'gifter': '你已拒绝'
            },
            cls.Redraw: {
                'requester': '你已撤销',
                'gifter': '对方已撤销'
            },
            cls.Success: {
                'requester': '对方已邮寄',
                'gifter': '你已邮寄，交易完成'
            }
        }
        return key_map[status][you_are]


class GiftStatus(Enum):
    waiting = 0
    success = 1
    redraw = 2
