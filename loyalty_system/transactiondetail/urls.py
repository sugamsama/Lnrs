from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionDetailViewSet

router = DefaultRouter()
router.register(r'transactiondetails', TransactionDetailViewSet)
urlpatterns = [
    path('', include(router.urls)),
]