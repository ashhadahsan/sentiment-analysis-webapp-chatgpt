# Create your views here.
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Youtube
from .serializers import YoutubeSerializer
from django.http import JsonResponse

# Create your views here.

# importing packages
from pytube import YouTube
import subprocess
import whisper
def load_model():
    return whisper.load_model("base", download_root="./", in_memory=False)

class YoutubeView(APIView):
    def get(self, request, *args, **kwargs):
        result = Youtube.objects.all()
        serializers = YoutubeSerializer(result, many=True)
        return Response({"status": "success", "urls": serializers.data}, status=200)

    def post(self, request):
        url = request.data.get("url")
        print(url)
        yt = YouTube(str(url))
        video = yt.streams.filter(only_audio=True).first()

        # download the file
        out_file = video.download(output_path="./data/video/")
        title = yt.title.replace("?", "")

        command = f'''ffmpeg -i "data/video/{title}.mp4" -ab 160k -ac 2 -ar 44100 -vn -y "data/audio/{title}.wav"'''

        subprocess.call(command, shell=True)
        model = load_model()

        result = model.transcribe(f"data/audio/{title}.wav")
        return JsonResponse(
            {
                "status": "success",
                "transcription":result["text"]
            }
        )
