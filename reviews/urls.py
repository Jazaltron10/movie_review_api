from django.urls import include, path 
from .views import ReviewViewSet
from rest_framework.routers import DefaultRouter


# Initialize DRF router to manage routes for our ViewSet
router = DefaultRouter()
router.register('reviews', ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),  # Include all router-generated routes
]

