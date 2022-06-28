import json
import requests


def get_token():
    post_url = 'https://bojianger.com/user/api/user/login.do'
    headers = {
        'Content-Type': 'application/json',
    }
    payload = {
        'phone': '13798122637',
        'password': 'realmadrid'
    }
    r = requests.post(
        url=post_url,
        data=json.dumps(payload),
        headers=headers
    )
    if r.status_code == 200:
        print('Succeed to get token.')
        token = json.loads(r.text)['data']
        return token
    else:
        print('Failed to get token')


if __name__ == '__main__':
    get_token()
