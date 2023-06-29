from django.contrib import admin
from django.urls import path
from myapp import views
urlpatterns = [
    path('', views.index, name='home'),
    path('explore', views.explore, name='explore'),
    path('contact', views.contact, name='contact'),
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('add_blog/', views.add_blog, name="add_blog"),
    path('my_account/', views.my_account, name="my_account"),
    path('read/<slug>', views.read, name="read"),
    path('update/<slug>', views.update, name="update"),
    path('delete/<slug>', views.delete, name="delete")
]
