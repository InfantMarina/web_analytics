from Tracking_app import models
from rest_framework import serializers

class SerializingTables(serializers.ModelSerializer):
    class Meta:
        model = models.WA_Timelog
        fields = "__all__"