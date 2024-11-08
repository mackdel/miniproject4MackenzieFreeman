from django.contrib import admin
from .models import PolicySection, Policy, Definition, PolicyRequest

admin.site.register(Policy)
admin.site.register(PolicySection)
admin.site.register(Definition)

@admin.register(PolicyRequest)
class PolicyRequestAdmin(admin.ModelAdmin):
    list_display = ('policy', 'name', 'email', 'submitted_at', 'is_resolved')
    list_filter = ('is_resolved', 'submitted_at')
    search_fields = ('name', 'email', 'question', 'policy__title')
    readonly_fields = ('policy', 'name', 'email', 'question', 'submitted_at')  # Fields that cannot be edited
    actions = None  # Removes the ability to perform actions like bulk delete

    def has_add_permission(self, request):
        # Disable the ability to add new requests
        return False

