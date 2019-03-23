from rest_framework import routers
from .views import ImageUploadViewSet
from django.conf.urls import url

router = routers.SimpleRouter()
router.register(r'', ImageUploadViewSet)

urlpatterns = router.urls