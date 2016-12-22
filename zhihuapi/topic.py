from .request import req


class Topic:

    def __init__(self, topic_id):
        self.id = topic_id

    @classmethod
    def root(cls):
        """The root topic."""
        return cls(19776749)
