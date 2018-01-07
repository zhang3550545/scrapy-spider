# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html
import random
from zhongyuan_data import settings


class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        user_agent = random.choice(settings.USER_AGENTS)
        request.headers.setdefault(b'User-Agent', user_agent)
