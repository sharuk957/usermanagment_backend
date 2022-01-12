from rest_framework import serializers

from .models import MyUser


class UserSerializer(serializers.ModelSerializer):
    last_login = serializers.DateField(read_only=True)
    is_active = serializers.BooleanField(read_only=True)
    is_admin = serializers.BooleanField(read_only=True)
    is_superuser = serializers.BooleanField(read_only=True)
    is_staff = serializers.BooleanField(read_only=True)

    class Meta:

        model = MyUser
        fields = '__all__'

    def create(self,validated_data):
        user = MyUser.objects.create_user(**validated_data)
        return user