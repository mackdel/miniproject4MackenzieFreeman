from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import FormView
from django.shortcuts import get_object_or_404
from .models import PolicySection, Policy
from .forms import PolicyRequestForm

# Home page view: Displays the homepage for authenticated users
class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "handbook/index.html"


# Policy sections view: Displays all policy sections with their related policies listed underneath
class PolicySectionsView(LoginRequiredMixin, ListView):
    model = PolicySection
    template_name = "handbook/policy_sections.html"
    context_object_name = "sections"

    def get_queryset(self):
        # Prefetch related policies for efficiency
        return PolicySection.objects.prefetch_related('policies')


# Section detail view: Displays details of a single section and its related policies
class SectionDetailView(LoginRequiredMixin, DetailView):
    model = PolicySection
    template_name = "handbook/section.html"
    context_object_name = "section"
    slug_field = "number"  # Match section based on the 'number' field (e.g., 1.0)
    slug_url_kwarg = "section_number"  # URL parameter to look up the section

    def get_context_data(self, **kwargs):
        # Add policies in the section to the context
        context = super().get_context_data(**kwargs)
        context['policies'] = Policy.objects.filter(section=self.object).order_by('number')
        return context


# Policy request form view: Allows users to submit questions/clarifications for a specific policy
class PolicyRequestFormView(LoginRequiredMixin, FormView):
    form_class = PolicyRequestForm
    template_name = "handbook/request_form.html"

    def get_success_url(self):
        # Redirect to the success page after form submission
        return reverse("handbook:request_success")

    def get_context_data(self, **kwargs):
        # Add the related policy to the context
        context = super().get_context_data(**kwargs)
        context['policy'] = get_object_or_404(Policy, number=self.kwargs['policy_number'])
        return context

    def form_valid(self, form):
        # Save the form and associate it with the specific policy
        policy = get_object_or_404(Policy, number=self.kwargs['policy_number'])
        policy_request = form.save(commit=False)
        policy_request.policy = policy
        policy_request.save()
        return super().form_valid(form)


# Request success view: Displays a confirmation page after a successful form submission
class RequestSuccessView(TemplateView):
    template_name = "handbook/request_success.html"
