from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:pk>/',category_list, name='category_list'),
    path('post/<int:pk>/',post_detail, name='post_detail'),
    path('add_artical/',add_post, name='add')
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)