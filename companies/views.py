from companies.models import Company
from companies.serializers import CompanySerializer, CompanyListSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class CompanyViewSet(viewsets.ModelViewSet):
	queryset = Company.objects.all()
	serializer_class = CompanySerializer
	permission_classes = [IsAuthenticated]

	def get_serializer_class(self):
		if self.action == 'list':
			return CompanyListSerializer
		return CompanySerializer
	
	def get_queryset(self):
		return Company.objects.filter(user=self.request.user)
	
	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
