from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
            # ---------------- LAB 3 ------------------- 
            # path('', views.index), 
            # path('index2/<int:val1>/', views.index2),
            # path('<int:bookId>', views.viewbook)
            
            
            # ---------------- LAB 4 -------------------
            path('', views.index, name='books.index'),
            path('list_books/', views.list_books, name='books.list_books'),
            path('<int:bookId>/', views.viewbook, name='books.view_one_book'),
            path('aboutus/',views.aboutus,name='books.aboutus'),
            
            # ---------------- LAB 5 -------------------
            path('html5/links',views.links,name='books.links'),
            path('html5/text/formatting',views.text_formatting,name='books.text_formatting'),
            path('html5/listing',views.listing,name='books.listing'),
            path('html5/tables',views.tables,name='books.tables'),
            
            # ---------------- LAB 6 -------------------
            path('search',views.search, name='books.search'),
            
            #---------------- LAB 7 -------------------
            path('simple/query', views.simple_query, name='books.simple_query'),
            path('complex/query', views.complex_query, name='books.complex_query'),
]       