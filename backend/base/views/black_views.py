from django.shortcuts import render
from base.models import Blacklist
from django.core import serializers
from django.http import HttpResponse
from django.http import JsonResponse
def getBlackUsers(request):
    queryset = Blacklist.objects.all()
    #print(queryset)
    query_list = serializers.serialize('json', queryset)
    print(query_list)#너가 원하는 
    #return query_list
    return HttpResponse(query_list, content_type="text/json-comment-filtered")

    #return HttpResponse(query_list, content_type="text/json-comment-filtered")
    #return HttpResponse(query_list, content_type="text")
    #return query_list
    #return JsonResponse(queryset)

