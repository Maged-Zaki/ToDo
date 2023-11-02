from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView, View, FormView, CreateView
from django.contrib.auth import authenticate, login, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

from django.utils import timezone

from datetime import datetime, timedelta


#forms and models
from .forms import SignUpForm, LoginForm, TaskForm, GroupTasksForm
from .models import SignUp, Task



class HomeView(TemplateView):
    template_name = "todo_app/index.html"
    



class TasksView(LoginRequiredMixin, View):
    login_url = "/log-in"

    def get(self, request):
        task_from = TaskForm()
        group_form = GroupTasksForm()

        return render(request, "todo_app/my_tasks.html", {
            "task_form": task_from,
            "group_form": group_form,
            "current_tasks": get_user_tasks(self.request.user)
        })


    def post(self, request):
        if "task_submit" in request.POST:

            task_form = TaskForm(request.POST)

            if task_form.is_valid():
                content = task_form.cleaned_data["content"]
                finish_time = task_form.cleaned_data["finish_time"]

                task = Task(user=self.request.user, content=content, finish_time=finish_time)
                task.save()

                return HttpResponseRedirect(reverse("tasks_view"))
            else:
                return render(request, "todo_app/my_tasks.html", {
                    "task_form": task_form,
                    "group_form": GroupTasksForm(),
                    "current_tasks": get_user_tasks(self.request.user)
                })

        elif 'group_submit' in request.POST:
            group_form = GroupTasksForm(request.POST)

            if group_form.is_valid():
                date  = group_form.cleaned_data["date"]

                grouped_tasks = get_grouped_tasks(self.request.user, date)

                return render(request, "todo_app/my_tasks.html", {
                    "task_form": TaskForm(),
                    "group_form": GroupTasksForm(),
                    "current_tasks": grouped_tasks,
                    "grouped_tasks": len(grouped_tasks) >= 1
                })
            
            else:
                return render(request, "todo_app/my_tasks.html", {
                    "task_form": TaskForm(),
                    "group_form": group_form,
                    "current_tasks": get_user_tasks(self.request.user)
                })
            
        return HttpResponseRedirect(reverse("tasks_view"))


def get_user_tasks(user):
    tasks = Task.objects.filter(user=user).order_by("finish_time")

    return tasks
        

def get_grouped_tasks(user, date):
    day = date.day
    month = date.month
    year = date.year

    return Task.objects.filter(user=user, finish_time__day=day, finish_time__month =month, finish_time__year=year).order_by("finish_time")


class SignUpView(CreateView):
    template_name = "todo_app/login.html"
    form_class = SignUpForm
    success_url = "/tasks"
    
    def form_valid(self, form):
        response =  super().form_valid(form)

        login(self.request, self.object)

        return response
    


class CustomLoginView(FormView):
    template_name = "todo_app/login.html"
    form_class = LoginForm
    success_url = "/tasks"

    def form_valid(self, form):
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(self.request, user)

            return super().form_valid(form)
        else:
            try:
                user = SignUp.objects.get(username=username)
            except:
                form.add_error("username", "Invalid Username")
                return super().form_invalid(form)

            form.add_error("password", "Invalid Password")
            return super().form_invalid(form)


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))



@login_required
def delete_task(request, task_id):
    current_user = request.user

    task = get_object_or_404(Task, id=task_id, user=current_user)
    task.delete()
    return HttpResponseRedirect(reverse("tasks_view"))

@login_required
def group_tasks(request):
    current_user = request.user