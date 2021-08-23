# -*- coding: utf-8 -*-
# @File   : get_token
# @Time   : 2021/8/23 11:43 
# @Author : BLUE_JUZIUPUP
from Api.http_api import Http_Api


class Token(Http_Api):
    app_id = 'cli_a1861cddecf85013'
    app_secret = 'dnst9iwMxaa8sz36LakB2gE3aHaYeEaA'
    app_ticket = 1

    def get_app_access_token(self):
        data = {
            'url': 'https://open.feishu.cn/open-apis/auth/v3/app_access_token',
            'method': 'post',
            'data': {
                'app_id': self.app_id,
                'app_secret': self.app_secret,
                'app_ticket': self.app_ticket
            }
        }
        r = self.request(**data)
        print(r.text)

    def get_tenant_access_token(self):
        data = {
            'url': 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal',
            'method': 'post',
            'json': {
                'app_id': self.app_id,
                'app_secret': self.app_secret
            }
        }
        r = self.request(**data)
        return r['tenant_access_token']

if __name__ == '__main__':
    token = Token()
    token.get_tenant_access_token()