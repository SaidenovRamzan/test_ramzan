from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response

from accounts.models import UserProfile
from accounts.serializers import UserProfileSerializer


class UserProfileApiView(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        age = self.get_age(serializer.data.get('date_of_birth'))
        response_data = serializer.data
        response_data['age'] = age
        return Response(response_data)
      
    def perform_destroy(self, instance):
        user = User.objects.filter(username=instance.phone_number)
        user.delete()
        instance.delete() 
     

