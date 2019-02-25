from django.contrib import admin
from django.urls import path
import app_1.views 

urlpatterns = [
    path('<int:blog_id>/', app_1.views.detail, name = 'detail'),
    path('new/', app_1.views.new, name = 'new'),
    path('create/', app_1.views.create, name = 'create'),
    path('newblog/', app_1.views.blogpost, name = 'newblog'),
    path('about/', app_1.views.about, name = 'about'),
]