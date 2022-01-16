from rest_framework import routers


def get_url_routes(viewsets, router=None):
    if router is None:
        router = routers.SimpleRouter(trailing_slash=False)
    for args in viewsets:
        router.register(*args)
    return router.urls
