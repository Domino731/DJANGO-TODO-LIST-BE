from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view(['GET'])
def api_home(request):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if request.method != 'GET':
        return Response({'message': 'GET is only allowed'}, status=405)
    if instance:
        data = {"TEST": 1}
    return Response(data)
