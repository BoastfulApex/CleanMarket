from rest_framework import viewsets
from .serializers import *
from rest_framework import filters, status
from rest_framework.response import Response
from django.core.paginator import Paginator
from django.urls import reverse
from django.shortcuts import get_object_or_404


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryView(viewsets.ModelViewSet):
    serializer_class = SubCategorySerializer

    def get_queryset(self):
        queryset = SubCategory.objects.all().order_by('id')

        category_id = self.request.GET.get('category_id')

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset


class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name_uz', 'name_ru', 'name_en']

    def get_queryset(self):
        queryset = Product.objects.all().order_by('id')

        category_id = self.request.GET.get('category_id')
        subcategory_id = self.request.GET.get('subcategory_id')

        if category_id:
            queryset = queryset.filter(category_id=category_id)

        if subcategory_id:
            queryset = queryset.filter(sub_category_id=subcategory_id)

        return queryset

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        slug = self.kwargs.get('pk')
        obj = get_object_or_404(queryset, slug=slug)
        return obj

    def list(self, request, *args, **kwargs):
        try:
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 10))
            page_size = max(1, min(page_size, 100))  # Ensure page_size is between 1 and 100

            queryset = self.get_queryset()
            total_items = queryset.count()
            max_page = (total_items + page_size - 1) // page_size

            if page > max_page:
                page = max_page

            paginator = Paginator(queryset, page_size)
            paginated_queryset = paginator.get_page(page)

            serializer = ProductSerializer(paginated_queryset, many=True)

            data = {
                'page': page,
                'max_page': max_page,
                'previous_page': self.get_page_url(page - 1) if page > 1 else None,
                'next_page': self.get_page_url(page + 1) if page < max_page else None,
                'results': serializer.data
            }

            return Response(data)

        except Exception as exx:
            return Response({
                "status": True,
                "code": 500,
                "data": [],
                "message": [str(exx)]
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def get_page_url(self, page_number):
        if page_number < 1:
            return None
        return reverse('product-list') + f'?page={page_number}'


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

    def get_object(self):
        queryset = self.filter_queryset(self.get_queryset())
        slug = self.kwargs.get('slug')  # Retrieve the slug from the URL
        return get_object_or_404(queryset, slug=slug)


class PartnerView(viewsets.ModelViewSet):
    queryset = Partner.objects.all()
    serializer_class = PartnerSerializer
