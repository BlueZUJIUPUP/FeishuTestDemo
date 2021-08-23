# -*- coding: utf-8 -*-
# @File   : http_requests
# @Time   : 2021/8/23 11:45 
# @Author : BLUE_JUZIUPUP
import json
import requests
from Api.Log import log


class Http_Api:

    def request(self, method, url, **kwargs):
        if url or 'url' in kwargs:
            return self.http_request(method, url, **kwargs)

        if 'rpc' == kwargs.get("protocol"):
            return self.rpc_request(kwargs)

    def http_request(self, method, url, **kwargs):
        log.debug(kwargs)
        r = requests.request(method, url, **kwargs)
        # todo: 后面换成logging
        log.debug(json.dumps(r.json(), indent=2, ensure_ascii=False))
        return r

    def rpc_request(self, kwargs):
        pass

    def tcp_request(self):
        pass
