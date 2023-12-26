from rest_framework import serializers
from .models import chambeador

class chambeadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = chambeador
        fields = '__all__'
