import json

from django.http import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
from products.models import Product


def api_home(request):
    model_data = Product.objects.all().order_by('?').first()
    data = {}
    if model_data:
        data = model_to_dict(model_data, fields=['title', 'id', 'content', 'price'])
    return JsonResponse(data)
    #     json_data_str = json.dumps(data)
    # return HttpResponse(json_data_str, headers={'content-type': 'application/json'})
