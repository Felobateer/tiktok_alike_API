from .models import Video
from rest_framework import serializers

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['id', 'title', 'description', 'thumb_nail', 'description', 'content', 
                  'views', 'likes', 'comments', 'tags', 'posted_at']
        extra_kwargs = {
            "posted_at": {"read_only": True},
            "views": {"read_only": True},
            "likes": {"read_only": True},
            "comments": {"read_only": True},
            "tags": {"read_only": True},
        }
    
    def create(self, validated_data):
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    
