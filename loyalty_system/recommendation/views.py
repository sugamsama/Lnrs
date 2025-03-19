from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Recommendation
from .serializers import RecommendationSerializer

class RecommendationViewSet(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    permission_classes = [IsAuthenticated]
class RecommendationDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recommendation.objects.all() 
    serializer_class = RecommendationSerializer
    permission_classes = [IsAuthenticated]