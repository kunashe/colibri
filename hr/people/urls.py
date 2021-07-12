from django.urls import path
from .import views

urlpatterns = [

    path('update-person/<str:id>/',views.update_person,name="update_person")
]

