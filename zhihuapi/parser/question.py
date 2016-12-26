from pyquery import PyQuery as pq

from .. import urls
from .util import parse_slug, parse_int


def answers_byvote(htmls):
    answers = []
    for html in htmls:
        d = pq(html)
        ele = d('.zm-item-answer')
        answers.append(_parse_answer(d, ele))
    return answers


def answers_bypage(d):
    eles = d('#zh-question-answer-wrap .zm-item-answer')
    return [_parse_answer(d, d(ele)) for ele in eles]


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


def detail(d):
    main_ele = d('.zu-main-content-inner')
    visits_ele = d('meta[itemprop="visitsCount"]', main_ele)
    topics_ele = d('.zm-tag-editor-labels .zm-item-tag', main_ele)
    title_ele = d('#zh-question-title .zm-item-title', main_ele)
    detail_ele = d('#zh-question-detail .zm-editable-content', main_ele)
    if not len(detail_ele):
        detail_ele = d('#zh-question-detail textarea', main_ele)
    comments_ele = d('#zh-question-meta-wrap .toggle-comment', main_ele)
    answers_ele = d('#zh-question-answer-num', main_ele)
    sidebar_ele = d('.zu-main-sidebar')
    follow_btn_ele = d('.follow-button', sidebar_ele)
    follow_ele = d('.zh-question-followers-sidebar .zg-gray-normal a',
                   sidebar_ele)
    link = follow_ele.attr('href')[:-len('/followers')]

    question = {
        'id': parse_int(link[len('/question/')]),
        'type': 'question',
        'title': title_ele.text().strip(),
        'url': urls.full(link),
        'content': detail_ele.text(),
        'answer_count': parse_int(answers_ele.attr('data-num')),
        'comment_count': parse_int(comments_ele.text().split()[0]),
        'follower_count': parse_int(follow_ele.text()),
        'visit_count': parse_int(visits_ele.attr('content')),
        'topics': [_parse_topics(d(ele)) for ele in topics_ele]
    }
    return question


def _parse_topics(ele):
    link = ele.attr('href')
    topic = {
        'id': parse_int(link[len('/topic/'):]),
        'type': 'topic',
        'name': ele.text().strip()
    }
    return topic


def followers(html):
    d = pq(html)
    eles = d('.zm-profile-card')
    return [_parse_follower(d, ele) for ele in eles]


def _parse_follower(d, ele):
    id_ele = d('.zm-rich-follow-btn', ele)
    link_ele = d('.zm-item-link-avatar', ele)
    link = link_ele.attr('href')

    follower = {
        'id': id_ele.attr('data-id'),
        'name': link_ele.attr('title'),
        'url': urls.full(link),
    }
    follower.update(parse_slug(link))
    return follower
