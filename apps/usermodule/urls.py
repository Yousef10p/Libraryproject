from . import views
from django.urls import path

urlpatterns = [
    path('lap8/task7',views.lap8_task7),
    
    
    path("create/",views.create,name="student.create"),
    path("read/",views.read,name="student.read"),
    path("update/<int:id>",views.update,name="student.update"),
    path("delete/<int:id>",views.delete,name="student.delete"),
    
     path("create2/",views.create2,name="student2.create"),
    path("read2/",views.read2,name="student2.read"),
    path("update2/<int:id>",views.update2,name="student2.update"),
    path("delete2/<int:id>",views.delete2,name="student2.delete"),
]