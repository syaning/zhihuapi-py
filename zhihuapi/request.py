import requests

from . import urls


user_agent = (
    'Mozilla/5.0 (Windows NT 10.0; WOW64) '
    'AppleWebKit/537.36 (KHTML, like Gecko) '
    'Chrome/55.0.2883.87 Safari/537.36'
)


class Request(object):

    def __init__(self):
        self.headers = {
            'Cookie': '',
            'Authorization': '',
            'Referer': urls.baseurl,
            'User-Agent': user_agent
        }
        self._xsrf = ''

    def request(self, method, url, **kwargs):
        url = urls.full(url)
        return requests.request(method, url, headers=self.headers, **kwargs)

    def get(self, url, params=None):
        return self.request('GET', url, params=params)

    def post(self, url, data):
        return self.request('POST', url, json=data)

    def post_form(self, url, data):
        return self.request('POST', url, data=data)

    def delete(self, url):
        return self.request('DELETE', url)
