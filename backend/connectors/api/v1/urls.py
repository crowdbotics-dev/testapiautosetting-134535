from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Testconnectors134535ViewSet

router = DefaultRouter()
router.register(
    "testconnectors134535", Testconnectors134535ViewSet, basename="testconnectors134535"
)

urlpatterns = [
    path("connectors/", include(router.urls)),
]
