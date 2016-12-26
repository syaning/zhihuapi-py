from .. import urls
from .util import parse_slug, parse_int


def answers(d):
    eles = d('.zm-item[data-type="Answer"]')
    return [_parse_answer(d, ele) for ele in eles]


def _parse_answer(d, ele):
    question_ele = d('.zm-item-title a', ele)
    question_link = question_ele.attr('href')
    answer_ele = d('.zm-item-answer', ele)
    voteup_ele = d('.zm-votebar .count', ele)
    author_ele = d('.zm-item-answer-author-info .author-link', ele)
    author_link = author_ele.attr('href')
    content_ele = d('.zm-item-rich-text textarea', ele)
    comments_ele = d('.zm-item-meta .toggle-comment', ele)

    answer = {
        'id': parse_int(answer_ele.attr('data-atoken')),
        'type': 'answer',
        'voteup_count': parse_int(voteup_ele.text()),
        'comment_count': parse_int(comments_ele.text().split()[0]),
        'content': content_ele.text(),
        'created_time': parse_int(answer_ele.attr('data-created')),
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
