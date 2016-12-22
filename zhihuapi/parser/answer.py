from .. import urls


def voters(data):
    data = data['data']
    for obj in data:
        obj['url'] = urls.user(obj['url_token'], obj['user_type'])
    return data
