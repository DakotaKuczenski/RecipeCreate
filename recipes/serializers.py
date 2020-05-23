from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name="recipes:user-detail") # trying to fix.
    class Meta:
        model = Post
        fields = ('author', 'title', 'description')
