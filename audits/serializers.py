from rest_framework import serializers
from .models import Audit, Control, Answer


class ControlSerializer(serializers.ModelSerializer):
	class Meta:
		model = Control
		fields = ["id", "code", "description", "type", "iso_type"]


class AnswerSerializer(serializers.ModelSerializer):
	control_info = ControlSerializer(source="control", read_only=True)

	class Meta:
		model = Answer
		fields = ["id", "audit", "control", "control_info", "status", "work_in_progress"]


class AuditSerializer(serializers.ModelSerializer):
	answers = AnswerSerializer(many=True, read_only=True)

	class Meta:
		model = Audit
		fields = ["id", "company", "date", "answers"]
		read_only_fields = ["date"]
