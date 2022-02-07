list
-------

Создать пользователя ::

    GET /api/users



Пример: ::

    GET /api/v2/users

    [
    {
        "username": "test_user001",
        "last_login": null,
        "email": "001@mail.ru",
        "date_joined": "2022-02-07T15:52:59.079174Z",
        "is_staff": false,
        "id": 37
    },
    {
        "username": "test_user1",
        "last_login": null,
        "email": "11@mail.ru",
        "date_joined": "2022-01-18T14:28:28.887669Z",
        "is_staff": false,
        "id": 6
    },
    {
        "username": "test_user2",
        "last_login": null,
        "email": "22@mail.ru",
        "date_joined": "2022-01-18T17:50:43.536860Z",
        "is_staff": false,
        "id": 7
    }
    ]
