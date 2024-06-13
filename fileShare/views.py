from django.shortcuts import render,HttpResponse
from django.http import Http404
from .forms import UploadFileForm
from .models import FileModel

# Create your views here.
def fileUpload(request):
    
    form = UploadFileForm(request.POST, request.FILES)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return HttpResponse("File uploaded successfully")
        else:
            return Http404("Error uploading file")

    else:
        form = UploadFileForm()
    
    return render(request, 'fileUpload.html', {'form': form, 'submitted': True}  )