from django.urls import path

from apps.polls.views import dashboard

urlpatterns = [
    path('', dashboard, name="dashboard")
]
