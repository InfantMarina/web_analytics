from Tracking_app import models
from rest_framework import serializers

class SerializingTables(serializers.ModelSerializer):
    class Meta:
        model = models.WA_Visitors
        fields = ['ip_address','city','region','country','loc','org','postal','timezone']


