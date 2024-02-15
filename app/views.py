from django.shortcuts import redirect, render
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class auth:
    def signup(request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'auth/signup.html')

    def signup_submit(request):
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username).exists():
            messages.warning(request, "Username already exists.")
            return redirect('auth.signup')

        if User.objects.filter(email=email).exists():
            messages.warning(request, "Email already exists.")
            return redirect('auth.signup')

        if password != confirm_password:
            messages.warning(request, "Password didn't match.")
            return redirect('auth.signup')

        user = User.objects.create_user(
            username,
            email,
            password
        )
        user.save()

        messages.success(request, "Signup successfully!.")
        return redirect('auth.login')

    def login(request):
        if request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'auth/login.html')

    def login_submit(request):
        pass
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.warning(request, "Invalid credentials.")
            return redirect('auth.login')

    def logout(request):
        logout(request)
        return redirect('auth.login')


class dashboard:
    @login_required(login_url='/auth/login')
    def dashboard(request):
        if request.user.is_superuser:
            tasks = Todo.objects.all().values()
        else:
            tasks = Todo.objects.filter(
                user_id_id=request.user.username).values()
        data = {
            'user': request.user,
            'tasks': tasks
        }
        return render(request, 'dashboard/dashboard.html', data)

    class tasks:
        def add_task_submit(request):

            todo = Todo()
            todo.user_id = request.user
            todo.task = request.POST['task']
            todo.date = request.POST['date']
            todo.save()

            messages.success(request, "Task added successfully.")
            return redirect('dashboard')

        def edit_task(request, id):

            todo = Todo.objects.get(id=id)

            data = {
                'user': request.user,
                'todo': todo
            }
            return render(request, 'dashboard/edit-task.html', data)

        def edit_task_submit(request):

            todo = Todo.objects.get(id=request.POST['id'])
            todo.task = request.POST['task']
            todo.date = request.POST['date']
            todo.save()

            messages.success(request, "Task update successfully.")
            return redirect('dashboard')

        def delete_task(request, id):

            todo = Todo.objects.get(id=id)
            todo.delete()

            messages.success(request, "Task deleted successfully.")
            return redirect('dashboard')
