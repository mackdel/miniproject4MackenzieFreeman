from django.contrib import admin
from .models import PolicySection, Policy, Definition

admin.site.register(Policy)
admin.site.register(PolicySection)
admin.site.register(Definition)
