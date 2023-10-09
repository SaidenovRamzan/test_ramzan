from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response

from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer, UserListWithOrders
from order.permissions import IsOwnerOrReadOnly, AdultPermission


class UserProfileApiView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permissions = {
        'update': [IsOwnerOrReadOnly(), 
                   AdultPermission(),
                   ],
        'partial_update':[IsOwnerOrReadOnly(),
                          AdultPermission(),
                          ],
        'destroy':[IsOwnerOrReadOnly(), 
                   AdultPermission(),
                   ],
    }
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = UserListWithOrders(instance)
        response_data = serializer.data
        return Response(response_data)
      
    def perform_destroy(self, instance):
        user = User.objects.filter(username=instance.phone_number)
        user.delete()
        instance.delete()
        
    def get_permissions(self):
        if self.action in self.permissions:
            perm = self.permissions.get(self.action)
            return perm
        return super().get_permissions()
    