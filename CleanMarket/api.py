from rest_framework import routers
from store.views import *

router = routers.DefaultRouter()

router.register('categories', CategoryView, basename='categories')
router.register('sub_categories', SubCategoryView, basename='sub_categories')
router.register('products', ProductView, basename='products')
router.register('top_products', TopProductView, basename='top_products')
router.register('about', AboutView, basename='about')
router.register('news', NewsView, basename='news')
router.register('faq', FAQView, basename='faq')
router.register('partner', PartnerView, basename='partner')
router.register('products_id', ProductsIdPost, basename='products_id')
router.register('sliders', SliderView, basename='sliders')
router.register('why_us', WhyUsView, basename='why_us')

