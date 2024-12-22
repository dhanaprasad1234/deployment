from django.urls import path,include
from .views import home,authview,logout,createstore,login

app_name = 'assignapp'
urlpatterns = [path('home/', home,name='home'),
                path('authview/', authview,name='authview'),
               path('login/',login,name = 'login'),
               path('logout/',logout,name ='logout'),
                path('createstore/',createstore,name ='createstore'),
               path('accounts/', include('django.contrib.auth.urls'))]