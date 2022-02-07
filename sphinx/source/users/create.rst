create
-------

Создать пользователя ::

    POST /api/users

Обязательные параметры:

* ``username``
* ``password``
* ``email``

Опциональные параметры:


Пример: ::

    POST /api/v2/users
    {
    "username": "test_user001",
    "password": "P@ssw0rd!",
    "email": "001@mail.ru"
    }

::

    201 Created
    {
    "username": "test_user001",
    "last_login": null,
    "email": "001@mail.ru",
    "date_joined": "2022-02-07T15:52:59.079174Z",
    "is_staff": false,
    "id": 37
    }

