from rest_framework import serializers
from multiupload.fields import MultiFileField
from order.models import Order

class OrderSerializers(serializers.ModelSerializer):
    file = MultiFileField(min_num=0, max_num=3)
    class Meta:
        model = Order
        fields = ['order_number', 'user', 'status', 'file']
        read_only_fields = ['order_number']
        