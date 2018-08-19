from rest_framework.routers import DefaultRouter

from days.views import DayViewset

router = DefaultRouter()
router.register('', DayViewset, base_name='day')

urlpatterns = router.urls

