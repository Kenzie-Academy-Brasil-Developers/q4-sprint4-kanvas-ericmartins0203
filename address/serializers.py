from rest_framework import serializers

from accounts.serializers import AccountsSerializer

class AddressSerializer(serializers.Serializer):
    uuid = serializers.CharField(read_only=True)
    street = serializers.CharField()
    house_number = serializers.FloatField()
    city = serializers.CharField()
    state = serializers.CharField()
    zip_code = serializers.CharField()
    country = serializers.CharField()

class AddressUserSerializer(serializers.Serializer):
    uuid = serializers.CharField(read_only=True)
    street = serializers.CharField()
    house_number = serializers.FloatField()
    city = serializers.CharField()
    state = serializers.CharField()
    zip_code = serializers.CharField()
    country = serializers.CharField()
    users = AccountsSerializer(many=True)