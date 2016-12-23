from pyquery import PyQuery as pq

from .. import urls
from .util import parse_slug, parse_int, parse_float


def answers_byvote(htmls):
    answers = []
    for html in htmls:
        d = pq(html)
        ele = d('.zm-item-answer')
        answers.append(_parse_answer(d, ele))
    return answers


def _parse_answer(d, ele):
    author_ele = d('.zm-item-answer-author-info .author-link', ele)
    author_link = author_ele.attr('href')
    voteup_ele = d('.zm-item-vote-info', ele)
    content_ele = d('.zm-item-rich-text', ele)
    answer_ele = d('.zm-editable-content', content_ele)
    comment_ele = d('.meta-item.toggle-comment', ele)

    answer = {
        'id': parse_int(ele.attr('data-atoken')),
        'type': 'answer',
        'url': urls.full(content_ele.attr('data-entry-url')),
        'voteup_count': parse_int(voteup_ele.attr('data-votecount')),
        'comment_count': parse_int(comment_ele.text().split()[0]),
        'content': answer_ele.html().strip(),
        'created_time': parse_int(ele.attr('data-created')),
        'author': {
            'name': author_ele.text(),
            'url': urls.full(author_link)
        }
    }
    answer['author'].update(parse_slug(author_link))
    return answer
