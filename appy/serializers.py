from rest_framework import serializers
from .models import Post, Calc

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CalcSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calc
        fields = '__all__'
