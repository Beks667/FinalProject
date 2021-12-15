from rest_framework import serializers
from .models import Comment

class CommentSeralizer(serializers.ModelSerializer):
    class Meta:
        model =Comment
        fields = ['films','author','like','content','created_at','parent','is_active',]