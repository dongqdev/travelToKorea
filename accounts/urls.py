from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('mypage/', views.mypage, name="mypage"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<str:username>/', views.mypage, name='mypage')
    ]

