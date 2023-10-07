from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from order.models import Order, FileImageForOrder
from order.serializers import FileImageForOrderSerializer, OrderSerializer
from rest_framework.response import Response


class OrderViewSets(viewsets.ModelViewSet):
    # parser_classes = (MultiPartParser,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated, )
    
    def create(self, request, *args, **kwargs):
        # a = self.serializer.validated_data()
        # print(a)
        return super().create(request, *args, **kwargs)


class Test(APIView):
    def get(self, request, format=None):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)