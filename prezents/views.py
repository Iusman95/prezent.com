from django.shortcuts import render

from django.http import HttpResponseRedirect
# Create your views here.

def index(requests):
    return render(requests, 'prezents/index.html')


""" def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/index/')    
    else:
        form = UploadFileForm()

    return render(request, 'prezents/upload_file.html', {'form': form})

def handle_uploaded_file(f):
    with open('data.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk) """