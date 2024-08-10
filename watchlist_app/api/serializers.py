from rest_framework import serializers


def name_length(value):
    if len(value) < 2:
        raise serializers.ValidationError("Name is too short!")
    
    
class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(validators=[name_length])
    description = serializers.CharField()
    active = serializers.BooleanField()