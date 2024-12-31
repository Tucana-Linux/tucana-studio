from rest_framework import serializers
from configurator.models import Config

class ConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'
        read_only_fields = ('userID', )