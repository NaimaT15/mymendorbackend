from rest_framework import serializers
from .models import User, admin, department

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=['first_name','last_name','email','identification_number', 'password','password2']

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = admin
        fields=['user_ID']

class RegistrationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model=User
        fields=['first_name','last_name','email','identification_number', 'password','password2']
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
        account.set_password(password)
        account.save()
        return account

class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields=('__all__')