def parse_slug(link):
    ret = {
        'type': 'people'
    }

    if not link:
        ret['name'] = '匿名用户'
        return ret

    if link.startswith('/org/'):
        ret['user_type'] = 'organization'
        ret['url_token'] = link[len('/org/'):]
    else:
        ret['user_type'] = 'people'
        ret['url_token'] = link[len('/people/'):]

    return ret


def parse_int(val):
    try:
        return int(val)
    except:
        return 0


def parse_float(val):
    try:
        return float(val)
    except:
        return 0
