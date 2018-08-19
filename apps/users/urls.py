from rest_framework.routers import DefaultRouter

from users.views import UserViewset

router = DefaultRouter()
router.register('', UserViewset, base_name='user')

urlpatterns = router.urls

