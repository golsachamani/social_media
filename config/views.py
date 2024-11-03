from django.conf.urls.static import static
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


@csrf_exempt
def upload_image(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get("file")
        if uploaded_file:
            file_name = default_storage.save(
                f"posts/{uploaded_file.name}", ContentFile(uploaded_file.read())
            )
            file_url = default_storage.url(file_name)
            return JsonResponse({"location": file_url})
    return JsonResponse({"error": "Image upload failed"}, status=400)
