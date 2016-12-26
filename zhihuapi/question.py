import json

from .request import req
from .parser import question as parser


class Question:

    def __init__(self, question_id):
        self.id = question_id

    def answers_byvote(self, offset=0):
        """Get answers by voteup weights.

        Args:
            offset: An integer.

        Returns:
            A list of answers.
        """
        url = '/node/QuestionAnswerListV2'
        data = {
            'method': 'next',
            'params': json.dumps({
                'url_token': self.id,
                'pagesize': 20,
                'offset': offset
            }),
            '_xsrf': req._xsrf
        }
        r = req.post(url, data=data)
        return parser.answers_byvote(r['msg'])

    def answers_bypage(self, page=1):
        """Get answers by page (or created time).

        Args:
            page: Page number.

        Returns:
            A list of answers.
        """
        url = '/question/%d' % self.id
        params = {
            'page': page,
            'sort': 'created'
        }
        d = req.get(url, params)
        return parser.answers_bypage(d)

    def detail(self):
        """Get detail information of this question.

        Returns:
            Detailed question information.
        """
        url = '/question/%d' % self.id
        d = req.get(url)
        return parser.detail(d)

    def followers(self, offset=0):
        """Get users that followed this question.

        Args:
            offset: An integer.

        Returns:
            A list of users.
        """
        url = '/question/%d/followers' % self.id
        data = {
            'offset': offset,
            'start': 0,
            '_xsrf': req._xsrf
        }
        r = req.post(url, data=data)
        return parser.followers(r['msg'][1])
