import json
import time
import random
import requests

from typing import Generator

from data import JsonLoader
from login import get_token


class Spider:
    """
    base class
    """

    def __init__(self, url: str, token: str = None) -> None:
        self.headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Content-Type': 'application/json; charset=utf-8',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/100.0.4896.75 Safari/537.36 Edg/100.0.1185.39',
        }

        self.url = url

        if token is not None:
            self.token = token
        else:
            self.token = get_token()
        self.headers['token'] = self.token

    def parse(self, **kwargs) -> Generator:
        raise NotImplemented

    def _parse_queries(self, **kwargs) -> str:
        if len(kwargs) > 0:
            queries = '&'.join([key + '=' + value for key, value in kwargs.items()])
            url = self.url + '?' + queries
        else:
            url = self.url
        return url

    def __call__(self, **kwargs) -> Generator:
        return self.parse(**kwargs)


class AudienceSpider(Spider):
    def __init__(self, url: str, token: str = None) -> None:
        super(AudienceSpider, self).__init__(url, token)

    def parse(self, **kwargs) -> Generator:
        time.sleep(1)
        url = self._parse_queries(**kwargs)
        r = requests.get(
            url=url,
            headers=self.headers,
            verify=False
        )
        json_data = JsonLoader(json.loads(r.text))
        item = dict()
        print('Crawl audience list from {}'.format(url))
        for audience_data in json_data.data.rows:
            item['month'] = audience_data.month
            item['uid'] = audience_data.uid
            item['audience_name'] = audience_data.audience_name
            item['yc_gift_value'] = audience_data.yc_gift_value
            yield item


class AudienceDetailSpider(Spider):
    def __init__(self, url: str, token: str = None) -> None:
        super(AudienceDetailSpider, self).__init__(url, token)

    def parse(self, **kwargs) -> Generator:
        time.sleep(random.random() * 2)
        url = self._parse_queries(**kwargs)
        r = requests.get(
            url=url,
            headers=self.headers,
        )
        # print(json.loads(r.text))
        try:
            item = json.loads(r.text)['data']
            print('Crawl audience detail -- uid: {} name: {}'.format(
                item['uid'], item['name']))
        except KeyError:
            item = {}
        yield item
