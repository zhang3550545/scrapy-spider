#!/usr/bin/env python
# encoding: utf-8

"""
__author__: Widsom Zhang
__time__: 2017/12/1 11:17
"""

from scrapy import Spider, Request, FormRequest


class GithubLoginSpider(Spider):
    name = "github"
    allow_domains = ['github.com']

    # post登入的必须要的头字段
    post_headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.75 Safari/537.36",
        "Referer": "https://github.com/",
    }

    def start_requests(self):
        """
        执行spider，开始请求
        :return: 返回一个Request对象，请求登录的页面
        """
        return [Request(url='https://github.com/login', meta={'cookiejar': 1}, callback=self.post_login)]

    def post_login(self, response):
        """
        登录的页面请求成功后，解析响应的页面，获取登录需要的<input>标签的信息
        :param response: 登录接口返回的页面
        :return:
        """
        # 解析GitHub登入上传必要的字段
        utf8 = response.xpath('//form//input[@name="utf8"]/@value').extract()[0]
        authenticity_token = response.xpath("//form//input[@name='authenticity_token']/@value").extract()[0]
        login = "xxxxxx@126.com"
        password = "xxxxxx"
        commit = response.xpath("//form//input[@name='commit']/@value").extract()[0]

        print("utf8: " + utf8)
        print("authenticity_token: " + authenticity_token)
        print("commit: " + commit)

        # 发送FormRequest表单请求
        return FormRequest.from_response(response=response,
                                         meta={'cookiejar': response.meta['cookiejar']},
                                         headers=self.post_headers,
                                         formdata={
                                             "utf8": utf8,
                                             "authenticity_token": authenticity_token,
                                             "login": login,
                                             "password": password,
                                             "commit": commit
                                         },
                                         callback=self.after_login)

    def after_login(self, response):
        """
        form表单请求成功后，请求登入我的页面
        :param response:
        :return: 返回一个响应
        """
        if response.status == 200:
            return Request("https://github.com/zhang3550545",
                           meta={'cookiejar': response.meta['cookiejar']},
                           callback=self.parse_page)

    def parse_page(self, response):
        """
        将响应的我的页面数据，写入文件
        :param response:
        :return:
        """
        if response.status == 200:
            with open('my_account.html', 'wb')as f:
                f.write(response.body)
