from rest_framework import viewsets
from rest_framework.parsers import MultiPartParser
from order.models import Order
from order.serializers import OrderSerializers

class OrderViewSets(viewsets.ModelViewSet):
    parser_classes = (MultiPartParser,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializers
    