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
    """This class is just a wrapper for requests package."""

    def __init__(self):
        """Initialize a request instance.

        `_raw` is a flag to show whether or not return the raw response body.
        This is only available for zhihu v4 api that returns a JSON format
        response body.
        """
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


# The global request
req = Request()


def cookie(val):
    """Set cookie for global request.

    The cookie value must include `z_c0` (authorization token) and `_xsrf`.

    Args:
        val: Cookie string.
    """
    req.setCookie(val)


def raw(val):
    """Set `_raw` for global request.

    Whether or not return raw response body. This is only available for
    zhihu v4 apis which return JSON format responses.

    Args:
        val: A boolean value.
    """
    req._raw = val
