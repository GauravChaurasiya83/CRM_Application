from django.urls import path
from webapp.views import *

urlpatterns = [

    path('',home,name=""),
    path('register/',register,name = "register"),
    path('login/',my_login,name='login'),
    
    path('logout/',user_logout,name='logout'),

    # CRUD
    path('dashboard',dashboard,name='dashboard'),
    path('create_record',create_record,name = 'create_record'),
    path('update_record/<int:pk>',update_record,name = 'update_record'),
    path('record/<int:pk>',singular_view_record,name = 'record'),
    path('delete/<int:pk>',delete_record,name = 'delete_record'),
]    