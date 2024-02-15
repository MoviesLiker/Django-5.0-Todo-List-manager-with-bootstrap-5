from django.urls import path
from . import views

urlpatterns = [

    path('auth/signup', views.auth.signup, name='auth.signup'),
    path('auth/signup-submit', views.auth.signup_submit, name='auth.signup_submit'),
    path('auth/login', views.auth.login, name='auth.login'),
    path('auth/login-submit', views.auth.login_submit, name='auth.login_submit'),
    path('auth/logout', views.auth.logout, name='auth.logout'),

    path('', views.dashboard.dashboard, name='dashboard'),

    path('tasks/add-task-submit', views.dashboard.tasks.add_task_submit,
         name='tasks.add_task_submit'),
    path('tasks/edit-task/<int:id>', views.dashboard.tasks.edit_task,
         name='tasks.edit_task'),
    path('tasks/edit-task-submit', views.dashboard.tasks.edit_task_submit,
         name='tasks.edit_task_submit'),
    path('tasks/delete-task/<int:id>', views.dashboard.tasks.delete_task,
         name='tasks.delete_task'),
]
