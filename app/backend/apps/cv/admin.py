from django.contrib import admin

from apps.cv.models import (
    CV,
    Header,
    BodySection
)


@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ("filename", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "created_at")
    search_fields = ("filename", "user__username")

@admin.register(Header)
class HeaderAdmin(admin.ModelAdmin):
    list_display = ("full_name", "position", "linkedin_url", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "created_at")

@admin.register(BodySection)
class BodySectionAdmin(admin.ModelAdmin):
    list_display = ("name", "cv", "is_active", "created_at", "updated_at")
    list_filter = ("is_active", "created_at")
