from typing import Generic
from urllib import response
from django.shortcuts import render
from rest_framework import generics
from .models import user
from .serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.forms import model_to_dict
# Create your views here.

class UserApiList(generics.ListCreateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer

class UserApiUpdate(generics.UpdateAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer

class UserAPIDerailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = user.objects.all()
    serializer_class = UserSerializer


class UserApiView(generics.ListAPIView):  #сериалайзер
    queryset = user.objects.all()
    serializer_class = UserSerializer

# class UserApiView(APIView):
#     def get(self,request):
#         u = user.objects.all()
#         return Response({'posts':UserSerializer(u, many = True).data})

#     def post(self,request):
#         serializer = UserSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()

        # post_new = user.objects.create(
        #     title = request.data['title'],
        #     context = request.data['context'],
        #     cat_id = request.data['cat_id']
        # )
        # return Response({'post':serializer.data})

    
    def put(self,request,*args,**kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response({"error":"Method PUT is not allowed"})

        try:
            instance=user.objects.get(pk=pk)
        except:
            return Response({"error":"object does not exists"})

        serializer= UserSerializer(data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response({"post":serializer.data})




