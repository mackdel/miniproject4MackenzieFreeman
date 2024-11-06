from django.shortcuts import get_object_or_404, render
from .models import PolicySection, Policy

def index(request):
    return render(request, 'handbook/index.html')

# Display all sections with their policies listed underneath.
def policy_sections(request):
    sections = PolicySection.objects.prefetch_related('policies')
    return render(request, 'handbook/policy_sections.html', {'sections': sections})

# Display all details for a specific section.
def section(request, section_number):
    section = get_object_or_404(PolicySection, number=section_number)
    policies = Policy.objects.filter(section=section).order_by('number')
    return render(request, 'handbook/section.html', {'section': section, 'policies': policies})
