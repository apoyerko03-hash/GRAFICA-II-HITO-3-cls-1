import requests
from rest_framework.decorators  import api_view
from rest_framework.response import Response

#voy a usar el meotodo get para consumir la api externa 
@api_view(['GET'])
def obtener_posts(request):
    url = "https://dog.ceo/api/breeds/image/random"
    response = requests.get(url)
    if response.status_code == 200:
        return Response(response.json())
    return Response({"error": "fallo"}, status=500)

# POST de creación hacia API externa
@api_view(['POST'])
def crear_post(request):
    url = "https://dog.ceo/api/breeds/image/random"
    data = request.data

    response = requests.post(url, json=data)

    return Response(response.json())