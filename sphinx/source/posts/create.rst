create
-------

Создавать посты могут только зарегистрированые пользователи. Пост создаётся в блоге
пользователя.

Создать пост ::

    POST /api/posts

Обязательные параметры:

* ``title``
* ``content``

Опциональные параметры:


Пример: ::

    POST /api/v2/posts
    {
    "title": "Another post user2",
    "content": "Some content as."
    }

::

    201 Created
    {
    "title": "Another post user2",
    "content": "Some content as.",
    "created": "2022-02-07",
    "updated": "2022-02-07",
    "published": null,
    "status": "draft",
    "blog": 7
    }

