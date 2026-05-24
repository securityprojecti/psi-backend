from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Audit, Control, Answer
from .serializers import AuditSerializer, ControlSerializer, AnswerSerializer
from .permissions import IsCompanyOwner


class AuditViewSet(viewsets.ModelViewSet):
	serializer_class = AuditSerializer
	permission_classes = [IsAuthenticated, IsCompanyOwner]
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['company', 'date']
	search_fields = ['company__name']
	ordering_fields = ['date', 'company']
	ordering = ['-date']

	def get_queryset(self):
		return Audit.objects.filter(company__user=self.request.user)


class ControlViewSet(viewsets.ModelViewSet):
	queryset = Control.objects.all()
	serializer_class = ControlSerializer
	permission_classes = [IsAuthenticated]
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['type', 'iso_type']
	search_fields = ['code', 'title', 'description']
	ordering_fields = ['code', 'type', 'iso_type']
	ordering = ['code']


class AnswerViewSet(viewsets.ModelViewSet):
	serializer_class = AnswerSerializer
	permission_classes = [IsAuthenticated, IsCompanyOwner]
	filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
	filterset_fields = ['audit', 'control', 'status', 'work_in_progress']
	search_fields = ['control__code', 'audit__company__name', 'status']
	ordering_fields = ['audit', 'control', 'status']
	ordering = ['control__code']

	def get_queryset(self):
		return Answer.objects.filter(audit__company__user=self.request.user)
