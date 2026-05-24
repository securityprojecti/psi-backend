from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuditViewSet, ControlViewSet, AnswerViewSet

router = DefaultRouter()
router.register(r"audits", AuditViewSet, basename="audit")
router.register(r"controls", ControlViewSet, basename="control")
router.register(r"answers", AnswerViewSet, basename="answer")

urlpatterns = [
	path("", include(router.urls)),
]
