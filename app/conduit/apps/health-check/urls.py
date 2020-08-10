from django.conf.urls import url

from .views import  HealthCheckView

urlpatterns = [
    url(r'^health_check/?$', HealthCheckView.as_view()),
]
