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
