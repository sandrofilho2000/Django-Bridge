from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_api_key.permissions import HasAPIKey
from sample_model.models import SampleModel
from sample_model.serializers import SampleModelSerializer
from django.http import HttpResponse
from django.template import loader


def index(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


@api_view(["GET"])
@permission_classes([HasAPIKey])
def sample_model_viewer(request):
    sample_model_instance = SampleModel.objects.first()
    sample_model = SampleModelSerializer(sample_model_instance).data
    response_data = {"data": sample_model["sample_field"]}
    return Response(response_data)
