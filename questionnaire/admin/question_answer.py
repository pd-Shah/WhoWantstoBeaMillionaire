from django.contrib import admin

from ..models import (
    QuestionAnswer,
)

BASE = ["title", "created_at", "updated_at"]


@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_filter = [] + BASE
    list_display = [] + BASE
    readonly_fields = [
        "show_in_ui",
    ]
