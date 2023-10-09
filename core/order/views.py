from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from order.models import Order, FileImageForOrder
from django.contrib.auth.models import User

from order.serializers import FileImageForOrderSerializer, OrderSerializer
from rest_framework.response import Response
from rest_framework import status


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    # permission_classes = (IsAuthenticated, )
    
    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.data.get('user'))
            order = Order.objects.create(user=User.objects.get(id=user.id))
        except User.DoesNotExist:
            # return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)
            ...
        
        files = request.data.pop('files')
        for file in files:
            FileImageForOrder.objects.create(order=order, order_file=file.get('order_file'))
        return Response(OrderSerializer(order).data)
    
    def list(self, request, *args, **kwargs):
        if request.user.id:
            queryset = self.filter_queryset(self.get_queryset())
        else:
            queryset = self.filter_queryset(Order.objects.filter(user=None))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

class Test(APIView):
    ...
#     def get(self, request, format=None):
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, format=None):
#             print(request.data,',===============')
#             files = request.data.pop('files')
#             user = User.objects.get(id=request.data.get('user'))
#             print(files,'--------------------------')
#             order = Order.objects.create(user=User.objects.get(id=user.id))
#             for file in files:
#                 print(file.get('order_file'),'999999999999999999999999999999')
#                 FileImageForOrder.objects.create(order=order, order_file=file.get('order_file')) http://localhost:8000/api/v1/order/7/
#             return Response(request.data)