#-*-coding:utf-8-*-

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

import json
 
def hello(request):
    return HttpResponse("Hello world ! ")

@csrf_exempt
def manage(request):
    send_data = {}

    send_data['userNum'] = 1000
    send_data['mostVisited'] = "大灵猫"
    send_data['visitedNum'] = [
        {"value": 235, "name": '动物'},
        {"value": 710, "name": '植物'},
        {"value": 534, "name": '昆虫'},
        {"value": 153, "name": '化石'}
    ]

    response = HttpResponse(json.dumps(send_data), content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'       # 跨域头部
    return response