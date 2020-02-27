from django.urls import path
from BackendAPI.views import View


view = View()

urlpatterns = [
    path('gender/', view.get_predictions),
]
