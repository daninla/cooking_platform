from .models import Post,Category
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('title','content','created_at','category','author')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title','id')