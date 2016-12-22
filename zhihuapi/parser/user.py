import json

from .. import urls


def profile(data):
    data['url'] = urls.user(data['url_token'], data['user_type'])
    return data


def detail(d, url_token):
    val = d('#data').attr('data-state')
    val = json.loads(val)
    return val['entities']['users'][url_token]


def activities(data):
    data = data['data']
    for obj in data:
        actor = obj['actor']
        target = obj['target']
        actor['url'] = urls.user(actor['url_token'], actor['user_type'])
        if target['type'] == 'topic':
            target['url'] = urls.topic(target['id'])
        elif target['type'] == 'question':
            target['url'] = urls.question(target['id'])
        elif target['type'] == 'answer':
            question = target['question']
            author = target['author']
            target['url'] = urls.answer(question['id'], target['id'])
            question['url'] = urls.question(question['id'])
            author['url'] = urls.user(author['url_token'], author['user_type'])
        elif target['type'] == 'column':
            target['url'] = urls.column(target['id'])
        elif target['type'] == 'collection':
            target['url'] = urls.collection(target['id'])
    return data


def questions(data):
    data = data['data']
    for obj in data:
        obj['url'] = urls.question(obj['id'])
    return data


def answers(data):
    data = data['data']
    for obj in data:
        question = obj['question']
        author = obj['author']
        obj['url'] = urls.answer(question['id'], obj['id'])
        question['url'] = urls.question(question['id'])
        author['url'] = urls.user(author['url_token'], author['user_type'])
    return data


def articles(data):
    data = data['data']
    for obj in data:
        author = obj['author']
        obj['url'] = urls.article(obj['id'])
        author['url'] = urls.user(author['url_token'], author['user_type'])
    return data


def collections(data):
    data = data['data']
    for obj in data:
        obj['url'] = urls.collection(obj['id'])
    return data


def follows(data):
    data = data['data']
    for obj in data:
        obj['url'] = urls.user(obj['url_token'], obj['user_type'])
    return data


def columns(data):
    data = data['data']
    for obj in data:
        col = obj['column']
        author = col['author']
        col['url'] = urls.column(col['id'])
        author['url'] = urls.user(author['url_token'], author['user_type'])
    return data


def following_columns(data):
    data = data['data']
    for obj in data:
        author = obj['author']
        obj['url'] = urls.column(obj['id'])
        author['url'] = urls.user(author['url_token'], author['user_type'])
    return data


def following_topics(data):
    data = data['data']
    for obj in data:
        topic = obj['topic']
        topic['url'] = urls.topic(topic['id'])
    return data
