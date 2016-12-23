from .request import req
from .parser import topic as parser


class Topic:

    def __init__(self, topic_id):
        self.id = topic_id

    @classmethod
    def root(cls):
        """The root topic."""
        return cls(19776749)

    def hierarchy(self):
        """Get the hierarchy of this topic."""
        url = '/topic/%d/organize' % self.id
        d = req.get(url)
        return parser.hierarchy(d)

    def followers(self, start='', offset=0):
        """Get followers of this topic.

        Args:
            start: Timestamp in seconds.
            offset: An integer.

        Returns:
            A list of users.
        """
        url = '/topic/%d/followers' % self.id
        data = {
            'start': start,
            'offset': offset,
            '_xsrf': req._xsrf
        }
        r = req.post(url, data=data)
        return parser.followers(r['msg'][1])

    def top_answers(self, page=1):
        """Get top answers of this topic.

        Args:
            page: The page number.

        Returns:
            A list of answers.
        """
        url = '/topic/%d/top-answers' % self.id
        params = {'page': page}
        d = req.get(url, params)
        return parser.answers(d)

    def hot_answers(self, offset=''):
        """Get hot answers of this topic.

        Args:
            offset: Answer score in float number.

        Returns:
            A list of answers.
        """
        url = '/topic/%d/hot' % self.id
        data = {
            'offset': offset,
            'start': 0,
            '_xsrf': req._xsrf
        }
        r = req.post(url, data=data)
        return parser.answers(r['msg'][1])

    def new_answers(self, offset=''):
        """Get newest answers of this topic.

        Args:
            offset: Answer score in float number.

        Returns:
            A list of answers.
        """
        url = '/topic/%d/newest' % self.id
        data = {
            'offset': offset,
            'start': 0,
            '_xsrf': req._xsrf
        }
        r = req.post(url, data=data)
        return parser.answers(r['msg'][1])

    def pending_question(self, page=1):
        """Get pending questions of this topic.

        For more information about what is a pending question, see:
        https://www.zhihu.com/question/40470324

        Args:
            page: The page number.

        Returns:
            A list of questions
        """
        url = '/topic/%d/questions' % self.id
        params = {'page': page}
        d = req.get(url, params)
        return parser.questions(d)

    def hot_pending_question(self, page=1):
        """Get hot pending questions of this topic.

        For more information about what is a pending question, see:
        https://www.zhihu.com/question/40470324

        Args:
            page: The page number.

        Returns:
            A list of questions
        """
        url = '/topic/%d/unanswered' % self.id
        params = {'page': page}
        d = req.get(url, params)
        return parser.questions(d)
