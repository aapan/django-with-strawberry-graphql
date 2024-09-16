import strawberry
import strawberry_django
from strawberry_django.optimizer import DjangoOptimizerExtension

from account.types import UserInput, UserType


@strawberry.type
class Query:
    me: UserType = strawberry_django.auth.current_user()
    get_users: list[UserType] = strawberry_django.field()


@strawberry.type
class Mutation:
    login: UserType = strawberry_django.auth.login()
    logout = strawberry_django.auth.logout()
    register: UserType = strawberry_django.auth.register(UserInput)


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        DjangoOptimizerExtension,
    ],
)
