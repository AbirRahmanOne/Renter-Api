from django.http import JsonResponse
from rest_framework import status


def custom_404(request, exception=None):
    return JsonResponse({
        'status_code': 404,
        'error': 'The resource was not found'
    },
        status=status.HTTP_404_NOT_FOUND

    )