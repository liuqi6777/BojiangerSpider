import itertools

import pandas as pd

from spider import *


TOKEN = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxMzc5ODEyMjYzNyIsImlhdCI6MTY1MDYzOTU5OCwiZXhwIjoxNjUxMjQ' \
        '0Mzk4fQ.Xoe--WFwF2UnZZ3F-mHY_sMo2QR4bHGBRytEQUpaY57ZFhZ27MQIwo3-6kgQ4O5fI4qH_6JoILh9fTvSjih7MQ'


def get_audience_detail_by_day(uid, start_date, end_date):
    spider = AudienceDetailSpider(
        url='https://bojianger.com/data/api/auth/audience_detail.do',
    )
    dates = [pd.Period.strftime(date, '%Y-%m-%d') for date in pd.period_range(start_date, end_date, freq='D')]
    queries = [
        {
            'uid': str(uid),
            'date': date,
            'orderBy': 'update_time',
            'order': 'date_desc',
            'pageNum': '1',
            'pageSize': '7',
        }
        for date in dates
    ]
    items = itertools.chain.from_iterable([spider(**query) for query in queries])
    return items


def get_audience_detail_by_month(uid, start_month, end_month):
    spider = AudienceDetailSpider(
        url='https://bojianger.com/data/api/auth/audience_detail_month.do'
    )
    months = [pd.Period.strftime(month, '%Y-%m') for month in pd.period_range(start_month, end_month, freq='M')]
    queries = [
        {
            'uid': str(uid),
            'month': month,
            'orderBy': 'update_time',
            'order': 'date_desc',
            'pageNum': '1',
            'pageSize': '7',
        }
        for month in months
    ]
    items = itertools.chain.from_iterable([spider(**query) for query in queries])
    return items


def get_audience_list_by_month(start_month, end_month, max_page=10):
    spider = AudienceSpider(
        url='https://bojianger.com/data/api/common/audience_list_month.do',
    )
    months = [pd.Period.strftime(month, '%Y-%m') for month in pd.period_range(start_month, end_month, freq='M')]
    pages = [str(i) for i in range(1, max_page + 1)]
    queries = [
        {
            'month': m,
            'orderBy': 'yc_gift_value',
            'getType': 'all',
            'pageNum': p,
            'pageSize': '20',
        }
        for m in months for p in pages
    ]
    items = itertools.chain.from_iterable([spider(**query) for query in queries])
    return items
