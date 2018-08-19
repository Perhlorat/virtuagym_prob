from rest_framework.routers import DefaultRouter

from plans.views import PlanViewset

router = DefaultRouter()
router.register('', PlanViewset, base_name='plan')

urlpatterns = router.urls

