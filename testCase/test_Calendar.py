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

    def teardown_class(self):
        pass

    def test_list_calendar(self):
        calendars = self.calendar.get_Calendar()
        assert len(calendars) == 1

    @pytest.mark.parametrize('name', ["hogwarts_ck_18_001", "hogwarts_ck_18_002"])
    def test_creat_calendar(self, name):
        c = self.calendar.create(
            name,
            color=16711680,
            description='',
            permissions='public'
        )

    def test_delete_calendar(self):
        old_calendars = self.calendar.get_Calendar()
        calendar_id = old_calendars[1].calendar_id[0]
        self.calendar.delete(calendar_id)
        new_calendars = self.calendar.get_Calendar()
        assert len(new_calendars) + 1 == len(old_calendars)

    def test_delete_allcalendar(self):
        self.calendar.delete_all()
        self.calendar.get_Calendar()
