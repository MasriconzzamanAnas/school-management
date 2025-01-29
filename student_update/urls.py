from django.urls import path
from . import views

urlpatterns =[
    path('', views.home.as_view(), name="home"),
    path('studentList/', views.studentList.as_view(), name="studentList"),
    path('add_student/', views.add_student.as_view(), name="add_student"),
    path('update_student/<int:id>', views.update_student.as_view(), name='update_student'),
    path('delete_student/<int:id>', views.delete_student.as_view(), name='delete_student'),
]