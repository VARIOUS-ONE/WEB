from itertools import product
from multiprocessing.connection import wait
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from os import remove
from django.db import models
# from django.db.models import Products
from base.models import Product

from time import sleep

def make_wordcloud(text):
    font_path = "./base/views/NanumGothic.ttf" # 경로 맞추기 (일단 바탕화면에 다운 받아 놓음 )
    wordcloud = WordCloud(font_path=font_path, background_color="white", width=400, height=400) # width, height 웹에 맞추기 
    wordcloud = wordcloud.generate(text) # 받아온 text
    wordcloud.to_file("result.png")
    
@api_view(['POST', 'GET'])
def visualization_wordcloud(request):
    #print("캬캬캬캬캬캬캬캬캬캬캬캬!!")
    text = ""
    if request.method == 'POST':
        font_path = "./base/views/NanumGothic.ttf" # 경로 맞추기 (일단 바탕화면에 다운 받아 놓음 )
        product_name = request.data['product_name']
        text = request.data['total_review']
        wordcloud = WordCloud(font_path=font_path, background_color="white", width=400, height=400)
        wordcloud = wordcloud.generate(text) # 받아온 text
        #print(update_product) product 이름이 나옴. 

        #wordcloud.to_file("./base/views/wordcloudresult/"+product_name+".png")
        update_product = Product.objects.get(name = product_name)
        # print(update_product)
        # print(update_product.brand)
        #wordcloud.to_file("./wordcloudresult/"+product_name+".png")

        update_product.wordcloud = "./"+product_name+".png"
        #backend/base/views/wordcloudresult/slah
        #images/wordcloud
        # update_product.description = "수정합니다"
        # print(update_product.description)
        sleep(1)
        update_product.save(update_fields=['wordcloud'])
    return Response('끝까지 완주하였습니다')