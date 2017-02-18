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
        return self._answers('default', offset)

    def answers_bypage(self, offset=0):
        """Get answers by page (or created time).

        Args:
            offset: An integer.

        Returns:
            A list of answers.
        """
        return self._answers('created', offset)

    def _answers(self, sort_by='default', offset=0):
        """Get answers."""
        url = '/api/v4/questions/%d/answers' % self.id
        params = {
            'sort_by': sort_by,
            'offset': offset,
            'limit': 20,
            'include': ','.join([
                'data[*].is_normal',
                'is_sticky',
                'collapsed_by',
                'suggest_edit',
                'comment_count',
                'collapsed_counts',
                'reviewing_comments_count',
                'content',
                'voteup_count',
                'reshipment_settings',
                'comment_permission',
                'mark_infos',
                'created_time',
                'updated_time'
            ])
        }
        data = req.get(url, params=params)
        return data if req._raw else parser.answers(data)

    def detail(self):
        """Get detail information of this question.

        Returns:
            Detailed question information.
        """
        url = '/api/v4/questions/%d' % self.id
        data = req.get(url)
        return parser.detail(data)

    def followers(self, offset=0):
        """Get users that followed this question.

        Args:
            offset: An integer.

        Returns:
            A list of users.
        """
        url = '/api/v4/questions/%d/followers' % self.id
        params = {
            'limit': 20,
            'offset': offset
        }
        data = req.get(url, params)
        return data if req._raw else parser.followers(data)
