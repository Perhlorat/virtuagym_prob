from rest_framework.routers import DefaultRouter

from exercises.views import ExerciseViewset

router = DefaultRouter()
router.register('', ExerciseViewset, base_name='exercise')

urlpatterns = router.urls

