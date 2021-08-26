# -*- coding: utf-8 -*-
# @File   : test_c
# @Time   : 2021/8/23 15:45 
# @Author : BLUE_JUZIUPUP
import pytest

from Api.Calendar import Calendar
from Api.Gettoken import Token


class TestCalendar:

    def setup_class(self):
        token = Token().get_tenant_access_token()
        self.calendar = Calendar(token)
        # self.calendar.create()

    def setup(self):
        self.calendar.delete_all()

    def teardown_class(self):
        pass

    def test_getCalendar(self):
        data = {
            'summary': 'hogwarts_ck_18_001',
            'color': '16711680',
            'description': '',
            'permissions': 'public'
        }
        c_calendar = self.calendar.create(**data)
        calendar_id = c_calendar['data']['calendar']['calendar_id']
        g_calendar = self.calendar.getCalendar(calendar_id)
        assert g_calendar['data']['summary'] == 'hogwarts_ck_18_001'

    # def test_getCalendar01(self):
    #     self.calendar.getCalendarList()
    #     calendar_id = 'feishu.cn_iUjqF3PvYMGbPp7sQ3Zzyc@group.calendar.feishu.cn'
    #     self.calendar.delete(calendar_id)
    #     self.calendar.getCalendar(calendar_id)

    def test_getCalendarlist(self):
        calendars = self.calendar.getCalendarList()
        assert len(calendars) == 1

    @pytest.mark.parametrize('name', ["hogwarts_ck_18_001", "hogwarts_ck_18_002"])
    def test_creat_calendar(self, name):
        data = {
            'summary': name,
            'color': '16711680',
            'description': '',
            'permissions': 'public'
        }
        self.calendar.create(**data)

    def test_delete_calendar(self):
        data = {
            'summary': 'hogwarts_ck_18_001',
            'color': '16711680',
            'description': '',
            'permissions': 'public'
        }
        c_calendar = self.calendar.create(**data)
        calendar_id = c_calendar['data']['calendar']['calendar_id']
        old_calendars = self.calendar.getCalendarList()
        self.calendar.delete(calendar_id)
        new_calendars = self.calendar.getCalendarList()
        print(f"old_calendars{len(old_calendars)},new_calendars{len(new_calendars)}")
        assert len(old_calendars) - 1 == len(new_calendars)

    def test_delete_allcalendar(self):
        self.calendar.delete_all()
        self.calendar.getCalendarList()

    def test_update(self):
        data = {
            'summary': 'hogwarts_ck_18_001',
            'color': '16711680',
            'description': '',
            'permissions': 'public'
        }
        c_calendar = self.calendar.create(**data)
        calendar_id = c_calendar['data']['calendar']['calendar_id']
        data = {
            "summary": "test_update",
            "description": "test_update",
            "permissions": "private",
            "color": -1,
            "summary_alias": "test_update"
        }
        self.calendar.update(calendar_id=calendar_id, **data)

    def test_search(self):
        data = {
            'summary': 'hogwarts_ck_18_001',
            'color': '16711680',
            'description': '',
            'permissions': 'public'
        }
        self.calendar.create(**data)
        self.calendar.search('hogwarts')

    def test_subscribe(self):
        data = {
            'summary': 'hogwarts_ck_18_001',
            'color': '16711680',
            'description': '',
            'permissions': 'public'
        }
        c_calendar = self.calendar.create(**data)
        calendar_id = c_calendar['data']['calendar']['calendar_id']
        print(calendar_id)
        self.calendar.subscribe(calendar_id)

    def test_unsubscribe(self):
        data = {
            'summary': 'hogwarts_ck_18_001',
            'color': '16711680',
            'description': '',
            'permissions': 'public'
        }
        c_calendar = self.calendar.create(**data)
        calendar_id = c_calendar['data']['calendar']['calendar_id']
        self.calendar.subscribe(calendar_id)
        self.calendar.unsubscribe(calendar_id)
