baseurl = 'https://www.zhihu.com'
column_url = 'https://zhuanlan.zhihu.com'


def full(url):
    if not url:
        return ''
    if url.startswith(baseurl):
        return url
    if url.startswith(column_url):
        return url
    if url[0] != '/':
        url = '/' + url
    return baseurl + url


def question(question_id):
    return '%s/question/%d' % (baseurl, question_id)


def answer(question_id, answer_id):
    return '%s/question/%d/answer/%d' % (baseurl, question_id, answer_id)


def user(url_token, user_type):
    if user_type == 'organization':
        user_type = 'org'
    return '%s/%s/%s' % (baseurl, user_type, url_token)


def article(article_id):
    return '%s/p/%s' % (column_url, article_id)


def collection(collection_id):
    return '%s/collection/%s' % (baseurl, collection_id)


def column(column_id):
    return '%s/%s' % (column_url, column_id)


def topic(topic_id):
    return '%s/topic/%s' % (baseurl, topic_id)
