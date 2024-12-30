from rest_framework.response import Response
from rest_framework.decorators import api_view
from configurator.models import Config
from .serializers import ConfigSerializer
from rest_framework import status

@api_view(['GET'])
def getPublicConfigs(request):
    items = Config.objects.all()
    serializer = ConfigSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getSpecificConfigs(request):
    # by default this will just return the user's specific configs, but it can be used to drill into one specific one if the id 
    # or userid is provided
    # TODO add a setting for whether config is private or not
    id = request.query_params_get('id')
    user = request.query_params_get('user')
    if id is not None:
        item = Config.objects.filter(id=id)
        serializer = ConfigSerializer(item)
        return Response(serializer.data)
    if user is None:
        user = request.user

    items = Config.objects.filter(userID=user)
    serializer = ConfigSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addConfig(request):
    serializer = ConfigSerializer(data=request.data)
    if serializer.is_valid():
        config = serializer.save()
    return Response({"id": config.id, **serializer.data})

@api_view(['PUT'])
def modifyConfig(request):
    id = request.query_params_get('id')
    if id is None:
        return Response({'param-error': 'Missing ID'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = ConfigSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def downloadConfig(request):
    id = request.query_params_get('id')
    if id is None:
        return Response({'param-error': 'Missing ID'}, status=status.HTTP_400_BAD_REQUEST)
    user = request.user
    # TODO implement queue and taskid number <rahul@tucanalinu.org>
    # TODO 3 iso builds per user <rahul@tucanalinux.org>
