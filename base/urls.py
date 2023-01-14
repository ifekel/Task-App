from django.urls import path
from . import views
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('create', CreateTask.as_view(), name='create'),    
    path('task_detail/<str:pk>', views.task_detail, name='task_detail'),
    path('login', views.login, name='login'),
    path('login_form', views.login_form, name='login_form'),
    path('signup', views.signup, name='signup'),
    path('signup_form', views.signup_form, name='signup_form'),
    path('favorite', Favorite.as_view(), name='favorite'),
    path('deleted', views.deleted, name='deleted'),
    path('completed', Completed.as_view(), name='completed'),
    path('update_task/<str:pk>', UpdateTask.as_view(), name='update_task'),
    path('delete_task/<str:pk>', DeleteTask.as_view(), name='delete_task'),
    path('logout', LogoutView.as_view(next_page='login'), name='logout'),
    path('password', views.generatePassword, name='password'),
]