from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import LoyaltyProgram
from .serializers import LoyaltyProgramSerializer

class LoyaltyProgramViewSet(generics.ListCreateAPIView):
    queryset = LoyaltyProgram.objects.all()
    serializer_class = LoyaltyProgramSerializer
    permission_classes = [IsAuthenticated]
class LoyaltyProgramDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = LoyaltyProgram.objects.all()
    serializer_class = LoyaltyProgramSerializer
    permission_classes = [IsAuthenticated]