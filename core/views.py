from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.urls import reverse_lazy
from django.contrib.auth.models import auth
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from core.models import *
from django.http import HttpResponseRedirect, Http404
from core.forms import *
from datetime import datetime

class TaskList(LoginRequiredMixin, ListView):
    def get(self, request):
        account = Account.objects.get(user=request.user)
        current_tasks = Task.objects.filter(owner=account, is_done=False).order_by('-date', '-is_done')
        archive_tasks = tasks = Task.objects.filter(owner=account, is_done=True).order_by('-date', '-is_done')
        # TODO finish pagination
        paginator = Paginator(current_tasks, 100)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'current_tasks': page_obj,
            'archive_tasks': archive_tasks,
        }
        return render(request, 'index.html', context)

    def handle_no_permission(self):
        return redirect('login')

class TaskFiletredList(LoginRequiredMixin, ListView):
    def get_queryset(self):
        query = self.request.POST.get('query')
        account = Account.objects.get(user=self.request.user)
        return Task.objects.filter(Q(owner=account) & Q(title__icontains=query) | Q(task__icontains=query))

    def post(self, request):
        tasks = self.get_queryset()
        paginator = Paginator(tasks, 100)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {
            'filtered_tasks': page_obj,
        }
        return render(request, 'index.html', context)
    def handle_no_permission(self):
        return redirect('login')



class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    # fields = ['task']
    template_name = 'task_form.html'
    form_class = TaskForm
    extra_context = {
        'title': 'add new task',
    }
    success_url = reverse_lazy('task-list')

    def form_valid(self, form):
        task = form.save(commit=False)
        task.owner = Account.objects.get(user=self.request.user)
        task.save()
        return super(TaskCreate, self).form_valid(form)

    def handle_no_permission(self):
        return redirect('login')


class TaskEdit(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    extra_context = {'title': "Edit task"}
    success_url = reverse_lazy('task-list')

    def get_object(self, **kwargs):
        try:
            task = Task.objects.get(pk=self.kwargs['pk'])
            account = Account.objects.get(user=self.request.user)
            if task.owner == account:
                return task
            else:
                raise Http404
        except:
            raise Http404

    def form_valid(self, form):
        task = form.save(commit=False)
        task.date = datetime.now()
        task.save()
        return super(TaskEdit, self).form_valid(form)

    def handle_no_permission(self):
        return redirect('login')


class TaskDelete(LoginRequiredMixin, View):
    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            account = Account.objects.get(user=self.request.user)
            if task.owner == account:
                return task
            else:
                raise Http404
        except:
            raise Http404

    def get(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return redirect('task-list')

    def handle_no_permission(self):
        return redirect('login')


class AccountEditView(LoginRequiredMixin, UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'profile.html'
    success_url = reverse_lazy('account-settings')

    def get_object(self):
        try:
            return Account.objects.get(user=self.request.user)
        except Account.DoesNotExist:
            raise Http404

    def handle_no_permission(self):
        return redirect('login')


class AccountDelete(LoginRequiredMixin, View):
    def get_object(self):
        try:
            return User.objects.get(username=self.request.user.username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request):
        account = self.get_object()
        account.delete()
        return redirect('logout')

    def handle_no_permission(self):
        return redirect('login')


class UserLogin(LoginView):
    template_name = "login.html"


class UserRegister(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')


class PasswordChangeView(PasswordChangeView):
    template_name = "password_change.html"
    success_url = reverse_lazy('logout')


@login_required(login_url='login')
def change_task_state(request, pk):
    account = Account.objects.get(user=request.user)
    try:
        task = Task.objects.get(pk=pk)
        if task.is_done:
            task.is_done = False
            task.save()
        else:
            task.is_done = True
        task.date = datetime.now()
        task.save()
        return redirect('task-list')
    except Task.DoesNotExist:
        raise Http404


def logout(request):
    auth.logout(request)
    return redirect('login')
