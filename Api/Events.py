from Api.Feishu import feishuapi


class Events(feishuapi):

    def __init__(self, token):
        super().__init__(token)

    def get_events(self, calendar_id, event_id):
        date = {
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}',
            'method': 'get',
        }
        r = self.fs_request(**date)
        return r

    def get_eventsList(self, calendar_id, anchor_time: str = None, page_token: str = None, pake_size: int = None,
                       sync_token: str = None):
        date = {
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}/events',
            'method': 'get',
            'params': {
                'anchor_time': anchor_time,
                'page_token': page_token,
                'pake_size': pake_size,
                'sync_token': sync_token
            }
        }
        r = self.fs_request(**date)
        return r

    def create(self, calendar_id, **kwargs):
        date = {
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}/events',
            'method': 'post',
            'json': kwargs
        }
        r = self.fs_request(**date)
        return r

    def update(self, calendar_id, event_id, **kwargs):
        date = {
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}',
            'method': 'patch',
            'json': kwargs
        }
        r = self.fs_request(**date)
        return r

    def delete(self, calendar_id, event_id, need_notification: bool = False):
        date = {
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}/events/{event_id}',
            'method': 'delete',
            'json': {
                'need_notification': need_notification
            }
        }
        r = self.fs_request(**date)
        return r

    def search(self, calendar_id, query, user_id_type: str = None, page_token: str = None, pake_size: int = None,
               **kwargs):
        kwargs['query'] = query
        date = {
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}/events/search',
            'method': 'delete',
            'params': {
                'user_id_type': user_id_type,
                'page_token': page_token,
                'pake_size': pake_size
            },
            'json': kwargs
        }
        r = self.fs_request(**date)
        return r
