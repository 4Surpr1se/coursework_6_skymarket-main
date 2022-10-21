import djoser
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from djoser import urls
from djoser.urls import jwt
from djoser.views import UserViewSet
from rest_framework.routers import SimpleRouter
from drf_spectacular.views import SpectacularSwaggerView, SpectacularAPIView

from ads.urls import ad_urlpatterns

users_router = SimpleRouter()

# обратите внимание, что здесь в роуте мы регистрируем ViewSet,
# который импортирован из приложения Djoser
users_router.register("api/users", UserViewSet, basename="users")

# TODO здесь необходимо подклюючит нужные нам urls к проекту


urlpatterns = [
    path("api/admin/", admin.site.urls),
    path("api/redoc-tasks/", include("redoc.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/',
         SpectacularSwaggerView.as_view(url_name='schema'),
         name='swagger-ui'),
    path("", include(users_router.urls)),
    path('auth/', include(jwt)),
]
urlpatterns += ad_urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
