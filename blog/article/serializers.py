from rest_framework import serializers
from article.models import Article
from user_info.serializers import UserDescSerializer


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserDescSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'

# class ArticleListSerializer(serializers.ModelSerializer):
#     url = serializers.HyperlinkedIdentityField(view_name="article:detail")
#     # read_only 参数设置为只读
#     author = UserDescSerializer(read_only=True)

#     class Meta:
#         model = Article
#         fields = [
#             'id',
#             'title',
#             'url',
#             'created',
#             'author',
#         ]

# class ArticleDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
