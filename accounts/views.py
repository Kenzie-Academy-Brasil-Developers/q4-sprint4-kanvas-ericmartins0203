from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.models import MyUser
from accounts.serializers import AccountsSerializer, LoginSerializer
from accounts.permissions import isAdmin


class AccountsView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [isAdmin]


    def get(self, request:Request):

        users = MyUser.objects.all()
        serializer = AccountsSerializer(users, many=True)

        return Response(serializer.data, status.HTTP_200_OK)        


    def post(self, request: Request):
        serializer = AccountsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        found_user = MyUser.objects.filter(
            email=serializer.validated_data["email"]
        ).exists()

        if found_user:
            return Response(
                {"message": "User already exists"}, status.HTTP_422_UNPROCESSABLE_ENTITY
            )

        user = MyUser.objects.create(**serializer.validated_data)
        user.set_password(serializer.validated_data["password"])
        user.save()

        serializer = AccountsSerializer(user)

        return Response(serializer.data, status.HTTP_201_CREATED)


@api_view(["POST"])
def login_view(request: Request):
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    user = authenticate(
        username=serializer.validated_data["email"],
        password=serializer.validated_data["password"],
    )

    if not user:
        return Response(
            {"message": "Invalid credentials."}, status.HTTP_401_UNAUTHORIZED
        )

    token, _ = Token.objects.get_or_create(user=user)

    return Response({"token": token.key})