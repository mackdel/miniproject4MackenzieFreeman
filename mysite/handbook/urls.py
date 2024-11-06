from django.urls import path

from . import views

app_name = 'handbook'
urlpatterns = [
    path('', views.index, name='index'),
    path('policy_sections/', views.policy_sections, name='policy_sections'),
    path('section/<str:section_number>/', views.section, name='section'),
]