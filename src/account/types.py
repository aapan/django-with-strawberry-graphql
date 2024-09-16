import strawberry_django
from django.contrib.auth import get_user_model
from strawberry import auto


@strawberry_django.order(get_user_model())
class UserOrder:
    email: auto


@strawberry_django.filter(get_user_model())
class UserFilter:
    id: auto
    username: auto
    email: auto


@strawberry_django.type(get_user_model(), filters=UserFilter, order=UserOrder)
class UserType:
    id: auto
    username: auto
    email: auto


@strawberry_django.input(get_user_model())
class UserInput:
    username: auto
    email: auto
