# -*- coding: utf8 -*-

import re
import time
import random
import requests
from datetime import datetime, timedelta

# 以下为需自行抓包数据
TIME = 5  # 单次上传阅读时间，默认为5分钟
LIMIT_TIME = 18  # 每日最大上传阅读时间，默认为18小时
DELAYSEC = 1  # 单次任务延时，默认为1秒


