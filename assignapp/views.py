from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import store
from .form import StoreForm, LoginForm, User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
@login_required
def home(request):
   sort_by = request.GET.get('sort', 'Created_at')
   if sort_by not in ['Name', 'Created_at', 'Price']:
       sort_by = 'Created_at'

   store1 = store.objects.filter(user_id=request.user.id).order_by(sort_by)

   paginator = Paginator(store1, 5)
   page_number = request.GET.get('page', 1)

   try:
       page_obj = paginator.get_page(page_number)
   except (EmptyPage, PageNotAnInteger):
       page_obj = paginator.get_page(1)  # Fallback to the first page if invalid

   context = {
       'page_obj': page_obj,
       'sort_by': sort_by,
       'store1' : store1 ,
   }
   return render(request, 'registration/home.html', context)
def authview(request):
    if request.method == 'POST':
        store = User(request.POST)

        if store.is_valid():
            user= store.save()
            login(request)
            return redirect('assignapp:home')

    else:
        store = User()
    return render(request, 'registration/signup.html', {"store": store})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        print(form)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request,username=username,password=password)
            print(user)
            if user is not None:
                login(request)
                return redirect('assignapp:home')
    else:
        form = LoginForm()
    return render(request,'registration/login.html',{'form':form})

def logout(request):
    if request.method == 'POST' :
        logout(request)
        return redirect('assignapp:login')
    return redirect('assignapp:login')

@login_required
def createstore(request):
    if request.method == 'POST':
        store = StoreForm(request.POST)
        if store.is_valid():
            form=store.save(commit=False)
            form.user = request.user
            form.save()
            return redirect('assignapp:home')
    else:
        store = StoreForm()
    return render(request,'registration/storeform.html',{'store':store})
