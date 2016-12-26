from .. import urls
from .util import parse_slug, parse_int


def voters(data):
    data = data['data']
    for obj in data:
        obj['url'] = urls.user(obj['url_token'], obj['user_type'])
    return data


def comments(data):
    return data['data']


def explore(d):
    eles = d('.feed-item')
    return [_parse_explore(d, ele) for ele in eles]


def _parse_explore(d, ele):
    question_ele = d('.question_link', ele)
    link = question_ele.attr('href')
    question_link = link[:link.find('/answer')]
    item_ele = d('.zm-item-answer', ele)
    voteup_ele = d('.zm-item-vote-info', item_ele)
    author_ele = d('.zm-item-answer-author-info .author-link', item_ele)
    author_link = author_ele.attr('href')
    content_ele = d('.zm-item-rich-text textarea', item_ele)
    comments_ele = d('.zm-item-meta .toggle-comment', ele)

    answer = {
        'id': parse_int(item_ele.attr('data-atoken')),
        'type': 'answer',
        'url': urls.full(link),
        'voteup_count': parse_int(voteup_ele.attr('data-votecount')),
        'comment_count': parse_int(comments_ele.text().split()[0]),
        'content': content_ele.text(),
        'created_time': parse_int(item_ele.attr('data-created')),
        'author': {
            'name': author_ele.text(),
            'url': urls.full(author_link)
        },
        'question': {
            'id': parse_int(question_link[len('/question/'):]),
            'type': 'question',
            'title': question_ele.text(),
            'url': urls.full(question_link)
        }
    }
    answer['author'].update(parse_slug(author_link))
    return answer
