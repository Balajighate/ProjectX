from django.urls import path

from . import views
# create application urls

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.my_login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('viewrecord/<int:pk>',views.viewrecord,name='viewrecord'),
    path('updaterecord/<int:pk>',views.updaterecord,name='updaterecord'),
    path('deleterecord/<int:pk>',views.deleterecord,name='deleterecord'),
    path('logout',views.logout,name='logout'),
    

]