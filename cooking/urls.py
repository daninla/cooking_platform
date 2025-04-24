from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('', index, name='index'),
    path('', Index.as_view(), name='index'),
    path('add_artical/',AddPost.as_view(), name='add'),
    path('post/<int:pk>/update/',PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/',PostDelete.as_view(), name='post_delete'),
    path('category/<int:pk>/',category_list, name='category_list'),
    path('post/<int:pk>/', post_detail, name='post_detail'),
    path('login/',user_login, name='user_login'),
    path('logout/',user_logout, name='user_logout'),
    path('register/',register, name='register_user'),
]
 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)