# -*- coding: utf-8 -*-
# @File   : feishu
# @Time   : 2021/8/23 14:55 
# @Author : BLUE_JUZIUPUP
from Api.http_api import Http_Api
from Api.log import log


class feishuapi(Http_Api):

    def __init__(self, token):
        self.token = token

    def fs_request(self, method, url, **kwargs):

        if 'headers' in kwargs:
            kwargs['headers']['Authorization'] = f'Bearer {self.token}'
        else:
            kwargs['headers'] = {'Authorization': f'Bearer {self.token}'}
        log.debug(kwargs)
        r = self.request(method, url, **kwargs)
        return r
