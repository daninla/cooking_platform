from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('add_artical/',AddPost.as_view(), name='add'),
    path('post/<int:pk>/update/',PostUpdate.as_view(), name='post_update'),
    path('post/<int:pk>/delete/',PostDelete.as_view(), name='post_delete'),
    path('category/<int:pk>/',category_list, name='category_list'),
    path("search/", SearchResalt.as_view(), name="search"),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('password/', UserChangePassword.as_view(),name='change_password'),

    path('login/',user_login, name='user_login'),
    path('logout/',user_logout, name='user_logout'),
    path('register/',register, name='register_user'),
    path('add_comment/<int:post_id>/',add_comment, name='add_comment'),
    path('profile/<int:user_id>/',profile, name='profile'),

    #API
    path('post/api/', CookingAPI.as_view(),name='cookingApi'),
    path('post/api/<int:pk>', CookingAPIDetail.as_view(),name='cookingApiDetail'),
    path('post/api/', CookingCategoryAPI.as_view(),name='cookingCategoryApi'),
    path('post/api/<int:pk>', CookingCategoryAPIDetail.as_view(),name='cookingCategoryApiDetail'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)