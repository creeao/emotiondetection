from django.shortcuts import render, redirect
from django.conf import settings
from django.core.files.storage import FileSystemStorage
# Create your views here.


def home_view(request, *args, **kwargs):
    context = {}
    return render(request, "home.html", context)


def upload_view(request, *args, **kwargs):
    if request.method == 'POST' and request.FILES['myfile']:
        if 'image' in request.FILES['myfile'].content_type:
            myfile = request.FILES['myfile']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            return render(request, "upload.html", {'uploaded_file_url': uploaded_file_url})
        else:
            return render(request, "upload.html", {'uploaded_file_url': 'It has to be an image'})

    return render(request, "upload.html")
