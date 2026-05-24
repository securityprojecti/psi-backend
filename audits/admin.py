from django.contrib import admin
from .models import Audit, Control, Answer


@admin.register(Audit)
class AuditAdmin(admin.ModelAdmin):
	list_display = ("id", "company", "date")
	list_filter = ("date", "company")
	search_fields = ("company__name",)
	readonly_fields = ("date",)


@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
	list_display = ("id", "code", "type")
	list_filter = ("type",)
	search_fields = ("code", "description")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
	list_display = ("id", "audit", "control", "status", "work_in_progress")
	list_filter = ("status", "work_in_progress", "audit")
	search_fields = ("control__code", "audit__company__name")
	readonly_fields = ("audit", "control")
