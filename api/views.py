from django.contrib.auth.models import User
from django.http import Http404
from django_rest.http import status
from rest_framework.response import Response
from rest_framework.views import APIView
from api.serializers import *
from datetime import datetime


class ListActiveTasks(APIView):
    def get_object(self):
        try:
            try:
                account = Account.objects.get(user=self.request.user)
            except:
                raise Http404
            return Task.objects.filter(owner=account, is_done=False)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request):
        tasks = self.get_object()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            account = Account.objects.get(user=request.user)
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(owner=account, is_done=False)
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class ListDoneTasks(APIView):
    def get_object(self):
        try:
            try:
                account = Account.objects.get(user=self.request.user)
            except:
                raise Http404
            return Task.objects.filter(owner=account, is_done=True)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request):
        if request.user.is_authenticated:
            tasks = self.get_object()
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class TaskDetailView(APIView):
    def get_object(self, pk):
        try:
            account = Account.objects.get(user=self.request.user)
            return Task.objects.get(owner=account, pk=pk)
        except Task.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        if request.user.is_authenticated:
            task = self.get_object(pk)
            serializer = TaskSerializer(task, many=False)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def patch(self, request, pk):
        if request.user.is_authenticated:
            task = self.get_object(pk)
            account = Account.objects.get(user=self.request.user)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save(owner=account, date=datetime.now())
                return Response(serializer.data)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, pk):
        if request.user.is_authenticated:
            task = self.get_object(pk)
            task.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)


class AccountDetailView(APIView):
    def get_object(self):
        if self.request.user.is_authenticated:
            return Account.objects.get(user=self.request.user)
        else:
            raise Http404

    def get(self, request):
        account = self.get_object()
        serializer = AccountSerializer(account, many=False)
        return Response(serializer.data)

    def patch(self, request):
        account = self.get_object()
        serializer = AccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save(user=User.objects.get(username=request.user.username))
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if request.user.is_authenticated:
            user = request.user
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
