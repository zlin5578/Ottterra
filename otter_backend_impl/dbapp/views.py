# dbapp/views.py

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from PIL import Image
from io import BytesIO

from .remote_inference import remote_trellis_infer

@csrf_exempt
def upload_and_infer(request):
    if request.method == 'POST':
        try:
            image_file = request.FILES['image']
            image = Image.open(image_file)
            video_url = remote_trellis_infer(image)
            return render(request, 'result.html', {'video_url': video_url})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return render(request, 'upload.html')

@csrf_exempt
def getModelbyPicInput(request):
    if request.method == 'POST':
        try:
            image_file = request.FILES['image']
            image = Image.open(image_file)
            video_url = remote_trellis_infer(image)
            return render(request, 'model_result.html', {'video_url': video_url})
        except Exception as e:
            return render(request, 'model_result.html', {'error': str(e)})
    return render(request, 'model_upload.html')


def gradio_page(request):
    return render(request, 'gradio_embed.html')