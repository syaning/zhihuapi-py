from .request import req
from .parser import collection as parser


class Collection:

    def __init__(self, collection_id):
        self.id = collection_id

    def answers(self, page=1):
        """Get answers in this collection.

        Args:
            page: Page number.

        Returns:
            A list of answers.
        """
        url = '/collection/%d' % self.id
        params = {'page': page}
        d = req.get(url, params)
        return parser.answers(d)
