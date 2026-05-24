from django.db import models
from companies.models import Company


class Audit(models.Model):
	company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="audits")
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f"Audit {self.id} - {self.company.name}"

	class Meta:
		ordering = ["-date"]


class Control(models.Model):

	class ISOType(models.TextChoices):
		ISO_27001 = "ISO 27001"
		ISO_27002 = "ISO 27002"

	code = models.CharField(max_length=255, unique=True)
	title = models.CharField(max_length=255)
	description = models.TextField()
	type = models.CharField(max_length=255)
	iso_type = models.CharField(max_length=20, choices=ISOType.choices, default=ISOType.ISO_27001)

	def __str__(self):
		return self.code

	class Meta:
		ordering = ["code"]


class Answer(models.Model):
	audit = models.ForeignKey(Audit, on_delete=models.CASCADE, related_name="answers")
	control = models.ForeignKey(Control, on_delete=models.CASCADE, related_name="answers")
	status = models.CharField(max_length=255)
	work_in_progress = models.BooleanField(default=False)

	def __str__(self):
		return f"Answer - Audit {self.audit.id} - Control {self.control.code}"

	class Meta:
		unique_together = ("audit", "control")
		ordering = ["control__code"]
