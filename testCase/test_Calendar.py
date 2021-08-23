# -*- coding: utf-8 -*-
# @File   : test_c
# @Time   : 2021/8/23 15:45 
# @Author : BLUE_JUZIUPUP


from Api.Calendar import Calendar
from Api.get_token import Token


class TestCalendar:

    def setup_class(self):
        token = Token().get_tenant_access_token()
        self.calendar = Calendar(token)
        # self.calendar.create()

    def teardown_class(self):
        pass

    def test_01(self):
        calendars =self.calendar.get_Calendar()
        assert len(calendars) == 1

    def test_02(self):
        c = self.calendar.create(
            'hogwarts_ck_18',
            color=16711680,
            description='',
            permissions='public'
        )