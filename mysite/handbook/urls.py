from django.urls import path

from . import views

app_name = 'handbook'
urlpatterns = [
    path('', views.index, name='index'),
    path('policy_sections/', views.policy_sections, name='policy_sections'),
    path('section/<str:section_number>/', views.section, name='section'),
    path('policy/<str:policy_number>/', views.request_form, name='request_form'),
    path('request_success/', views.request_success, name='request_success'),
]