from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import matplotlib.pyplot as plt
import cv2,os,urllib.request
import sys
face_detection_videocam = cv2.CascadeClassifier(os.path.join(
			settings.BASE_DIR,'opencv_haarcascade_data/haarcascade_frontalface_default.xml'))
# Create your views here.


def index(request, *args, **kwargs):
	if request.method == 'POST' and request.FILES['myfile']:
		if 'image' in request.FILES['myfile'].content_type:
			myfile = request.FILES['myfile']
			fs = FileSystemStorage()
			filename = fs.save(myfile.name, myfile)
			# Create the haar cascade
			faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

			# Read the image
			image = cv2.imread('C:/Users/G/Desktop/Test.jpg')
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

			# Detect faces in the image
			faces = faceCascade.detectMultiScale(
				gray,
				scaleFactor=1.1,
				minNeighbors=5,
				minSize=(30, 30),
				flags = cv2.CASCADE_SCALE_IMAGE	
			)

		

			# Draw a rectangle around the faces
			for (x, y, w, h) in faces:
				cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

			#cv2.imshow("Faces found", image)
			im = cv2.imread(image)
			im_resized = cv2.resize(im, (224, 224), interpolation=cv2.INTER_LINEAR)

			plt.imshow(cv2.cvtColor(im_resized, cv2.COLOR_BGR2RGB))
			plt.show()

			return render(request, "upload/home.html", {'uploaded_file_url': "Found {0} faces!".format(len(faces))})
		else:
			return render(request, "upload/home.html", {'uploaded_file_url': 'It has to be an image'})

	return render(request, 'upload/home.html')