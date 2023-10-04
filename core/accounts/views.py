from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from datetime import datetime

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
         
    def get_age(self, birth_date:str)->int:
        date_of_birth = datetime.strptime(birth_date, "%Y-%m-%d")
        current_date = datetime.now()
        age = current_date.year - date_of_birth.year
        age -= ((current_date.month < date_of_birth.month) if current_date.month != date_of_birth.month else current_date.month < date_of_birth.month)
        return age

