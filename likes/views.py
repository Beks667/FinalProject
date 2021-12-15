from .models import PostLikes
from .serializers import PostLikesSerializer
from serials.models import Product
from accounts.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404 
from django.db.models import Q
class LikeListCreate(APIView):
    def get(self,request,format = None):
        snippets = PostLikes.objects.all()
        serializer =PostLikesSerializer(snippets ,many = True)
        return Response(serializer.data)


    def post(self,request,pk):
        like_users=request.user
        like_posts=get_object_or_404(Product, id=pk)
        check=PostLikes.objects.filter(Q(like_users=like_users) & Q(like_posts=like_posts))
        if (check.exists()):
            return Response({
                "status": status.HTTP_400_BAD_REQUEST,
            "message":"Already Liked"
            })
        new_like=PostLikes.objects.create(like_users=like_users,like_posts=like_posts.last())
        new_like.save()
        serializer=PostLikesSerializer(new_like)
        return Response(serializer.data,status=status.HTTP_201_CREATED)


