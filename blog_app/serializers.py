from rest_framework import serializers

from .models import Article


class ArticleSerializers(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = (
            "id",
            "title",
            "author",
            "content",
            "published_date",
            "tag",
        )
