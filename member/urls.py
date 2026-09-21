from django.urls import path
from . import views

app_name = 'member'

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.login_form, name = "login_form"),
    path('login/', views.login, name = "login"),
    path('logout/', views.logout, name = "logout"),
    path('register/', views.insert_form, name = "register"),
    path('home/', views.home, name='home'),
    path('mypage/', views.mypage, name='mypage'),
    path('mypage/update/', views.mypageUpdate, name='mypageUpdate'),
    path('mypage/delete/', views.mypageDelete, name='mypageDelete'),
    #path('insert/', views.insert_form, name = 'insert_form'),
    path('insert/save', views.insert, name = 'insert'),
    #path('delete/<int:id>', views.delete_form, name = 'delete_form'),
    path('delete/<int:member_id>', views.delete, name = 'delete'),
    path('update/', views.update_form, name = 'update_form'),
    path('update/upt', views.update, name = 'update'),
]