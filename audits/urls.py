from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuditViewSet, ControlViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r"audits", AuditViewSet)
router.register(r"controls", ControlViewSet)
router.register(r"answers", AnswerViewSet)

urlpatterns = [
	path("", include(router.urls)),
]
