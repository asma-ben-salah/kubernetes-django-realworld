from rest_framework.views import APIView
from django.http import HttpResponse
from django.db import connection
from django.db.utils import OperationalError


class HealthCheckView(APIView):
    """
    Checks to see if the site is healthy.
    """
    def get(self, request, format=None):
      
        try:
           
            connection.ensure_connection()
            return HttpResponse("Connection ok")
        except  OperationalError:
            return HttpResponse("Connection false")