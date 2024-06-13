from django.shortcuts import render

# Create your views here.
def fileShare(request):
    return render(request, 'fileShare.html')