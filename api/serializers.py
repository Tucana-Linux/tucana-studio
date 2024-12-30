from rest_framework import serializers
from configurator.models import Config

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'