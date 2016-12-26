zhihu API
=========

This is just an **UNOFFICIAL** API for `zhihu <https://www.zhihu.com>`_. View source on `Github <https://github.com/syaning/zhihuapi-py>`_.

`Node.js version <https://github.com/syaning/zhihu-api>`_ is also available.


Installation
============

.. code-block:: bash

    $ pip install zhihuapi


Quich Start
===========

.. code-block:: python

    import zhihuapi as api

    with open('cookie') as f:
        api.cookie(f.read())

    data = api.user('zhihuadmin').profile()
    print(data)

The result is:

.. code-block:: js

    {
        "url_token": "zhihuadmin",
        "avatar_url": "https://pic3.zhimg.com/34bf96bf5584ac4b5264bd7ed4fdbc5a_is.jpg",
        "avatar_url_template": "https://pic3.zhimg.com/34bf96bf5584ac4b5264bd7ed4fdbc5a_{size}.jpg",
        "type": "people",
        "name": "知乎小管家",
        "headline": "欢迎反馈问题和建议！",
        "is_org": false,
        "url": "https://www.zhihu.com/people/zhihuadmin",
        "badge": [
            {
                "type": "identity",
                "description": "知乎官方帐号"
            }
        ],
        "user_type": "people",
        "is_advertiser": false,
        "id": "3d198a56310c02c4a83efb9f4a4c027e"
    }

*Note that you must set cookie before sending any HTTP request.*


API
===


Set Cookie
----------

.. autofunction:: zhihuapi.cookie


Raw Response
------------

.. autofunction:: zhihuapi.raw


User
----

.. autoclass:: zhihuapi.user
.. autoclass:: zhihuapi.user.User
    :members:


Topic
-----

.. autoclass:: zhihuapi.topic
.. autoclass:: zhihuapi.topic.Topic
    :members:


Question
--------

.. autoclass:: zhihuapi.question
.. autoclass:: zhihuapi.question.Question
    :members:


Answer
------

.. autoclass:: zhihuapi.answer
.. autoclass:: zhihuapi.answer.Answer
    :members:


Collection
----------

.. autoclass:: zhihuapi.collection
.. autoclass:: zhihuapi.collection.Collection
    :members:


Column
------

.. autoclass:: zhihuapi.column
.. autoclass:: zhihuapi.column.Column
    :members:


Action
------

.. automodule:: zhihuapi.action
    :members:
