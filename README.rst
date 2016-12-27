zhihu API
=========================

**UNOFFICIAL** API for `zhihu <https://www.zhihu.com>`_. This package supports only Python 3.x.

A `Node.js implementation <https://github.com/syaning/zhihu-api>`_ is also available.

Installation
------------

.. code-block:: bash

    $ pip install zhihuapi

Quich Start
-----------

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

License
-------

MIT