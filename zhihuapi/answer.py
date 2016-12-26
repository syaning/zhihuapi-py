import json

from .request import req
from .parser import answer as parser


class Answer(object):

    def __init__(self, answer_id):
        self.id = answer_id

    def voters(self, offset=0):
        """Get voters of this answer.

        Args:
            offset: An integer.

        Returns:
            A list of voters.
        """
        url = '/api/v4/answers/%d/voters' % self.id
        params = {
            'offset': offset,
            'limit': 20
        }
        data = req.get(url, params)
        return data if req._raw else parser.voters(data)

    def comments(self, offset=0):
        """Get comments of this answer.

        Args:
            offset: An integer.

        Returns:
            A list of comments.
        """
        url = '/api/v4/answers/%d/comments' % self.id
        params = {
            'offset': offset,
            'limit': 20,
            'order': 'normal',
            'status': 'open',
            'include': 'data[*].author,reply_to_author,content,vote_count'
        }
        data = req.get(url, params)
        return data if req._raw else parser.comments(data)

    @staticmethod
    def explore_day(offset=0):
        """Explore hot answers in this day.

        Args:
            offset: An integer.

        Returns:
            A list of answers.
        """
        return _explore(offset=offset, time_type='day')

    @staticmethod
    def explore_month(offset=0):
        """Explore hot answers in this month.

        Args:
            offset: An integer.

        Returns:
            A list of answers.
        """
        return _explore(offset=offset, time_type='month')


def _explore(offset, time_type):
    url = '/node/ExploreAnswerListV2'
    params = {
        'params': json.dumps({
            'offset': offset,
            'type': time_type
        })
    }
    d = req.get(url, params)
    return parser.explore(d)
