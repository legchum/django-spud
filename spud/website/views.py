from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm
from django.contrib.auth.decorators import login_required
from .models import Record, Dexter_data

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                auth_login(request, user)
                return redirect('')  # Redirect to home page after successful login
            else:
                messages.error(request, 'Invalid username or password')

    context = {"form": form}
    return render(request, 'pages/login.html', context=context)

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged Out Successfully!')
    return redirect('')

def register(request):
    form = CreateUserForm()

    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully! You can now log in.')
            return redirect('login')

    context = {"form": form}

    return render(request,"pages/register.html",context=context)

def doakes(request):
    return render(request, 'pages/doakes.html')

@login_required(login_url="login")
def dexter_data(request):
    my_dexter_data = Dexter_data.objects.all()
    context = {'Dexter_data':my_dexter_data}
    return render(request, 'pages/dexter_data.html', context=context)

@login_required(login_url="login")
def dashboard(request):

    my_records = Record.objects.all()
    context = {'Records':my_records}
    return render(request, 'pages/dashboard.html', context=context)

@login_required(login_url="login")
def create_record(request):
    form = CreateRecordForm()
    if request.method == "POST":
        form = CreateRecordForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Record created successfully!')
            return redirect("dashboard")

    context = {'create_form':form}
    return render(request, 'pages/create_record.html', context=context)

@login_required(login_url="login")
def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = UpdateRecordForm(instance=record)

    if request.method == "POST":
        form = UpdateRecordForm(request.POST, instance=record)
        if form.is_valid:
            form.save()
            messages.success(request, 'Record updated successfully!')
            return redirect("dashboard")
    context = {'update_form': form}
    return render(request, 'pages/update_record.html', context=context)

@login_required(login_url="login")
def view_record(request, pk):
    record = Record.objects.get(id=pk)
    context = {'record':record}
    return render(request, 'pages/view_record.html', context=context)

@login_required(login_url="login")
def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    record.delete()
    messages.success(request, 'Record deleted successfully!')
    return redirect('dashboard')
