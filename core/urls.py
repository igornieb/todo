from django.urls import path
from core.views import *

urlpatterns = [
    path("", TaskList.as_view(), name='task-list'),
    path("create-task", TaskCreate.as_view(), name='task-create'),
    path("edit-task/<pk>", TaskEdit.as_view(), name='task-edit'),
    path("search", TaskFiletredList.as_view(), name='search'),
    path("delete-task/<pk>", TaskDelete.as_view(), name='task-delete'),
    path("change-task-state/<pk>", change_task_state, name='change-task-state'),
    path("account", AccountEditView.as_view(), name='account-settings'),
    path("account/delete", AccountDelete.as_view(), name='account-delete'),
    path("account/change-password", PasswordChangeView.as_view(), name='change-password'),
    path("login", UserLogin.as_view(), name='login'),
    path("register", UserRegister.as_view(), name='register'),
    path("logout", logout, name="logout"),
]
