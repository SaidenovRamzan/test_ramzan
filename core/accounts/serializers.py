from rest_framework import serializers

from accounts.models import UserProfile
from django.contrib.auth.models import User
from datetime import datetime

 
class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'phone_number', 'date_of_birth', 'profile_picture', 'password', 'age')
        read_only_fields = ['age']
        
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['phone_number'],
            password=validated_data['password']
        )
        
        profile = UserProfile(
            user=user,
            phone_number=validated_data['phone_number'],
            date_of_birth=validated_data['date_of_birth'],
            profile_picture=validated_data.get('profile_picture'),
            age = self.get_age(validated_data['date_of_birth'])
        )
        profile.save()
        return profile
    
    def get_age(self, birth_date):
        if birth_date:
            current_date = datetime.now().date()
            age = current_date.year - birth_date.year
            age -= (
                (current_date.month < birth_date.month)
                if current_date.month != birth_date.month
                else current_date.day < birth_date.day
            )
            return age
        else:
            return 0

    

    
