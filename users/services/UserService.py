from ..models.UserModel import UserModel


class UserService:

    @classmethod
    def get_all(cls):
        users = UserModel.objects.all()
        return users
