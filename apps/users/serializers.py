from django.contrib.auth.models import User
from django.utils.translation import gettext as _
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)


    def validate_username(self, username):
        check_username = User.objects.filter(username=username)
        if self.instance:
            check_username = check_username.exclude(id=self.instance.id)

        if check_username.exists():
            raise ValidationError('User with such username exists')
        return username

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'password', 'username')


class PlanUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')