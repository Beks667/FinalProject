from django.shortcuts import render
from django.urls.conf import include
from django.shortcuts import get_object_or_404
from django.db.models import Q

 
from .models import Category,Product
from likes.models import PostLikes
from likes.serializers import PostLikesSerializer
from .serializer import ProductSerializer,CategorySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404

class ProductListView(APIView):
    def get(self, request):
        snippets = Product.objects.all()
        serializer = ProductSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductDetailView(APIView):
    def get_object(self, pk):
        try:
            return Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = ProductSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def post(self, request, pk):
        post_to_be_liked = self.get_object(pk)
        user = request.user
        if not user.is_authenticated:
            return Response({'message': 'Authirzation required'}, status=status.HTTP_401_UNAUTHORIZED)
        elif user.is_authenticated:
            like_users=request.user
            like_posts=post_to_be_liked
            check=PostLikes.objects.filter(Q(users_like_id=like_users.id) & Q(posts_like_id=pk))
            if (check.exists()):
                return Response({
                    "status": status.HTTP_400_BAD_REQUEST,
                "message":"Already Liked"
                })
            new_like=PostLikes.objects.create(users_like=like_users,posts_like=like_posts)
            new_like.save()
            serializer=PostLikesSerializer(new_like)
            return Response(serializer.data,status=status.HTTP_201_CREATED)


# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class CategoryListView(APIView):
    def get(self, request):
        snippets = Category.objects.all()
        serializer = CategorySerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CategoryDetailView(APIView):
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet)
        return Response(serializer.data)

    def put(self, request, pk):
        snippet = self.get_object(pk)
        serializer = CategorySerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)