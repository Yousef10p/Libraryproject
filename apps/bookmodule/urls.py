from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [ 
            path('', views.index), 
            path('index2/<int:val1>/', views.index2),
            path('<int:bookId>', views.viewbook)
]