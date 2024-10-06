from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login',views.login,name='logins'),
    path('signin',views.signin, name='sign'),
    path('log',views.logout,name='logout'),
    path('q',views.quest,name='question'),
    path('ans',views.calculate,name='answer'),

]