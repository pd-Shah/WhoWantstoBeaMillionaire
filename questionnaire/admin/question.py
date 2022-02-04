from django.contrib import admin

from ..models import (
    Question,
)

BASE = ["title", "created_at", "updated_at", ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_filter = [] + BASE
    list_display = [] + BASE
    readonly_fields = [
        "show_in_ui",
    ]
