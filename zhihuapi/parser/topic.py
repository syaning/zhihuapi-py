from pyquery import PyQuery as pq

from .. import urls
from .util import parse_slug, parse_int, parse_float


def hierarchy(d):
    link_ele = d('.topic-avatar .zm-entry-head-avatar-link')
    link = link_ele.attr('href')
    avatar_ele = d('img', link_ele)
    parent_eles = d('#zh-topic-organize-parent-editor .zm-item-tag')
    child_eles = d('#zh-topic-organize-child-editor .zm-item-tag')

    topic = {
        'id': parse_int(link[len('/topic/'):]),
        'type': 'topic',
        'url': urls.full(link),
        'name': avatar_ele.attr('alt'),
        'avatar_url': avatar_ele.attr('src'),
        'parents': _parse_hierarchy_labels(d, parent_eles),
        'children': _parse_hierarchy_labels(d, child_eles)
    }
    return topic


def _parse_hierarchy_labels(d, eles):
    topics = []
    for ele in eles:
        ele = d(ele)
        link = ele.attr('href').rstrip('/organize')
        topic = {
            'id': parse_int(ele.attr('data-token')),
            'type': 'topic',
            'name': ele.text().strip(),
            'url': urls.full(link)
        }
        topics.append(topic)
    return topics


def followers(html):
    followers = []
    d = pq(html)
    eles = d('.zm-person-item')
    return [_parse_follower(d, ele) for ele in eles]


def _parse_follower(d, ele):
    follow_ele = d('.zg-btn', ele)
    name_ele = d('.zm-list-content-title a', ele)
    link = name_ele.attr('href')
    follower = {
        'id': follow_ele.attr('id')[len('pp-'):],
        'name': name_ele.text(),
        'url': urls.full(link)
    }
    follower.update(parse_slug(link))
    return follower


def answers(d):
    if type(d) is str:
        d = pq(d)
    eles = d('.feed-item')
    return [_parse_answer(d, ele) for ele in eles]


def _parse_answer(d, ele):
    ele = d(ele)
    ques_ele = d('.question_link', ele)
    ques_link = ques_ele.attr('href')
    entry_ele = d('.entry-body', ele)
    voteup_ele = d('.zm-item-vote-info', entry_ele)
    author_ele = d('.zm-item-answer-author-info .author-link', entry_ele)
    author_link = author_ele.attr('href')
    answer_ele = d('.zm-item-rich-text', entry_ele)
    answer_link = answer_ele.attr('data-entry-url') or ''
    content_ele = d('textarea', answer_ele)
    comment_ele = d('.zm-item-meta .toggle-comment', ele)
    comment_count = comment_ele.text().split()
    comment_count = comment_count[0] if len(comment_count) else 0

    answer = {
        'id': parse_int(answer_link[answer_link.rfind('/') + 1:]),
        'type': 'answer',
        'url': urls.full(answer_link),
        'voteup_count': parse_int(voteup_ele.attr('data-votecount')),
        'comment_count': parse_int(comment_count),
        'content': content_ele.text(),
        'author': {
            'name': author_ele.text(),
            'url': urls.full(author_link)
        },
        'question': {
            'id': parse_int(ques_link[len('/question/'):]),
            'type': 'question',
            'title': ques_ele.text(),
            'url': urls.full(ques_link)
        },
        'score': parse_float(ele.attr('data-score'))
    }
    answer['author'].update(parse_slug(author_link))
    return answer


def questions(d):
    eles = d('.feed-item')
    return [_parse_question(d, ele) for ele in eles]


def _parse_question(d, ele):
    link_ele = d('.question_link', ele)
    link = link_ele.attr('href')
    answers_ele = d('meta[itemprop="answerCount"]', ele)
    followers_ele = d('.question-item-meta .meta-item:nth-child(3)', ele)

    question = {
        'id': parse_int(link[len('/question/'):]),
        'type': 'question',
        'url': urls.full(link),
        'title': link_ele.text(),
        'answer_count': parse_int(answers_ele.attr('count')),
        'follower_count': parse_int(followers_ele.text().split()[0])
    }
    return question
