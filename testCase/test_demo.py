# -*- coding: utf-8 -*-
# @File   : test_demo
# @Time   : 2021/8/23 10:50 
# @Author : BLUE_JUZIUPUP


import requests


class Testdemo:
    def setup_class(self):
        self.app_access_token = 1
        pass

    def teardown_class(self):
        pass

    def test_get_tenant_access_token(self):
        data = {
            'url': 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token',
            'method': 'post',
            'data': {
                    'app_access_token': self.app_access_token
            }
        }
        r = requests.request(**data)
        print(r.text)

        pass
