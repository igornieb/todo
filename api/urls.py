from django.urls import path, include
from api.views import *
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views

urlpatterns = [
    path('active', ListActiveTasks.as_view()),
    path('archive', ListDoneTasks.as_view()),
    path('task/<pk>', TaskDetailView.as_view()),
    path('account', AccountDetailView.as_view()),
    path('api-auth', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
