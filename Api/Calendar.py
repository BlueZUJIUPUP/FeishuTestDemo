# -*- coding: utf-8 -*-
# @File   : Calendar
# @Time   : 2021/8/23 15:48 
# @Author : BLUE_JUZIUPUP
from Api.Feishu import feishuapi


class Calendar(feishuapi):

    def __init__(self, token, **kwargs):
        super().__init__(token)
        # self.token = token
        self.calendar_id = kwargs.get('calendar_id'),
        self.color = kwargs.get('color'),
        self.description = kwargs.get('description'),
        self.permissions = kwargs.get('permissions'),
        self.role = kwargs.get('role'),
        self.summary = kwargs.get('summary'),
        self.summary_alias = kwargs.get('summary_alias'),
        self.type = kwargs.get('type')

    def get_token(self):
        return self.token

    def get_Calendar(self, page_size=500, *args):
        data = {
            'url': 'https://open.feishu.cn/open-apis/calendar/v4/calendars',
            'method': 'get'
        }

        j = self.fs_request(**data)

        calendar_list: list[Calendar] = []
        for data in j['data']['calendar_list']:
            calendar_list.append(Calendar(token=self.token, **data))
        return calendar_list

    def update(self, calendar_id, **kwargs):
        data = {
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}',
            'method': 'patch',
            'json': {
                **kwargs
            }
        }
        r = self.fs_request(**data)
        return r

    def delete(self, id, **kwargs):
        pass

    def delete_all(self):
        pass

    def create(self,summary, **kwargs):
        url = 'https://open.feishu.cn/open-apis/calendar/v4/calendars'

        kwargs['summary'] = summary
        j = self.fs_request(
            url=url,
            method='post',
            json=kwargs
        )
        return j

    def search(self, query, page_token: str = None, page_size: int = None):
        data = {
            'url': 'https://open.feishu.cn/open-apis/calendar/v4/calendars/search',
            'method': 'post',
            'params': {
                'page_token': page_token,
                'page_size': page_size
            },
            'json': {
                'query': query
            }
        }
        r = self.fs_request(**data)

    def subscribe(self,calendar_id):
        data = {
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}/subscribe',
            'method': 'post',
        }
        r = self.fs_request(**data)
        return r

    def unsubscribe(self,calendar_id):
        data = {
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}/unsubscribe',
            'method': 'post',
        }
        r = self.fs_request(**data)
        return r

