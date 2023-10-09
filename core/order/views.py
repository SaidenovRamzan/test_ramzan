from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response

from order.serializers import OrderSerializer
from order.models import Order, FileImageForOrder
from order.permissions import IsOwnerOrReadOnly, AdultPermission


class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permissions = {
        'create': [permissions.AllowAny(), 
                   AdultPermission(),
                   ],
        'update': [IsOwnerOrReadOnly(), 
                   AdultPermission(),
                   ],
        'partial_update':[IsOwnerOrReadOnly(),
                          AdultPermission(),
                          ],
        'destroy':[IsOwnerOrReadOnly(), 
                   AdultPermission(),
                   ],
        'list':[permissions.AllowAny(), 
                AdultPermission(),
                ],
        'retrieve':[permissions.AllowAny(), 
                    AdultPermission(),
                    ]
    }
    
    def get_permissions(self):
        if self.action:
            return self.permissions.get(self.action)
        return [permissions.AllowAny()]
    
    def create(self, request, *args, **kwargs):
        try:
            user = User.objects.get(id=request.data.get('user'))
            order = Order.objects.create(user=User.objects.get(id=user.id))
        except User.DoesNotExist:
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
