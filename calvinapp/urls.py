
from django.contrib import admin
from django.urls import path
from calvinapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('collection/', views.collection),
    path('bugatti/', views.bugatti),
    path('mclaren/', views.mclaren),
    path('rolls royce/', views.rollsroyce),
]
