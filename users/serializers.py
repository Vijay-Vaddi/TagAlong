"""Serializers for user API view"""
from django.contrib.auth import get_user_model
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """Serializer for user object"""
    class Meta:
        model = get_user_model()
        fields = ['email', 'first_name', 'last_name',
                  'password']
        extra_kwargs = {"password":
                        {'write_only':True, 'min_length':5}
                    }

    def create(self, validated_data):
        """create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        """fetch and updated authenticated user"""
        password = validated_data.pop('password', None)
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()
        return user

