from django.db import models
from rest_framework import serializers
# Create your models here.
class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=20)
    email = models.CharField(max_length=20)
    phone = models.CharField(max_length=10, default='00000000')
    address = models.CharField(max_length=30, default='no-address')
    
#this is the serializer for the contact model, it explains what fields should be included into the json
class ContactSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Contact
        fields = ('id','full_name','email')
    