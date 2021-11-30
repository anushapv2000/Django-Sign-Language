#from django.shortcuts import render
#from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import StreamingHttpResponse
#from streamapp.camera import VideoCamera #2 IPWebCam #MaskDetect, LiveWebCam
# Create your views here.
import cv2
import os,urllib.request
from django.conf import settings
camera=cv2.VideoCapture(0)
Detection = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))

def index(request):
    return render(request, 'sili.html')

def sili(request):
    #return HttpResponse("SILI")
   return render(request, 'sili.html')


def frame_create():
    while True:
        ret,frame = camera.read()
        if not ret:
            break
        else:
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            detected = Detection.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
            for (x, y, w, h) in detected:
                cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=(0,255, 0), thickness=2)
            frame_flip = cv2.flip(frame,1)
            r,buf=cv2.imencode('.jpg',frame_flip)
            frame=buf.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        
def video_gen(request):
	return StreamingHttpResponse(frame_create(),
					content_type='multipart/x-mixed-replace; boundary=frame')

# Create your views here.
