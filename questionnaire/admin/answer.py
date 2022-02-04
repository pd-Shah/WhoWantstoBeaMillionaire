from django.contrib import admin

from ..models import (
    Answer,
)

BASE = ["title", "created_at", "updated_at",]


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_filter = [] + BASE
    list_display = [] + BASE
    readonly_fields = [
        "show_in_ui",
    ]
