from companies.models import Company
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ["id", "name", "created_at"]


class CompanyListSerializer(serializers.ModelSerializer):
	class Meta:
		model = Company
		fields = ["id", "name", "user"]
