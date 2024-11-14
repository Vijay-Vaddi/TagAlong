from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from users import urls

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/users/',include('users.urls')),
    path('admin/', admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(),name="api-schema"),
    path("api/docs/",
         SpectacularSwaggerView.as_view(url_name='api-schema'),
         name="api-docs"),
]
