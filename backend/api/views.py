import json

from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from products.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_home(request):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if request.method != 'POST':
        return Response({'message': 'GET not allowed'}, status=405)
    if model_data:
        data = model_to_dict(model_data, fields=['title', 'id', 'content', 'price'])
    return Response(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={'content-type': 'application/json'})
