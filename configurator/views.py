from django.http import JsonResponse
from django.shortcuts import render
from .models import Config
from api import views as api
import json

# Create your views here.
def myConfigs(request):
    try:
        configs = json.loads(JsonResponse(api.getConfigByUser(request, request.user.id)))
        configs_by_id = {config['id']: config for config in configs}
    except Exception as e:
        render(request, 'error.html', {'error': str(e)})
    render(request, 'config-dashboard.html', {'configs_by_id': configs_by_id})

def deleteConfig(request):
    pass
def newConfig(request):
    render(request, 'config.html')

def modifyConfig(request, id):
    # we are using the API here so that any updates to the API will replicate
    
    try:
        config = json.loads(JsonResponse(api.getConfigByID(request, id)))
    except Exception as e:
        render(request, 'error.html')

    render(request, 'config.html', config)
    