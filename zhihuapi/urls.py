baseurl = 'https://www.zhihu.com'


def full(url):
    if not url:
        return ''
    if url.startswith(baseurl):
        return url
    if url[0] != '/':
        url = '/' + url
    return baseurl + url
