from rest_framework import serializers
from django.contrib.auth import authenticate

from MymenderProject.decorators import customer_required
from .models import User, admin, department,customer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['first_name','last_name','email','identification_number','password','is_staff']

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin
        fields=['user_ID']

class RegistrationSerializer(serializers.ModelSerializer):
    #password=serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2=serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model=User
        fields=['first_name','last_name','email','identification_number','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self):
        account=User(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            identification_number=self.validated_data['identification_number'],
        )
        # cust=customer(
        #     user_ID=self.validated_data['identification_number'],
        # )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'password doesnot match'})
        account.is_customer=True
        account.set_password(password)
        account.is_staff=False
        account.save()
        # cust.save()
        return account



class RegisteradminSerializer(serializers.ModelSerializer):
    #password=serializers.CharField(style={'input_type': 'password'}, write_only=True)
    password2=serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model=User
        fields=['first_name','last_name','email','identification_number','password','password2']
        extra_kwargs={
            'password':{'write_only':True}
        }

    def save(self):
        account=User(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            identification_number=self.validated_data['identification_number'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'password doesnot match'})
        account.is_admin=True
        account.set_password(password)
        account.is_staff=True

        account.save()
        return account


class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields=('__all__')

class UserLoginSerializer(serializers.Serializer):
    identification_number = serializers.CharField(required=True)
    password = serializers.CharField(style={'input_type': 'password'},required=False, allow_null=True, write_only=True)

    def validate(self, attrs):
        identification_number = attrs.get('identification_number')
        user = User.objects.filter(identification_number=identification_number).exists()
        if user:
            return attrs
        else:
            msg = {
                'detail': 'User does not exists.', 'register': True}
            raise serializers.ValidationError(msg, code='authorization')


class UserLogoutSerializer(serializers.Serializer):
    # phone_number = serializers.CharField(max_length=11, required=True)

    def validate(self, attrs):
        identification_number = attrs.get('identification_number')
        user = User.objects.filter(identification_number=identification_number).exists()
        if user:
            return attrs
        else:
            msg = {
                'detail': 'User does not exists.', 'register': True}
            raise serializers.ValidationError(msg, code='authorization')