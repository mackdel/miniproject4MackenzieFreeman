from django.contrib import admin
from .models import PolicySection, Policy, Definition, PolicyRequest, ProcedureStep

# Inline configuration for Procedure Steps in Policies
class ProcedureStepInline(admin.TabularInline):
    model = ProcedureStep
    extra = 1  # Start with one empty row for adding steps
    ordering = ['step_number']  # Order steps by their number


# Inline configuration for Definitions in Policies
class DefinitionInline(admin.StackedInline):
    model = Definition.policies.through  # Many-to-Many relationship with Policies
    extra = 1


# Admin configuration for Policy model
class PolicyAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Policy Information", {
            "fields": ["section", "title", "number", "version", "policy_owner", "pub_date", "review_period"]
        }),
        ("Policy Details", {
            "fields": [
                "purpose",
                "scope",
                "policy_statements",
                "responsibilities"
            ],
        }),
        ("Relationships", {
            "fields": ["related_policies"]
        }),
    ]
    readonly_fields = ["number", "pub_date"]  # Fields that should not be editable
    list_display = ["number", "title", "section", "policy_owner", "pub_date", "version"]
    list_filter = ["section", "policy_owner", "pub_date"]
    search_fields = ["title", "policy_statements", "section__title"]
    ordering = ["section", "number"]
    filter_horizontal = ["related_policies"]  # Horizontal widget for managing related policies
    inlines = [ProcedureStepInline, DefinitionInline]

# Admin configuration for Policy Request model
class PolicyRequestAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Request Information", {
            "fields": ('policy', 'name', 'email', 'question', 'submitted_at')
        }),
        ("Resolution", {
            "fields": ('is_resolved', 'admin_notes')
        }),
    ]
    readonly_fields = ('policy', 'name', 'email', 'question', 'submitted_at')  # Non-editable fields
    list_display = ('policy', 'name_or_anonymous', 'email', 'submitted_at', 'is_resolved')
    list_filter = ('is_resolved', 'submitted_at', 'policy__section')
    search_fields = ('name', 'email', 'question', 'policy__title', 'policy__section__title')
    ordering = ('-submitted_at',)  # Order by the most recent submissions
    actions = ['mark_requests_resolved']

    # Show 'Anonymous' if name is blank.
    def name_or_anonymous(self, obj):
        return obj.name or "Anonymous"
    name_or_anonymous.short_description = "Name"

    # Mark selected requests as resolved.
    def mark_requests_resolved(self, request, queryset):
        count = queryset.update(is_resolved=True)
        self.message_user(request, f"{count} request(s) marked as resolved.")

    mark_requests_resolved.short_description = "Mark selected requests as resolved"

    # Prevent adding new Policy Requests manually
    def has_add_permission(self, request):
        return False


# Register models with admin site
admin.site.register(PolicySection)
admin.site.register(Policy, PolicyAdmin)
admin.site.register(Definition)
admin.site.register(PolicyRequest, PolicyRequestAdmin)

