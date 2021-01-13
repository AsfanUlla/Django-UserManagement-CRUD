from rest_framework import serializers
from usrmgmt.models import Users

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Users
        fields = ('U_ID',
                  'NAME',
                  'EMAIL',
                  'PHONE',
                  'ADDR')