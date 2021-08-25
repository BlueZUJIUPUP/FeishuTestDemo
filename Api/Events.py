from Api.Feishu import feishuapi


class Events(feishuapi):

    def __init__(self, token):
        super().__init__(token)

    def get_events(self):
        pass

    def create(self, calendar_id,**kwargs):
        date = {
            'url': f'https://open.feishu.cn/open-apis/calendar/v4/calendars/{calendar_id}/events',
            'method': 'post',
            'json': **kwargs
        }
        r = self.fs_request(**date)

    def update(self):
        pass

    def delete(self):
        pass
