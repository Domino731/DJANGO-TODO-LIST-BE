import json
from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer


@api_view(['GET'])
def api_home(request):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if request.method != 'GET':
        return Response({'message': 'GET is only allowed'}, status=405)
    if instance:
        # data = model_to_dict(instance, fields=['title', 'id', 'content', 'price', 'sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={'content-type': 'application/json'})
