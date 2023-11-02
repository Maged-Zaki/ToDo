from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path("log-in", views.CustomLoginView.as_view(), name="login"),
    path("sign_up", views.SignUpView.as_view(), name="sign_up"),
    path("tasks", views.TasksView.as_view(), name="tasks_view"),
    path("logout", views.logout_user, name="logout"),
    path("delete_task/<int:task_id>", views.delete_task, name="delete_task"),
    path("group_tasks", views.group_tasks, name="group_tasks"),

    ]