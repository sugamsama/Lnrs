from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoyaltyProgramViewSet
router = DefaultRouter()
router.register(r'loyalty_programs', LoyaltyProgramViewSet)
urlpatterns = [
    path('', include(router.urls)),
]