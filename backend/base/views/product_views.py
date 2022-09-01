from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from base.models import Product, Review
from base.serializers import ProductSerializer

from .sentimentAnalysis.review_SA import review_SA
from .sangwon.fake_review_detection import fake_review
from .sangwon.kobart_summary import kobart
#print(fake_review_detection.predict("1", "안녕하세요")) # temp1 가짜판별 ()
#print(fake_review_detection.predict("2","슬!롯!머!신 욕심 안내면  돈 벌어갈 수 있음 꼭 돈 잃는애들보면 욕심 많아가지고 잃는거임홀?홀?덤?덤?c?o?m?"))
#kobart.kobart_summary(text)
#from .sangwon.kobart_summary import kobart_summary
from rest_framework import status
import sqlite3

from base.models import Blacklist

@api_view(['GET'])
def getProducts(request):
    query = request.query_params.get('keyword')
    if query == None:
        query = ''

    products = Product.objects.filter(
        name__icontains=query).order_by('-createdAt')

    page = request.query_params.get('page')
    paginator = Paginator(products, 5)

    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)

    if page == None:
        page = 1

    page = int(page)
    print('Page:', page)
    serializer = ProductSerializer(products, many=True)
    return Response({'products': serializer.data, 'page': page, 'pages': paginator.num_pages})


@api_view(['GET'])
def getTopProducts(request):
    products = Product.objects.filter(rating__gte=4).order_by('-rating')[0:5]
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def createProduct(request):
    user = request.user

    product = Product.objects.create(
        user=user,
        name='Sample Name',
        price=0,
        brand='Sample Brand',
        countInStock=0,
        category='Sample Category',
        description=''
    )

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAdminUser])
def updateProduct(request, pk):
    data = request.data
    product = Product.objects.get(_id=pk)

    product.name = data['name']
    product.price = data['price']
    product.brand = data['brand']
    product.countInStock = data['countInStock']
    product.category = data['category']
    product.description = data['description']

    product.save()

    serializer = ProductSerializer(product, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteProduct(request, pk):
    product = Product.objects.get(_id=pk)
    product.delete()
    return Response('Producted Deleted')


@api_view(['POST'])
def uploadImage(request):
    data = request.data

    product_id = data['product_id']
    product = Product.objects.get(_id=product_id)

    product.image = request.FILES.get('image')
    product.save()

    return Response('Image was uploaded')


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def createProductReview(request, pk):
    user = request.user
    product = Product.objects.get(_id=pk)
    data = request.data

    # 1 - Review already exists
    alreadyExists = product.review_set.filter(user=user).exists()
    if alreadyExists:
        content = {'detail': 'Product already reviewed'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)

    # 2 - No Rating or 0
    elif data['rating'] == 0:
        content = {'detail': 'Please select a rating'}
        return Response(content, status=status.HTTP_400_BAD_REQUEST)
    else:
        summary = ""
        if(len(data['comment']) >= 150):
            summary = kobart.kokobart_summary(data['comment']) # temp1  요약문장(str)
        else:
            summary = data['comment']
        #print(data) rating , comment . 

        fake_review.predict(data['rating'], data['comment']) # temp2 가짜판별 ()

        temp = review_SA.predict(data['comment'])

        print(data)
        review = Review.objects.create(
            user=user,
            product=product,
            name=user.first_name,
            rating=data['rating'],
            comment=data['comment'],
            summary=summary,
            is_positive = temp
        )

        reviews = product.review_set.all()
        product.numReviews = len(reviews)

        total = 0
        for i in reviews:
            total += i.rating

        product.rating = total / len(reviews)
        product.save()

    return Response('Review Added')


    """
    # 3 - wrong review
    ml_result = review_SA.predict(data['comment'])

    #부정  & 레이팅 4 이상
    if ml_result == 0 and data['rating'] >=4:
        return Response("1")
    
    #긍정 & 레이팅 2 이하
    if ml_result == 1 and data['rating'] <=2:
        return Response("1")
    """
    # elif data['rating']=='1' or data['rating']=='2':
    #     if temp==1:
    #         print("리뷰를 다시 한번 확인해주세요")
    
    # elif data['rating']=='4' or data['rating']=='5':
    #     if temp==0:
    #         print("리뷰를 다시 한번 확인해주세요")

    # 4 - Create review