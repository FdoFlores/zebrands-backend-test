from rest_framework import serializers
from .models import Brand, Product
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Group, Permission

class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_name', 'email')

###############   # Overrided user functions  # ###############
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        #set_password already uses the make_password so it saves hashed password :]
        user.set_password(password)
        user.save()
        return user
    
    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        #Update every field in validated_data
        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        #Hash the password with the make_password
        if password is not None:
            instance.password = make_password(password)

        instance.save()
        return instance