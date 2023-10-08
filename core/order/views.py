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
    permission_classes = (IsAuthenticated, )
    
    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.data.get('user'))
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)
        
        order = Order.objects.create(user=User.objects.get(id=user.id))
        
        files = request.data.pop('files')
        for file in files:
            FileImageForOrder.objects.create(order=order, order_file=file.get('order_file'))
        return Response(OrderSerializer(order).data)


# class Test(APIView):
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
#                 FileImageForOrder.objects.create(order=order, order_file=file.get('order_file'))
#             return Response(request.data)