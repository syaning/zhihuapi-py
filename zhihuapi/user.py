from .request import req
from .parser import user as parser


class User(object):

    def __init__(self, url_token):
        self.url_token = url_token

    def profile(self):
        """Get profile of this user.
        """
        url = '/api/v4/members/%s' % self.url_token
        data = req.get(url)
        return data if req._raw else parser.profile(data)

    def detail(self):
        """Get detailed profile of this user.
        """
        url = '/people/%s/collections' % self.url_token
        d = req.get(url)
        return parser.detail(d, self.url_token)

    def activities(self, after_id=None, before_id=None):
        """Get this user's activities.

        Args:
            after_id: The upper bound of the activity id.
            before_id: The lower bound of the activity id.

        Returns:
            A list of activities.
        """
        url = '/api/v4/members/%s/activities' % self.url_token
        params = {
            'limit': 5,
            'include': ';'.join([
                ','.join([
                    'data[?(target.type=answer)].target.is_normal',
                    'suggest_edit',
                    'content',
                    'voteup_count',
                    'comment_count',
                    'collapsed_counts',
                    'reviewing_comments_count',
                    'mark_infos',
                    'created_time',
                    'updated_time'
                ]),
                'data[?(target.type=answer)].target.badge[?(type=best_answerer)].topics',
                ','.join([
                    'data[?(target.type=article)].target.column',
                    'content',
                    'voteup_count',
                    'comment_count',
                    'collapsed_counts',
                    'reviewing_comments_count',
                    'comment_permission',
                    'created',
                    'updated',
                    'upvoted_followees',
                    'voting'
                ]),
                ','.join([
                    'data[?(target.type=column)].target.title',
                    'intro',
                    'description',
                    'articles_count',
                    'followers'
                ]),
                'data[?(target.type=topic)].target.introduction',
                'data[?(verb=MEMBER_COLLECT_ANSWER)].extra_object',
                'data[?(verb=MEMBER_COLLECT_ARTICLE)].extra_object'
            ])
        }
        if after_id:
            params['after_id'] = after_id
        if before_id:
            params['before_id'] = before_id
        data = req.get(url, params)
        return data if req._raw else parser.activities(data)

    def questions(self, offset=0):
        """Get questions that this user asked.

        Args:
            offset: An integer.

        Returns:
            A list of questions.
        """
        url = '/api/v4/members/%s/questions' % self.url_token
        params = {
            'offset': offset,
            'limit': 20,
            'include': ','.join([
                'data[*].created',
                'follower_count',
                'answer_count'
            ])
        }
        data = req.get(url, params)
        return data if req._raw else parser.questions(data)

    def answers(self, offset=0):
        """Get answers that this user answered.

        Args:
            offset: An integer.

        Returns:
            A list of answers.
        """
        url = '/api/v4/members/%s/answers' % self.url_token
        params = {
            'offset': offset,
            'limit': 20,
            'sort_by': 'cereated',
            'include': ','.join([
                'data[*].is_normal',
                'comment_count',
                'collapsed_counts',
                'reviewing_comments_count',
                'content',
                'voteup_count',
                'reshipment_settings',
                'mark_infos',
                'created_time',
                'updated_time'
            ])
        }
        data = req.get(url, params)
        return data if req._raw else parser.answers(data)

    def articles(self, offset=0):
        """Get atricles that this user post.

        Args:
            offset: An integer.

        Returns:
            A list of articles.
        """
        url = '/api/v4/members/%s/articles' % self.url_token
        params = {
            'offset': offset,
            'limit': 20,
            'sort_by': 'created',
            'include': ','.join([
                'data[*].comment_count',
                'collapsed_counts',
                'reviewing_comments_count',
                'content',
                'voteup_count',
                'created',
                'updated'
            ])
        }
        data = req.get(url, params)
        return data if req._raw else parser.articles(data)

    def collections(self, offset=0):
        """Get collections owned by this user.

        Args:
            offset: An integer.

        Returns:
            A list of collections.
        """
        url = '/api/v4/members/%s/favlists' % self.url_token
        params = {
            'offset': offset,
            'limit': 20,
            'include': ','.join([
                'data[*].updated_time',
                'follower_count',
                'answer_count',
                'is_public'
            ])
        }
        data = req.get(url, params)
        return data if req._raw else parser.collections(data)

    def followers(self, offset=0):
        """Get followers.

        Args:
            offset: An integer.

        Returns:
            A list of users.
        """
        url = '/api/v4/members/%s/followers' % self.url_token
        params = {
            'offset': offset,
            'limit': 20
        }
        data = req.get(url, params)
        return data if req._raw else parser.follows(data)

    def followees(self, offset=0):
        """Get followees.

        Args:
            offset: An integer.

        Returns:
            A list of users.
        """
        url = '/api/v4/members/%s/followees' % self.url_token
        params = {
            'offset': offset,
            'limit': 20
        }
        data = req.get(url, params)
        return data if req._raw else parser.follows(data)

    def columns(self, offset=0):
        """Get columns owned by this user and its contributions.

        Args:
            offset: An integer.

        Returns:
            A list of columns and contributions.
        """
        url = '/api/v4/members/%s/column-contributions' % self.url_token
        params = {
            'offset': 'offset',
            'limit': 20,
            'include': ','.join([
                'data[*].column.title',
                'intro',
                'description',
                'followers',
                'articles_count'
            ])
        }
        data = req.get(url, params)
        return data if req._raw else parser.columns(data)

    def following_columns(self, offset=0):
        """Get columns that this user followed.

        Args:
            offset: An integer.

        Returns:
            A list of columns.
        """
        url = '/api/v4/members/%s/following-columns' % self.url_token
        params = {
            'offset': offset,
            'limit': 20,
            'include': ','.join([
                'data[*].intro',
                'followers',
                'articles_count',
                'image_url',
                'is_following'
            ])
        }
        data = req.get(url, params)
        return data if req._raw else parser.following_columns(data)

    def following_topics(self, offset=0):
        """Get topics that this user followed and its controbutions.

        Args:
            offset: An integer.

        Returns:
            A list of topics and contributions.
        """
        url = '/api/v4/members/%s/following-topic-contributions' % self.url_token
        params = {
            'offset': offset,
            'limit': 20
        }
        data = req.get(url, params)
        return data if req._raw else parser.following_topics(data)

    def following_questions(self, offset=0):
        """Get questions that this user followed.

        Args:
            offset: An integer.

        Returns:
            A list of questions.
        """
        url = '/api/v4/members/%s/following-questions' % self.url_token
        params = {
            'offset': offset,
            'limit': 20,
            'include': ','.join([
                'data[*].created',
                'answer_count',
                'follower_count'
            ])
        }
        data = req.get(url, params)
        return data if req._raw else parser.questions(data)

    def following_collections(self, offset=0):
        """Get collections that this user followed.

        Args:
            offset: An integer.

        Returns:
            A list of collections.
        """
        url = '/api/v4/members/%s/following-favlists' % self.url_token
        params = {
            'offset': offset,
            'limit': 20,
            'include': ','.join([
                'data[*].updated_time',
                'answer_count',
                'follower_count'
            ])
        }
        data = req.get(url, params)
        return data if req._raw else parser.collections(data)
