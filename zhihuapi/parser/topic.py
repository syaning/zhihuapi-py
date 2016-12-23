from pyquery import PyQuery as pq

from .. import urls


def hierarchy(d):
    link_ele = d('.topic-avatar .zm-entry-head-avatar-link')
    link = link_ele.attr('href')
    avatar_ele = d('img', link_ele)
    parent_eles = d('#zh-topic-organize-parent-editor .zm-item-tag')
    child_eles = d('#zh-topic-organize-child-editor .zm-item-tag')

    topic = {
        'id': int(link.lstrip('/topic/')),
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
            'id': int(ele.attr('data-token')),
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
    for ele in eles:
        # ele = d(ele)
        follow_ele = d('.zg-btn', ele)
        name_ele = d('.zm-list-content-title a', ele)
        link = name_ele.attr('href')
        follower = {
            'id': follow_ele.attr('id').lstrip('pp-'),
            'type': 'people',
            'user_type': 'organization' if link.startswith('/org') else 'people',
            'name': name_ele.text(),
            'url_token': link.lstrip('/poeple/').lstrip('/org/'),
            'url': urls.full(link)
        }
        followers.append(follower)
    return followers
