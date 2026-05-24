from django.db import models
from django.contrib.auth.models import User


class Company(models.Model):
	name = models.CharField(max_length=255)
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="companies")
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.name
