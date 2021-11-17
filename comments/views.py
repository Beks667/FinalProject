from django.shortcuts import render
from django.urls.conf import include

from .models import Comment
from .serializers import CommentSeralizer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class CommentListView(APIView):
    def get(self,request,format = None):
        snippets = Comment.objects.all()
        serializer =CommentSeralizer(snippets ,many = True)
        return Response(serializer.data)

    def post(self,request,format= None):
        serializer = CommentSeralizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class CommentDetailView(APIView):
    def get_object(self,pk):
        try:
            return Comment.objects.get(pk=pk)
        except Comment.DoesNotExist:
            raise Http404

    def get(self,request,pk,format = None):
        snippet = self.get_object(pk)
        serializer = CommentSeralizer(snippet)
        return Response (serializer.data)

    def put(self,request,pk,format=None):
        snippet=self.get_object(pk)
        serializer = CommentSeralizer(snippet,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format= None):
        snippet=self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)