import os
import time

import pytest

from Api.Calendar import Calendar
from Api.Events import Events
from Api.Gettoken import Token


class TestEvents:

    def setup_class(self):
        token = Token().get_tenant_access_token()
        self.Events = Events(token)
        self.calendar = Calendar(token)
        data = {
            'summary': 'hogwarts_ck_18_001',
            'color': '16711680',
            'description': '',
            'permissions': 'public'
        }
        # 创建日历，并获取创建日历的id
        self.calendar_id = self.calendar.create(**data)['data']['calendar']['calendar_id']

    def teardown_class(self):
        self.calendar.delete(self.calendar_id)

    def setup(self):
        pass


    @pytest.mark.parametrize('name',['test001','test002'])
    def test_createEvents(self,name):
        json = {
            "summary": name,
            "description": "日程描述",
            "need_notification": False,
            "start_time": {
                "timestamp": str(int(time.time())),
            },
            "end_time": {
                "timestamp": str(int(time.time()) + 100000),
            },
        }
        self.Events.create(self.calendar_id, **json)

    def test_getEvents(self):
        json = {
            "summary": "summary_test01",
            "description": "description_test01",
            "need_notification": False,
            "start_time": {
                "timestamp": str(int(time.time())),
            },
            "end_time": {
                "timestamp": str(int(time.time()) + 100000),
            },
        }
        # 创建日程，并获取创建日程的id
        event_id = self.Events.create(self.calendar_id, **json)["data"]["event"]["event_id"]
        # 查询日程
        event = self.Events.get_events(self.calendar_id, event_id)
        # 判断查询出来的日程名字是否与创建日程的名字一致
        assert event["data"]["event"]["summary"] == 'summary_test01'

    def test_deleteEvents(self):

        json = {
            "summary": "summary_test01",
            "description": "description_test01",
            "need_notification": False,
            "start_time": {
                "timestamp": str(int(time.time())),
            },
            "end_time": {
                "timestamp": str(int(time.time()) + 100000),
            },
        }
        # 创建日程，并获取创建日程的id
        event_id = self.Events.create(self.calendar_id, **json)["data"]["event"]["event_id"]
        # 删除日程
        event = self.Events.delete(self.calendar_id, event_id)
        # 判断是否删除成功
        assert event['code'] == 0
        # 查询日程是否被删除
        event = self.Events.get_events(self.calendar_id, event_id)

    def test_get_list(self):
        self.test_createEvents("test01")
        eventslist = self.Events.get_eventsList(self.calendar_id)['data']['items']
        assert len(eventslist) == 1

    def test_update(self):
        json = {
            "summary": "summary_test01",
            "description": "description_test01",
            "need_notification": False,
            "start_time": {
                "timestamp": str(int(time.time())),
            },
            "end_time": {
                "timestamp": str(int(time.time()) + 100000),
            },
        }
        # 创建日程，并获取创建日程的id
        event_id = self.Events.create(self.calendar_id, **json)["data"]["event"]["event_id"]
        data={
            "summary": "summary_new_test01",
        }
        # 修改日程的标题为summary_new_test01
        self.Events.update(self.calendar_id,event_id,**data)
        # 查询该日历的日程的标题
        event = self.Events.get_events(self.calendar_id, event_id)
        # 判断查询出来的标题是否与修改的标题名称一致
        assert event["data"]["event"]["summary"] == 'summary_new_test01'



    def test_search(self):
        json = {
            "summary": 'summary_test01',
            "description": "description_test01",
            "need_notification": False,
            "start_time": {
                "timestamp": str(int(time.time())),
            },
            "end_time": {
                "timestamp": str(int(time.time()) + 100000),
            },
        }
        # 创建日程，并获取创建日程的id
        self.Events.create(self.calendar_id, **json)
        self.Events.search(self.calendar_id, 'summary_test01')

