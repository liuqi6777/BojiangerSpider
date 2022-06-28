urls = [
    'https://bojianger.com/anchor-list-pro.html',
    'https://bojianger.com/anchor-list-pro-month.html',

    # 水友日志（水友列表）
    'https://bojianger.com/data/api/common/audience_list.do',
    # 水友月报（水友列表）
    'https://bojianger.com/data/api/common/audience_list_month.do',
    # 水友日数据
    'https://bojianger.com/data/api/auth/audience_detail.do',
    # 水友月数据
    'https://bojianger.com/data/api/auth/audience_detail_month.do',
    # 水友日弹幕
    'https://bojianger.com/data/api/auth/audience_detail_danmu.do',
    # 水友月弹幕
    'https://bojianger.com/data/api/auth/audience_detail_danmu_month.do',
    # 水友月活跃日期
    'https://bojianger.com/data/api/auth/audience_detail_day_month.do'
]

audience_list_payload = {
    'date': 'yyyy-MM-dd',
    'keyword': '',
    'orderBy': ['yc_gift_value', 'danmu_count', 'level'],
    'getType': 'all',
    'pageNum': '1',
    'pageSize': '20',
}

audience_list_month_payload = {
    'month': 'yyyy-MM',
    'keyword': '',
    'orderBy': ['yc_gift_value', 'danmu_count', 'level'],
    'getType': 'all',
    'pageNum': '1',
    'pageSize': '20',
}

audience_detail_payload = {
    'uid': '000000000',
    'date': 'yyyy-MM-dd',
    'keyword': '',
    'orderBy': 'update_time',
    'order': 'date_desc',
    'getType': 'all',
    'pageNum': '1',
    'pageSize': '20',
}

audience_detail_month_payload = {
    'uid': '00000000',
    'month': 'yyyy-MM',
    'keyword': '',
    'orderBy': 'update_time',
    'order': 'date_desc',
    'getType': 'all',
    'pageNum': '1',
    'pageSize': '20',
}

audience_detail_danmu_payload = {
    'date': 'yyyy-MM-dd',
    'rid': '0000000',  # 主播id
    'uid': '000000000',
    'order': '-1',  # 倒序
    'time': '-1',
    'duration': '0+~24',
    'pageNum': '1',
    'pageSize': '20',
}

audience_detail_danmu_month_payload = {
    'month': 'yyyy-MM',
    'rid': '0000000',  # 主播id
    'uid': '000000000',
    'order': '-1',  # 倒序
    'pageNum': '1',
    'pageSize': '20',
}

audience_detail_day_month_payload = {
    'uid': '000000000',
    'month': 'yyyy-MM',
    'keyword': '',
    'orderBy': 'update_time',
    'order': 'date_desc',
    'pageNum': '1',
    'pageSize': '31',
}
