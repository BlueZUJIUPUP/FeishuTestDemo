# -*- coding: utf-8 -*-
# @File   : http_requests
# @Time   : 2021/8/23 11:45 
# @Author : BLUE_JUZIUPUP

import requests

from Api.log import log


class Http_requests:

    def request(self, method, url, **kwargs):
        log.debug(kwargs)
        r = requests.request(method, url, **kwargs)
        log.debug(r.text)
        return r.json()
