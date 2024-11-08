from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import PolicySection, Policy, PolicyRequest
from .forms import PolicyRequestForm
from django.urls import reverse

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

# View to handle question/clarification form for a specific policy
def request_form(request, policy_number):
    # Retrieve the policy object
    policy = get_object_or_404(Policy, number=policy_number)

    if request.method == "POST":
        # Instantiate the form with POST data
        form = PolicyRequestForm(request.POST)

        if form.is_valid():
            # Save the request and associate it with the policy
            policy_request = form.save(commit=False)
            policy_request.policy = policy
            policy_request.save()

            # Redirect to a success page after submission
            return HttpResponseRedirect(reverse("handbook:request_success"))
    else:
        # For GET requests, render an empty form
        form = PolicyRequestForm()

    return render(
        request,
        "handbook/request_form.html",
        {
            "policy": policy,
            "form": form,
        },
    )

def request_success(request):
    return render(request, "handbook/request_success.html")
