from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection


def index(request):
    strict_redis = get_redis_connection()

    # 通过StrictRedis对象操作Redis
    # 增
    strict_redis.set('aa', '111')
    strict_redis.set('bb', '222')

    # 查
    aa = strict_redis.get('aa')
    bb = strict_redis.get('bb')
    text = 'aa=%s, bb=%s' % (aa.decode(), bb.decode())
    return HttpResponse(text)

