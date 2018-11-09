#-*-coding:utf-8-*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

import json

# Create your views here.
@csrf_exempt
def getSpecies(request):
    print(request.body)
    recv_data = json.loads(request.body.decode('utf-8'))
    dateRange = recv_data['dateRange']
    print(dateRange)
    send_data = {}

    send_data['userNum'] = 1000
    send_data['mostVisited'] = "大灵猫"
    send_data['visitedNum'] = [
        {"value": 235, "name": '动物'},
        {"value": 710, "name": '植物'},
        {"value": 534, "name": '昆虫'},
        {"value": 153, "name": '化石'}
    ]

    if dateRange == 3:
        send_data['visitedNum'] = [
        {"value": 525, "name": '动物'},
        {"value": 710, "name": '植物'},
        {"value": 234, "name": '昆虫'},
        {"value": 453, "name": '化石'}
    ]

    response = HttpResponse(json.dumps(send_data), content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'       # 跨域头部
    response['Access-Control-Allow-Headers'] = '*'
    return response

@csrf_exempt
def getAges(request):
    send_data = {}

    send_data['ageNum'] = [
        {"value": 335, "name": '10岁及以下'},
        {"value": 710, "name": '11-20岁'},
        {"value": 1234, "name": '21-40岁'},
        {"value": 353, "name": '40-60岁'},
        {"value": 1353, "name": '60岁以上'},
    ]

    response = HttpResponse(json.dumps(send_data), content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'       # 跨域头部
    return response
