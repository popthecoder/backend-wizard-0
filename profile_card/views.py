import requests
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
import os
import logging


# Set up logging
logger = logging.getLogger(__name__)

@csrf_exempt
@require_http_methods(["GET"])
def me_endpoint(request):
    try:
        response = requests.get('https://catfact.ninja/fact, timeout=5')
        response.raise_for_status()
        cat_fact = response.json().get('fact', 'No fact found.')
        logger.info(f"Successfully fetched cat fact at {datetime.utcnow().isoformat()}")
        
    except requests.exceptions.Timeout:
        logger.error("Cat fact API request timed out.")
        cat_fact = "Cat spend 70% of their lives sleeping.(Fallback fact - API timeout)"
        
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching cat fact: {e}")
        cat_fact = "Cats have five toes on their front paws, but only four on the back.(Fallback fact - API unavailable)"
        
        
    # Build the response data
    data = {
        "status": "success",
        "user": {
            "name": os.getenv('USER_NAME', 'Inaboya Taofeeq'),
            "email": os.getenv('USER_EMAIL', 'taofeeq476@gmail.com'),
            "stack": os.getenv('USER_STACK', 'Python/Django'),
        },
        "timestamp": datetime.utcnow().isoformat() + 'Z',
        "fact": cat_fact
    }
    
    # Return the JSON response
    return JsonResponse(data, status=200, content_type="application/json")


@csrf_exempt
@require_http_methods(["GET"])
def health_check(request):
    data = {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + 'Z'
    }
    return JsonResponse(data, status=200)
