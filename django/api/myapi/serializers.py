from rest_framework import serializers

from .models import Youtube


class YoutubeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Youtube
        fields = "__all__"
