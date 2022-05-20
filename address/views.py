from django.shortcuts import get_object_or_404
from rest_framework.authentication import TokenAuthentication
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


from address.models import Address
from accounts.models import MyUser
from address.serializers import AddressSerializer, AddressUserSerializer



class AddressView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request: Request):
        serializer = AddressSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        found_address = Address.objects.filter(
            zip_code=serializer.validated_data["zip_code"]
        ).exists()

        if found_address:
            user = request.user
            user.address = Address.objects.get(zip_code=serializer.validated_data["zip_code"])
            user.save()

            serializer = get_object_or_404(Address,zip_code=serializer.validated_data["zip_code"])
            serializer = AddressUserSerializer(serializer)

            return Response(serializer.data, status.HTTP_200_OK)

        address: Address = Address.objects.create(**serializer.validated_data)
        address.save()

        request.user.address = address
        request.user.save()

        serializer = AddressUserSerializer(address)

        return Response(serializer.data, status.HTTP_200_OK)