from django.urls import include, path
from rest_framework import routers
from hr import people
from hr.people import views

router = routers.DefaultRouter()
router.register(r'people', views.PeopleViewSet,basename='people')
router.register(r'stats', views.StatsViewSet,basename='stats')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]