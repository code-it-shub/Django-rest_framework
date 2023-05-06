from django.shortcuts import render
from rest_framework.views import APIView
from .models import shop_items,serializedItems
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

# Create your views here.

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

        





