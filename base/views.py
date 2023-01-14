from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
import json
import random
import csv
from .models import *

def login_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('tasks')
            
        else:
            messages.info(request, "Account not found!")
            return redirect('login')
        return render(request, 'login.html')


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        context['favs'] = context['tasks'].filter(favorite=True).count()
        return context

@login_required(login_url='login')
def task_detail(request, pk):
    task = Task.objects.get(id=pk)
    return render(request, 'task-detail.html', {'task': task})


class Favorite(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'favorite.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        context['favs'] = context['tasks'].filter(favorite=True).count()
        return context
    
class Completed(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'completed.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        context['favs'] = context['tasks'].filter(favorite=True).count()
        return context
    
@login_required(login_url='login')
def deleted(request):
    task = Task.objects.all()
    return render(request, 'deleted.html', {'tasks': task})

class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ["title", "description", "complete", "favorite"]    
    template_name = 'create.html'
    success_url = reverse_lazy('tasks')
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CreateTask, self).form_valid(form)

def signup(request):
    return render(request, 'signup.html')

def signup_form(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password != password2:
            messages.error(request, 'Password mismatch')
            return redirect('signup')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is already in use')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Account created successfully')
                return redirect('login')
    return render(request, 'signup.html')

def login(request):
    return render(request, 'login.html')

class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ["title", "description", "complete", "favorite"]
    template_name = 'update_task.html'
    success_url = reverse_lazy('tasks')
    

class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    template_name = 'delete_task.html'
    success_url = reverse_lazy('tasks')
    
    
def generatePassword(request):
    letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L'] 
    letter2 = ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i in range(10):
        password = random.choice(letter) + random.choice(letter2) + random.choice(letter) + random.choice(letter2) + random.choice(letter) + random.choice(letter2) + random.choice(letter) + random.choice(letter2) + random.choice(letter) + random.choice(letter2) + random.choice(letter) + random.choice(letter2) + random.choice(letter) + random.choice(letter2) + random.choice(letter) + random.choice(letter2)
    randomPassword = password
    return render(request, 'generate_password.html', {'password': randomPassword})
