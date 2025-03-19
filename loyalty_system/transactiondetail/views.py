from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import TransactionDetail
from .serializers import TransactionDetailSerializer

# Create your views here.
class TransactionDetailViewSet(generics.ListCreateAPIViews):
    queryset = TransactionDetail.objects.all()
    serializer_class = TransactionDetailSerializer
    permission_classes = [IsAuthenticated]
class TransactionDetailDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransactionDetail.objects.all()
    serializer_class = TransactionDetailSerializer
    permission_classes = [IsAuthenticated]