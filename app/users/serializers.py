from rest_framework import serializers
from .models import UserAccount


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ('email','name','password')
        extra_kwargs = {'password':{'write_only':True}}

    def create(self,validate_data):
        password = validate_data.pop('password',None)
        instance = self.Meta.model(**validate_data)
        if password is not None:
            instance.set_password(password)
        instance.save()

        return instance        

