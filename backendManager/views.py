#-*-coding:utf-8-*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist

import json
import requests
import time
import hashlib
import base64
import os
from urllib import urlencode

# Create your views here.
@csrf_exempt
def getSpecies(request):
    # print(request.body)
    recv_data = json.loads(request.body.decode('utf-8'))
    dateRange = recv_data['dateRange']
    # print(dateRange)
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

def writeFile(file, content):
    with open(file, 'wb') as f:
        f.write(content)
    f.close()

@csrf_exempt
def getAudio(request):
    print(request.body)
    # recv_data = json.loads(request.body.decode('utf-8'))
    # text = recv_data['text']
    send_data = {}

    URL = "http://api.xfyun.cn/v1/service/v1/tts"
    AUE = "raw"
    APPID = "5bfd079b"
    API_KEY = "c978a5902ca5d233edbe4e721c71a842"

    curTime = str(int(time.time()))
    #ttp=ssml
    param = "{\"aue\":\""+AUE+"\",\"auf\":\"audio/L16;rate=16000\",\"voice_name\":\"xiaoyan\",\"engine_type\":\"intp65\"}"
    print("param:{}".format(param))
    paramBase64 = str(base64.b64encode(param.encode('utf-8')))
    print("x_param:{}".format(paramBase64))
    
    m2 = hashlib.md5()
    m2.update((API_KEY + curTime + paramBase64).encode('utf-8'))
    
    checkSum = m2.hexdigest()
    print('checkSum:{}'.format(checkSum))
    
    header ={
            'X-CurTime':curTime,
            'X-Param':paramBase64,
            'X-Appid':APPID,
            'X-CheckSum':checkSum,
            'X-Real-Ip':'127.0.0.1',
            'Content-Type':'application/x-www-form-urlencoded; charset=utf-8',
    }
    print(header)
    
    # with open("E:/museumServer/123.txt", 'r') as f:
    #     text = f.read()

    print(os.path.abspath(".."))
    with open("123.txt", "r") as f:
        text = f.read()

    print({"text": unicode(text, "gb2312")})
    r = requests.post(URL,headers=header,data={"text": unicode(text, "gb2312").encode('utf-8')})
    contentType = r.headers['Content-Type']
    if contentType == "audio/mpeg":
        sid = r.headers['sid']
        send_data['audio'] = base64.b64encode(r.content)
        # if AUE == "raw":
        #     writeFile(sid+".wav", r.content)
        # else :
        #     writeFile("xiaoyan"+".mp3", r.content)
        print ("success, sid = " + sid)
    else :
        send_data['result'] = "failed"
        print (r.text)
    # print(r.content)
    

    response = HttpResponse(json.dumps(send_data), content_type="application/json")
    response['Access-Control-Allow-Origin'] = '*'       # 跨域头部
    return response
