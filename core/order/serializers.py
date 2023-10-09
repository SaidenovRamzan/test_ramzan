from rest_framework import serializers
from multiupload.fields import MultiFileField
from order.models import Order, FileImageForOrder


class FileImageForOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileImageForOrder
        fields = ('order_file',)
        
        
class OrderSerializer(serializers.ModelSerializer):
    files = FileImageForOrderSerializer(many=True)

    class Meta:
        model = Order
        fields = ('order_number', 'user', 'status', 'descrption', 'files')
        read_only_fields = ['order_number']
