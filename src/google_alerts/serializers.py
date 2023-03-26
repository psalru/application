from rest_framework import serializers

from .models import NewsFeed


class NewsFeedSerializer(serializers.ModelSerializer):
    s3 = serializers.SerializerMethodField('get_s3')

    class Meta:
        model = NewsFeed
        exclude = ['s3_bucket', 's3_key']

    def get_s3(self, obj):
        return f"https://storage.yandexcloud.net/{obj.s3_bucket}/{obj.s3_key}" if obj.s3_key else None
