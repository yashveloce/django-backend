from django.urls import path
from crudapp import views

urlpatterns = [
    path("createstudent/", views.StudentCRUD.as_view(),name="create_student"),
    path("readstudent/", views.StudentCRUD.as_view(),name="read_student"),
    path("updatestudent/", views.StudentCRUD.as_view(),name="update_student"),
    path("deletestudent/", views.StudentCRUD.as_view(),name="delete_student"),
]