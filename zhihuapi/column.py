from .request import req
from .urls import column_url


class Column:

    def __init__(self, slug):
        self.slug = slug

    def info(self):
        """Get column information"""
        url = '%s/api/columns/%s' % (column_url, self.slug)
        return req.get(url)

    def pins(self):
        """Pin top posts."""
        url = '%s/api/columns/%s/pins' % (column_url, self.slug)
        return req.get(url)

    def posts(self, offset=0):
        """Posts in this column.

        Args:
            offset: An integer.

        Returns:
            A list of posts.
        """
        url = '%s/api/columns/%s/posts' % (column_url, self.slug)
        params = {
            'offset': offset,
            'limit': 20
        }
        return req.get(url, params)

    def authors(self):
        """Authors in this column."""
        url = '%s/api/columns/%s/authors' % (column_url, self.slug)
        return req.get(url)
