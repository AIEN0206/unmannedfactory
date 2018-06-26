from rest_framework import serializers
from lumino.models import Drivelesscar


class DrivelesscarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drivelesscar
        fields = '__all__'
        # fields = ('id', 'song', 'singer', 'last_modify_date', 'created')