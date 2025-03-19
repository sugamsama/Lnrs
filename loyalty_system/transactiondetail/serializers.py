from rest_framework import serializers
from .models import TransactionDetail

class TransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDetail
        fields = ['id', 'transaction_id', 'product_id', 'quantity', 'subtotal']