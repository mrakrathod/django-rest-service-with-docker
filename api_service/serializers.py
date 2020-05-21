from rest_framework import serializers
from .models import BirthDay


class BirthdayModelSerializer(serializers.ModelSerializer):
    """
    It's the birthday model serializer to serialize all the birthday model data.
    """
    birthday = serializers.DateField(format='%d.%m.%Y')

    class Meta:
        model = BirthDay
        fields = '__all__'
        read_only_fields = [
            'id',
            'created_at',
            'modified_at'
        ]
