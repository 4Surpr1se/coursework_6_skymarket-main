from django.urls import include, path

# TODO настройка роутов для модели
from rest_framework import routers

from ads.views import AdViewSet, AdMeAPIView, CommentViewSet

router = routers.SimpleRouter()
router.register('api/ads', AdViewSet)
router.register('api/comment', CommentViewSet)


ad_urlpatterns = router.urls
ad_urlpatterns.append(path('api/ads/me/', AdMeAPIView.as_view()))
