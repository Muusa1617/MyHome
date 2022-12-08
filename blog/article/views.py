
from article.models import Article
from article.serializers import ArticleListSerializer,ArticleDetailSerializer
from rest_framework import generics
from article.permissions import IsAdminUserOrReadOnly

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.uesr)
    permission_classes = [IsAdminUserOrReadOnly]


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    permission_classes = [IsAdminUserOrReadOnly]