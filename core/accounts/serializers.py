from rest_framework import serializers
from accounts.models import UserProfile
from django.contrib.auth.models import User

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'phone_number', 'date_of_birth', 'profile_picture', 'password')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['phone_number'],
            password=validated_data['password']
        )

        profile = UserProfile(
            user=user,
            phone_number=validated_data['phone_number'],
            date_of_birth=validated_data['date_of_birth'],
            profile_picture=validated_data.get('profile_picture')
        )

        profile.save()

        return profile
