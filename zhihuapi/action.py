from .request import req


def follow(url_token):
    """Follow a user.

    Args:
        url_token: The url token (or slug) of the user.
    """
    url = '/api/v4/members/%s/followers' % url_token
    return req.post(url)


def unfollow(url_token):
    """Unfollow a user.

    Args:
        url_token: The url token (or slug) of the user.
    """
    url = '/api/v4/members/%s/followers' % url_token
    return req.delete(url)


def message(user_id, content):
    """Send message to a user.

    Args:
        user_id: Hash id of the user.
        content: Message content in string.
    """
    url = '/api/v4/messages'
    data = {
        'content': content,
        'type': 'common',
        'receiver_hash': user_id
    }
    return req.post(url, json=data)


def vote(answer_id, val):
    """Vote an answer.

    Args:
        answer_id: The id of the answer.
        val: Voting type in number. 1 for voting up, 0 for voting neutral, -1 for voting down.
    """
    url = '/api/v4/answers/%s/voters' % answer_id
    if val > 0:
        data = {'type': 'up'}
    elif val < 0:
        data = {'type': 'down'}
    else:
        data = {'type': 'neutral'}
    return req.post(url, json=data)


def vote_up(answer_id):
    """Vote up an answer.

    Args:
        answer_id: The id of the answer.
    """
    return vote(answer_id, 1)


def vote_neutral(answer_id):
    """Vote neutral an answer.

    Args:
        answer_id: The id of the answer.
    """
    return vote(answer_id, 0)


def vote_down(answer_id):
    """Vote down an answer.

    Args:
        answer_id: The id of the answer.
    """
    return vote(answer_id, -1)


def report(resource_id, resource_type, reason_type):
    """Report a question, an answer, or a member
    
    For a question, valid reason_type are:
        - personal
        - spam
        - TODO add more reason_types for question
    For an answer, valid reason_type are:
        - spam
        - TODO add more reason_types for answer
    For a user, valid reason_type are:
        - spam
        - TODO add more reason_types for user
    
    Args:
        resource_id: The id of the entity (question id, answer id, member name)
        resource_type: question, answer, member
        reason_type: spam, etc.
    """
    url = '/api/v4/reports'
    data = {
        'resource_id': resource_id,
        'type': resource_type,
        'reason_type': reason_type,
        'source': 'web'
    }
    return req.post(url, json=data)
