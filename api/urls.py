from rest_framework import routers
from .api import chambeadorViewSet

router = routers.DefaultRouter()

router.register('api/chambeador', chambeadorViewSet, 'chambeador')


urlpatterns = router.urls