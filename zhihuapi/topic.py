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
        url = '/topic/%s/organize' % self.id
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
        url = '/topic/%s/followers' % self.id
        data = {
            'start': start,
            'offset': offset,
            '_xsrf': req._xsrf
        }
        r = req.post(url, data=data)
        return parser.followers(r['msg'][1])
