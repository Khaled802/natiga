from rest_framework import serializers
from .models import Degree

class DegreeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Degree
        fields = ('seating_number', 'name', 'student_case', 'total_degree')


class GettingResultBySeatingNumber(serializers.Serializer):
    seating_number = serializers.IntegerField(write_only=True, required=True)


class GettingResultByName(serializers.Serializer):
    name = serializers.CharField(required=True)