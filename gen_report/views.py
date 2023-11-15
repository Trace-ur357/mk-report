from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout, views
from django.contrib.auth.decorators import login_required

from django.core.files.storage import FileSystemStorage

import os
from io import BytesIO
import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.graphics import renderPDF
from svglib.svglib import svg2rlg

import matplotlib.pyplot as plt



# Create your views here.

# Inicio de sesion
def inicioSesion(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'title': "Login | Mk-report",
            'h1' : "Inicio de sesión"
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'title': "Login | Mk-report",
                'h1' : "Inicio de sesión",
                'error': 'El usuario o la contraseña no es correcta'
            })
        else:
            login(request, user)
            return redirect('app')


# Cierre de sesion
def cerrarSesion(request):
    logout(request)
    return (redirect('signin'))


# Aplicación 
@login_required
def aplicacion(request):
    # Formulario
    if request.method == 'GET':
        return render(request, 'app.html', {
            'title': 'Mk - report',
            'h1' : "Generador de reportes"
        })
    else:
        try:
            # Recopilacion de datos
            ''' Obtener los datos del formulario '''
            documento = request.FILES["documento"]
             
            if documento.content_type != "text/csv": # Evaluando si entra un documento csv
                return render(request, 'app.html', {
                    'title': 'Mk - report',
                    'error': "solo acepta documentos .csv"
                })
            storage = FileSystemStorage(location="gen_report/documentos")
            storage.save(documento.name, documento)

        except:
            return render(request, 'app.html', {
                'title': 'Mk - report | Inicio',
                'error': 'Es necesario ingresar un archivo .csv'
            })

    # Manipulacion de datos
    csv_url = "gen_report/documentos/"+documento.name

    df = pd.read_csv(csv_url)
    pdf_url = documento.name.replace(".csv", ".pdf")


    ## Limpieza de datos
    df.fillna(0, inplace=True)

    ## Diagrama de ejemplo
    fig = plt.figure(figsize=(4,3))
    plt.barh(df['Nombre del anuncio'], df['Resultados'])


    plt.title('Resultados de la campaña')
    plt.xlabel('Anuncio')
    plt.ylabel('Resultados obtenidos')
    plt.yticks(rotation=45)

    for i, v in enumerate(df['Resultados']):
        plt.annotate(f"{v}", (v, df['Nombre del anuncio'][i]), ha="center", va="top")

    imgdata = BytesIO()

    fig.savefig(imgdata, format='svg')
    imgdata.seek(0)

    drawing=svg2rlg(imgdata)


    # Exportacion de datos
    pdf = canvas.Canvas("gen_report/documentos/pdf/"+pdf_url)
    pdf_path = os.path.dirname(f'gen_report/documentos/pdf/{pdf_url}')

    
    renderPDF.draw(drawing, pdf, 120, 400)

    # Implementacion de los datos
    pdf.drawCentredString(70, 800, "Reporte enviado")
    # pdf.showPage()
    pdf.save()



    # Exportacion de documento
    pdf = open(f'{pdf_path}/{pdf_url}', 'rb')

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename=""'

    
    storage.delete(documento.name)
    storage.delete(csv_url) 
    return response
    
    return render(request,'app.html', {
        'title': 'Mk - report | Inicio',
        'mensaje': 'El archivo fue subido con exito',
        'is_download' : True,
        'documento': request.FILES['documento']
    })

    
