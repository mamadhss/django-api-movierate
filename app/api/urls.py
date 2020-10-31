from django.urls import path,include
from .views import MovieViewSet,RateViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movies',MovieViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('movies/<int:movie_id>/comment/',RateViewSet.as_view())

]