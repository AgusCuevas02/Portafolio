from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from .models import Perfil, Habilidad, Experiencia, Educacion

def home(request):
    perfil = Perfil.objects.first() 
    
    # Filtramos las habilidades por categoría
    lenguajes = Habilidad.objects.filter(categoria='Lenguajes')
    frameworks = Habilidad.objects.filter(categoria='Frameworks')
    plataformas = Habilidad.objects.filter(categoria='Plataformas')
    herramientas = Habilidad.objects.filter(categoria='Herramientas')
    experiencias = Experiencia.objects.all().order_by('-fecha_inicio')
    context = {
        'perfil': perfil, 
        'lenguajes': lenguajes,
        'frameworks': frameworks,
        'plataformas': plataformas,
        'herramientas': herramientas,
        'experiencias': experiencias,
    }
    return render(request, 'core/home.html', context)



def sobre_mi(request):
    perfil = Perfil.objects.first()
    return render(request, 'core/sobre_mi.html', {'perfil': perfil})

def descargar_cv(request):
    perfil = Perfil.objects.first()
    habilidades = Habilidad.objects.all()
    experiencias = Experiencia.objects.all().order_by('-fecha_inicio')
    educaciones = Educacion.objects.all().order_by('-fecha_inicio')

    template = get_template('core/cv_template.html')
    context = {
        'perfil': perfil,
        'habilidades': habilidades,
        'experiencias': experiencias,
        'educaciones': educaciones,
    }
    
    html = template.render(context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="CV_Agustina_Narvaez.pdf"'

    pisa_status = pisa.CreatePDF(html, dest=response)
    if pisa_status.err:
       return HttpResponse('Error al generar el PDF', status=500)
    return response
