from django.http import JsonResponse
import json


def home(request):
    Product
    body = request.body
    json_data = {}
    print(request.GET)  # url query params
    try:
        json_data = json.loads(body)
    except:
        pass
    print("json_data: ", json_data)
    json_data['query'] = dict(request.GET)
    json_data['headers'] = dict(request.headers)
    return JsonResponse(json_data)
