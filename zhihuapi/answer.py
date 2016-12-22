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
        url = '/api/v4/answers/%s/voters' % self.id
        params = {
            'offset': offset,
            'limit': 20
        }
        data = req.get(url, params)
        return data if req._raw else parser.voters(data)
