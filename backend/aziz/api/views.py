import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

@api_view(['GET','POST'])
def api_home(request):
    # body=request.body #JSON data
    # data={}
    # print(request.GET) #url query params
    # try:
    #     data=json.loads(body) #json data transfer into python dictionary  

    # except:
    #     pass
    # print(data)    
    # data['headers']=dict(request.headers)
    # data['content_type']=request.content_type
    # data['params']=dict(request.GET)
    # print(body)

    instance=Product.objects.get(id=1)
    # print(instance)
    # return Response({'message':'Hello World'})
    # data={}
    # this one of way to queryset dat transfer into json data

    # if(model_data):
    #     data={
    #         'title' :model_data.title,
    #         'description':model_data.description,
    #         'isOk':model_data.is_ok,
    #     }

    # this is another way model to dictionary
    if request.method=='GET':
        if(instance):
            # data=model_to_dict(instance,fields=['id','title','description'])
            serializer= ProductSerializer(instance)
            return Response(serializer.data)
        
    elif request.method=='POST':
        serializer=ProductSerializer(data=request.data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

# Retrieves and renders detailed information about a specific product.
#Inherits from generics.RetrieveAPIView, a Django REST Framework generic
# view for handling GET requests to retrieve a single model instance.
class ProductDetailsView(generics.RetrieveAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


Product_Detail_View=ProductDetailsView.as_view()

class ProductCreateApiView(generics.CreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title=serializer.validated_data.get('title')
        content=serializer.validated_data.get('description') or None
        # print(content+'Hello')
        if content is None:
            content=title
        serializer.save(description=content) #product.description=content
         
Product_Create_View=ProductCreateApiView.as_view()


# class ProductListsView(generics.ListAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer


# Product_List_View=ProductListsView.as_view()

class ProductCreateListsView(generics.ListCreateAPIView):
    #ListCreateAPIView dont means create a list because in serializer have one models
    queryset=Product.objects.all()
    serializer_class=ProductSerializer


Product_Create_List_View=ProductCreateListsView.as_view()


class ProductUpdatesView(generics.UpdateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

    def perform_update(self, serializer):
        instance=serializer.save()
        print(serializer.data)
        if not instance.description:
            instance.description=instance.title
            
Product_Update_View=ProductUpdatesView.as_view()

class ProductDestroyView(generics.DestroyAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'
    def perform_destroy(self, instance):
        return super().perform_destroy(instance)


Product_Destroy_View=ProductDestroyView.as_view()