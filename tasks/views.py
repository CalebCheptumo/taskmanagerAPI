from django.urls import path , include
from rest_framework.routers import DefaultRouter
from tasks.views import TaskViewSet

# Create your views here.
router = DefaultRouter()
router.register(r'tasks', TaskViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
