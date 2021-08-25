# -*- coding: utf-8 -*-
# @File   : test_demo
# @Time   : 2021/8/23 10:50 
# @Author : BLUE_JUZIUPUP
import os
import time

import requests


class Testdemo:
    def setup_class(self):
        self.app_access_token = 1
        self.app_secret ='dnst9iwMxaa8sz36LakB2gE3aHaYeEaA'
        self.app_ticket =1
        self.app_id = 'cli_a1861cddecf85013'


    def teardown_class(self):
        pass

    def test_01(self):
        timestamp = time.time()
        print(timestamp)
        print(int(timestamp))
        print(str(int(time.time())))
