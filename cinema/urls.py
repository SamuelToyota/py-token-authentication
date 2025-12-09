from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterAPIView, LoginAPIView, UserMeAPIView, OrderViewSet

router = DefaultRouter()
router.register("orders", OrderViewSet)

urlpatterns = [
    path("user/register/", RegisterAPIView.as_view()),
    path("user/login/", LoginAPIView.as_view()),
    path("user/me/", UserMeAPIView.as_view()),
    path("", include(router.urls)),
]
