from .request import req


class User(object):

    def __init__(self, url_token):
        self.url_token = url_token

    def profile(self):
        url = '/people/%s/collections' % self.url_token
        return req.get(url)

    def questions(self, offset=0):
        url = '/api/v4/members/%s/questions' % self.url_token
        params = {
            'offset': offset,
            'limit': 20,
            'include': ','.join([
                'data[*].created',
                'follower_count',
                'answer_count'
            ])
        }
        r = req.get(url, params)
        return r['data']
