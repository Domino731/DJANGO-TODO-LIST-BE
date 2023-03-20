import json

from django.http import JsonResponse

def api_home(request):
    print(request.GET) # url params
    body = request.body
    data = {}
    try:
       data = json.loads(request.body)
    except:
        pass

    return JsonResponse({"message": "success", "data": data})