from rest_framework import serializers
from django.contrib.auth import get_user_model
from core.forms import *

User = get_user_model()


class AccountSerializer(serializers.ModelSerializer):
    user = User
    class Meta:
        model = Account
        fields = ['user', 'first_name', 'last_name', 'profile_picture']


class TaskSerializer(serializers.ModelSerializer):
    owner = AccountSerializer(many=False, read_only=True)

    class Meta:
        model = Task
        fields = ['pk', 'owner', 'title','task', 'date', 'is_done']
