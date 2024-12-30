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
def getConfigByUser(request, userID):
    # by default this will just return the user's specific configs, but it can be used to drill into one specific one if the id 
    # or userid is provided
    # TODO add a setting for whether config is private or not
    # TODO add check for userid
    items = Config.objects.filter(userID=userID)
    serializer = ConfigSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getConfigByID(request, id):
    config = Config.objects.get(id=id)
    serializer = ConfigSerializer(config)
    return Response(serializer.data)


@api_view(['POST'])
def addConfig(request):
    serializer = ConfigSerializer(data=request.data)
    if serializer.is_valid():
        config = serializer.save()
    return Response({"id": config.id, **serializer.data})

@api_view(['PUT'])
def modifyConfig(request, id):
    try:
        config_instance = Config.objects.get(id=id)
    except:
        return Response({'id-error': 'That ID does not exist in the database'}, status=status.HTTP_204_NO_CONTENT)

    serializer = ConfigSerializer(config_instance, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def downloadConfig(request, id):
    user = request.user
    # TODO implement queue and taskid number <rahul@tucanalinu.org>
    # TODO 3 iso builds per user <rahul@tucanalinux.org>
