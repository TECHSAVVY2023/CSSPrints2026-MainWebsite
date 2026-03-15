from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import cssprints
from django.views.decorators.http import require_http_methods
from django.db import transaction
import json 


@require_http_methods(["POST"])
@csrf_exempt
def register(request):
    try:
        data = json.loads(request.body)
        firstname = data.get("firstname", "")
        lastname = data.get("lastname", "")

        with transaction.atomic():
            cssprints.objects.create(firstname=firstname, lastname=lastname)
            return JsonResponse({"message": "User registered successfully"})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
    
@require_http_methods(["GET"])
def get_all_users(request):
    try:
        data = list(cssprints.objects.values('firstname', 'lastname'))
        return JsonResponse(data, safe=False)
    
    except cssprints.DoesNotExist:
        return JsonResponse({"error": "Profile not found"}, status=404)