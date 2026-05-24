from rest_framework import viewsets
from .models import Audit, Control, Answer
from .serializers import AuditSerializer, ControlSerializer, AnswerSerializer


class AuditViewSet(viewsets.ModelViewSet):
	queryset = Audit.objects.all()
	serializer_class = AuditSerializer


class ControlViewSet(viewsets.ModelViewSet):
	queryset = Control.objects.all()
	serializer_class = ControlSerializer


class AnswerViewSet(viewsets.ModelViewSet):
	queryset = Answer.objects.all()
	serializer_class = AnswerSerializer
