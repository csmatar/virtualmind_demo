from rest_framework import fields, serializers

from .models import Core

class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Core
        fields = ("id", "name")
        extra_kwargs = {"id": {'read_only':True}}
