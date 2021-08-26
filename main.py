# -*- coding: utf-8 -*-
# @File   : mian
# @Time   : 2021/8/26 9:24 
# @Author : BLUE_JUZIUPUP
import os

import pytest



if __name__ == '__main__':
    pytest.main([])
    os.system("allure generate ./report/result/ -o ./report/html --clean")
