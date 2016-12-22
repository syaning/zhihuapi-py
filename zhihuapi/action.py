from .request import req


def follow(url_token):
    """Follow a user."""
    url = '/api/v4/members/%s/followers' % url_token
    return req.post(url)


def unfollow(url_token):
    """Unfollow a user."""
    url = '/api/v4/members/%s/followers' % url_token
    return req.delete(url)


def message(user_id, content):
    """Send message to a user."""
    url = '/api/v4/messages'
    data = {
        'content': content,
        'type': 'common',
        'receiver_hash': user_id
    }
    return req.post(url, json=data)


def vote(answer_id, val):
    """Vote an answer."""
    url = '/api/v4/answers/%s/voters' % answer_id
    if val > 0:
        data = {'type': 'up'}
    elif val < 0:
        data = {'type': 'down'}
    else:
        data = {'type': 'neutral'}
    return req.post(url, json=data)


def vote_up(answer_id):
    """Vote up an answer."""
    return vote(answer_id, 1)


def vote_neutral(answer_id):
    """Vote up an answer."""
    return vote(answer_id, 0)


def vote_down(answer_id):
    """Vote up an answer."""
    return vote(answer_id, -1)
