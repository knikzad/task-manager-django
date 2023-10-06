from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import JsonResponse
from datetime import date
from .forms import TaskForm, SignUpForm

from .models import Task
# Create your views here.


def home(request):
    if request.user.is_authenticated:
      user = request.user
      tasks = Task.objects.filter(user=user).order_by('due_date')
      today = date.today()
      return render(request, 'tasks/home.html', {
          'tasks': tasks,
        'today': today
      })
    else:
        messages.success(request, "You must be logged in to view home page!")
        return redirect('login')
      
def task_ajax(request):
    user = request.user
    tasks = Task.objects.filter(user=user)
    
    task_list = []
    for task in tasks:
        task_list.append({
            'id': task.id,
            'title': task.title,
            'status': task.status,
            'due_date': task.due_date.strftime('%Y-%m-%d'),
        })
    
    return JsonResponse({'tasks': task_list})


def add_task(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = TaskForm(request.POST)
            if form.is_valid():
                form.clean_due_date()
                task = form.save(commit=False)
                task.user = request.user
                task.save()
                messages.success(request, "Task has been successfully Added!")
                return redirect('home')
        else:
            form = TaskForm()
        return render(request, 'tasks/add_task.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to add task!")
        return redirect('login')


def update_task(request, pk):
    if request.user.is_authenticated:
        current_task = Task.objects.get(id=pk)
        form = TaskForm(request.POST or None, instance=current_task)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "The task has been successfully updated!")
            return redirect('home')
        return render(request, 'tasks/update_task.html', {'form': form})
    else:
        messages.success(request, "You must be logged in to upadte task!")
        return redirect('login')
      
def update_task_status(request, pk):
  current_task = Task.objects.get(pk = pk)
  status = request.POST.get('status')
  if status in ['completed', 'in_progress']:
      current_task.status = status
      current_task.save()
      return JsonResponse({'success': True})
  else:
      return JsonResponse({'success': False})

def task_detail(request, pk):
    if request.user.is_authenticated:
        task = Task.objects.get(id=pk)
        return render(request, 'tasks/task_detail.html', {'task': task})
    else:
        messages.success(request, "You must be logged in to view that!")
        return redirect('login')


def delete_task(request, pk):
    if request.user.is_authenticated:
        task = Task.objects.get(id=pk)
        task.delete()
        messages.success(request, "The task has been successfully deleted!")
        return redirect('home')
    else:
        messages.success(request, "You must be logged in to delete a task!")
        return redirect('login')


def register_user(request):
  if request.method == 'POST':
    form = SignUpForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data['username']
        password = form.cleaned_data['password1']
        user = authenticate(username = username, password = password)
        login(request, user)
        messages.success(request, "You have successfully registered!")
        return redirect('home')
  else:
    form = SignUpForm()
  return render(request, 'tasks/register.html', {'form':form})


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "You have successfully logged in!")
            return redirect('home')
        else:
            messages.success(request,
                             "Incorrect username or password! Try again...")
            return redirect('login')
    else:
        return render(request, 'tasks/login.html')


def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect('login')
