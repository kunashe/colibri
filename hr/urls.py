from django.urls import include, path
from rest_framework import routers
from hr import people
from hr.people import views

router = routers.DefaultRouter()
router.register(r'people', views.PeopleViewSet,basename='People')

urlpatterns = [
    path('', include(router.urls)),
    path('update-person/<str:id>/',views.update_person,name="update_person"),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]