from rest_framework import serializers
from sample_model.models import SampleModel


class SampleModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = SampleModel
        fields = "__all__"
