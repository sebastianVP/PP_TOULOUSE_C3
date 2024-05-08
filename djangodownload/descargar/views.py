from django.shortcuts import render

from django.http.response import HttpResponse
import mimetypes
import os

# Create your views here.
def index(request):
    return render(request,'index.html')

def descargar_archivo(request):
    BASE_DIR= os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    #filename = "mi_archivo.txt"
    filename = "Python_for_Geeks_w_pacb151.pdf"
    # BASED DIR carpeta inicial django download la que se creo con 
    # django-admin startproject djangodownload
    # python manage.py startapp descargar
    filepath = BASE_DIR +'/descargar/archivos/' + filename
    # SI ES UN ARCHIVO PDF debemos leerlo en modo de lectura binario o rb
    mime_type, _ = mimetypes.guess_type(filepath)
    if mime_type== 'application/pdf':
        path= open(filepath,'rb')
    else:
        path= open(filepath,'r')

    response =  HttpResponse(path,content_type= mime_type)

    response['Content-Disposition'] = f'attachment; filename={filename}'

    return response