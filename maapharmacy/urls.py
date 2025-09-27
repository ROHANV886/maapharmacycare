from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from myshop.views import (
    MyShopViewSet, FormViewSet, ProductViewSet,
    register_user, request_password_reset, confirm_password_reset,AddressViewSet
)
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'products', MyShopViewSet)
router.register(r'forms', FormViewSet)
router.register(r'products', ProductViewSet, basename='products')
router.register(r'addresses', AddressViewSet, basename='address')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),

    # Auth APIs
    path('api/register/', register_user, name='register'),  # signup
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # refresh token

    # Password reset APIs
    path('api/password-reset/', request_password_reset, name='password_reset'),
    path('api/password-reset-confirm/<uidb64>/<token>/', confirm_password_reset, name='password_reset_confirm'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
