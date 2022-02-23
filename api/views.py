from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from .models import *

# What to do?
# Search
# Fetch


@api_view(["GET"])
def get_model(request):
    model_id = request.GET.get("id")
    model_result = ThreeDModel.objects.get(id=int(model_id))
    return JsonResponse(
        {
            "name": model_result["name"],
            "description": model_result["description"],
            "more_info_link": model_result["more_info_link"],
            "more_info_text": model_result["more_info_text"],
            "file": "f"
        }
    )


@api_view(["GET"])
def search(request):
    query = request.GET.get("query")
    query_result = ThreeDModel.objects.filter(description__icontains=query)
    print(query_result)
    return JsonResponse(
        [
            {
                "name": x.name,
                "description": x.description,
                "more_info_link": x.more_info_link,
                "more_info_text": x.more_info_text,
                "file": x.model.url,
                "image": x.image.url
            } for x in query_result
        ],
        safe=False
    )

# @api_view(["GET"])
# def search(request):
