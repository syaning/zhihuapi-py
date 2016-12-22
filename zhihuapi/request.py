import requests
from pyquery import PyQuery as pq
from http import cookies

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
        self._raw = False

    def setCookie(self, cookie):
        c = cookies.SimpleCookie()
        c.load(cookie)
        if 'z_c0' not in c:
            raise Exception('Invalid cookie: '
                            'no authorization (z_c0) in cookie')
        if '_xsrf' not in c:
            raise Exception('Invalid cookie: no _xsrf in cookie')
        self.headers['Cookie'] = cookie.strip()
        self.headers['Authorization'] = 'Bearer %s' % c['z_c0'].value
        self._xsrf = c['_xsrf'].value

    def request(self, method, url, **kwargs):
        url = urls.full(url)
        r = requests.request(method, url, headers=self.headers, **kwargs)
        content_type = r.headers['content-type']
        if 'application/json' in content_type:
            return r.json()
        else:
            return pq(r.text)

    def get(self, url, params=None):
        return self.request('GET', url, params=params)

    def post(self, url, data=None, json=None):
        return self.request('POST', url, data=data, json=json)

    def delete(self, url):
        return self.request('DELETE', url)


req = Request()


def cookie(val):
    req.setCookie(val)


def raw(val):
    req._raw = val
