import sys
import aiohttp
import requests

class GG:
    def __init__(self, gg_token: str, bot_id: int, user_id: int):
        self.gg_token = gg_token
        self.bot_id = bot_id
        self.user_id = user_id
        self.agent = 'DBL-Python-Library (https://github.com/top-gg/DBL-Python-Library 0.4.0) Python/{0[0]}.{0[' '1]} aiohttp/{1}'.format(sys.version_info, aiohttp.__version__)

    def has_voted(self):
        headers = {
            'User-Agent': self.agent,
            'Content-Type': 'application/json',
            'Authorization': self.gg_token
        }
        params = {'userId': self.user_id}
        response = requests.get('https://top.gg/api/bots/{}/check'.format(self.bot_id), params=params, headers=headers)
        if response.json()['voted'] > 0:
            return True
        return False