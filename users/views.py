from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers.UserSerializer import UserSerializer
from .services.UserService import UserService
from server.middlewares.Authority import Authority
from common.Util import Util


class UserView(APIView):

    @classmethod
    @Authority.requires_rights([])
    @Util.time_used
    def get(cls, request):
        users = UserService.get_all()
        users = UserSerializer(users, many=True)
        return Response(users.data)
