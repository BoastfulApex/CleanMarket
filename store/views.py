from rest_framework import viewsets
from .serializers import *
from rest_framework import filters


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryView(viewsets.ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubCategorySerializer


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_uz', 'name_ru', 'name_en']


class TopProductView(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_uz', 'name_ru', 'name_en']

    def get_queryset(self):
        queryset = Product.objects.filter(top=True).all()
        return queryset



class AboutView(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


class FAQView(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class NewsView(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

