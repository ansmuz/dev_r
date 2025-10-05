from django.urls import path
from . import views

app_name = "resources"

urlpatterns = [
    path("react/libraries/", views.libraries, name="libraries"),
    path("tools/", views.tools, name="tools"),
]
    