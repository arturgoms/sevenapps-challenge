from django.urls import path, include

app_name = "api"

urlpatterns = [
    path("settings/", include("apps.api.settings.urls")),
    path("", include("apps.api.healthcheck.urls")),
    path("", include("apps.api.person.urls")),
    path("", include("apps.api.company.urls")),
]
