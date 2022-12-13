from rest_framework import serializers
from article.models import Article
from user_info.serializers import UserDescSerializer
from article.models import Category
from article.models import Tag

# 新增的序列化器


class TagSerializer(serializers.HyperlinkedModelSerializer):
    """标签序列化器"""

    def check_tag_obj_exists(self, validated_data):
        text = validated_data.get('text')
        if Tag.objects.filter(text=text).exists():
            raise serializers.ValidationError(
                'Tag with text {} exists.'.format(text))

    def create(self, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        self.check_tag_obj_exists(validated_data)
        return super().update(instance, validated_data)

    class Meta:
        model = Tag
        fields = '__all__'


class ArticleCategoryDetailSerializer(serializers.ModelSerializer):
    """给分类详情的嵌套序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')

    class Meta:
        model = Article
        fields = [
            'url',
            'title',
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    """分类详情"""
    articles = ArticleCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'created',
            'articles',
        ]


class CategorySerializer(serializers.ModelSerializer):
    """分类的序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['created']


class ArticleBaseSerializer(serializers.HyperlinkedModelSerializer):
    """博文序列化器基类"""
    id = serializers.IntegerField(read_only=True)
    author = UserDescSerializer(read_only=True)
    # category 的嵌套序列化字段
    category = CategorySerializer(read_only=True)
    # category 的 id 字段，用于创建/更新 category 外键
    category_id = serializers.IntegerField(
        write_only=True, allow_null=True, required=False)
    # tag 字段
    tags = serializers.SlugRelatedField(
        queryset=Tag.objects.all(),
        many=True,
        required=False,
        slug_field='text'
    )

    # category_id 字段的验证器
    def validate_category_id(self, value):
        if not Category.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError(
                "Category with id {} not exists.".format(value))
        return value

    # 覆写方法，如果输入的标签不存在则创建它
    def to_internal_value(self, data):
        tags_data = data.get('tags')

        if isinstance(tags_data, list):
            for text in tags_data:
                if not Tag.objects.filter(text=text).exists():
                    Tag.objects.create(text=text)

        return super().to_internal_value(data)

# 保留 Meta 类
# 将父类改为 ArticleBaseSerializer


class ArticleSerializer(ArticleBaseSerializer):
    class Meta:
        model = Article
        fields = '__all__'
        extra_kwargs = {'body': {'write_only': True}}

# 注意继承的父类是 ArticleBaseSerializer


class ArticleDetailSerializer(ArticleBaseSerializer):
    # 渲染后的正文
    body_html = serializers.SerializerMethodField()
    # 渲染后的目录
    toc_html = serializers.SerializerMethodField()

    def get_body_html(self, obj):
        return obj.get_md()[0]

    def get_toc_html(self, obj):
        return obj.get_md()[1]

    class Meta:
        model = Article
        fields = '__all__'
# from rest_framework import serializers
# from article.models import Article
# from user_info.serializers import UserDescSerializer

# class CategorySerializer(serializers.HyperlinkedModelSerializer):

#     class Meta:
#         model = Article
#         fields = '__all__'


# class ArticleSerializer(serializers.HyperlinkedModelSerializer):
#     author = UserDescSerializer(read_only=True)

#     class Meta:
#         model = Article
#         fields = '__all__'

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
