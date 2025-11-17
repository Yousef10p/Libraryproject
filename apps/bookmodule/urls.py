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
            
            #---------------- LAB 8 -------------------
            path('lap8/task1', views.lap8_task1, name='books.lap8_task1'),
            path('lap8/task2', views.lap8_task2, name='books.lap8_task2'),
            path('lap8/task3', views.lap8_task3, name='books.lap8_task3'),
            path('lap8/task4', views.lap8_task4, name='books.lap8_task4'),
            path('lap8/task5', views.lap8_task5, name='books.lap8_task5'),
            
            #---------------- LAB 9 -------------------
            path('lap9/task1', views.lap9_task1, name='books.lap9_task1'),
            path('lap9/task2', views.lap9_task2, name='books.lap9_task2'),
            path('lap9/task3', views.lap9_task3, name='books.lap9_task3'),
            path('lap9/task4', views.lap9_task4, name='books.lap9_task4'),
            path('lap9/task5', views.lap9_task5, name='books.lap9_task5'),
            path('lap9/task6', views.lap9_task6, name='books.lap9_task6'),
            
            
            #---------------- LAB 10 -------------------
            path('lap10/task1',views.lap10_task1, name='books.lap10_task1'),
            path('lap10/task2',views.lap10_task2, name='books.lap10_task2'),
            path('lap10/task3/<int:id>',views.lap10_task3, name='books.lap10_task3'),
            path('lap10/task4/<int:id>',views.lap10_task4, name='books.lap10_task4'), 
            #---------------- LAB 10 part 2 -------------------
            path('lap10_2/task1',views.lap10_2_task1, name='books.lap10_2_task1'),
            path('lap10_2/task2',views.lap10_2_task2, name='books.lap10_2_task2'),
            path('lap10_2/task3/<int:id>',views.lap10_2_task3, name='books.lap10_2_task3'),
            path('lap10_2/task4/<int:id>',views.lap10_2_task4, name='books.lap10_2_task4'), 
]           