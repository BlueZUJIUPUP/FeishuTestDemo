# -*- coding: utf-8 -*-
# @File   : test_demo
# @Time   : 2021/8/23 10:50 
# @Author : BLUE_JUZIUPUP


import requests


class Testdemo:
    def setup_class(self):
        self.app_access_token = 1
        self.app_secret ='dnst9iwMxaa8sz36LakB2gE3aHaYeEaA'
        self.app_ticket =1
        self.app_id = 'cli_a1861cddecf85013'


    def teardown_class(self):
        pass

    def test_get_app_access_token(self):
        data = {
            'url': 'https://open.feishu.cn/open-apis/auth/v3/app_access_token',
            'method': 'post',
            'data': {
                'app_id' : self.app_id,
                'app_secret': self.app_secret,
                'app_ticket' : self.app_ticket
            }
        }
        r = requests.request(**data)
        print(r.text)

    def test_get_tenant_access_token(self):
        data = {
            'url': 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal',
            'method': 'post',
            'json': {
                'app_id' : self.app_id,
                'app_secret': self.app_secret
            }
        }
        r = requests.request(**data)
        print(r.text)

        pass
