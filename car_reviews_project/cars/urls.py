from rest_framework import routers
from django.urls import path
from .views import CountryViewSet, ManufacturerViewSet, CarViewSet, CommentViewSet, export_data

router = routers.DefaultRouter()
router.register(r'countries', CountryViewSet)
router.register(r'manufacturers', ManufacturerViewSet)
router.register(r'cars', CarViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('api/export/<str:model>/<str:format>/', export_data),
] + router.urls
