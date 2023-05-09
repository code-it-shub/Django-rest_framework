from django.shortcuts import render
from rest_framework.views import APIView
from .models import shop_items,serializedItems
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from rest_framework import mixins , generics


# Create your views here.
#  CREATING API USING GENERICS

class itemShow(generics.ListCreateAPIView):
    queryset = shop_items.objects.all()
    serializer_class = serializedItems

class itemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = shop_items.objects.all()
    serializer_class = serializedItems

'''
# USING MIXINS CLASS 

class itemShow(mixins.ListModelMixin ,mixins.CreateModelMixin, generics.GenericAPIView):
    queryset= shop_items.objects.all()
    serializer_class = serializedItems

    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class itemDetail(generics.GenericAPIView , mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset= shop_items.objects.all()
    serializer_class = serializedItems
    def get(self, request, pk):
        return self.retrieve(request,pk)
    def put(self,request , pk):
        return self.update(request,pk)
    def delete(self,request, pk):
        return self.destroy(request,pk)
'''

'''
## Creating class based view here

class itemShow(APIView):
    def get(self, request):
        item = shop_items.objects.all()
        serialized = serializedItems(item, many=True)
        return Response(serialized.data)
    def post(self, request):
        serialized = serializedItems(data=request.data)
        if serialized.is_valid():
            serialized.save()
            return Response(serialized.data)
        else:
            return Response(serialized.errors)
        
class itemDetail(APIView):
    def item_get(self,pk ):
        try:
            return shop_items.objects.get(pk=pk)
        except shop_items.DoesNotExist:
            raise Http404
    def get(self ,request, pk):
        item = self.item_get(pk)
        serializer = serializedItems(item)
        return Response(serializer.data)
    def put(self ,request , pk):
        item = self.item_get(pk)
        serializer = serializedItems(item , data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    def delete(self,request, pk):
        item= self.item_get(pk)
        item.delete()
        return Response(status.HTTP_200_OK)
'''
        





