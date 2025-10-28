from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def saludo(request):
    return HttpResponse( 'SALUDEMOS LA PATRIA ORGULLOSA')


def info(request):
    return render(request,'pagina.html')


def biografia(request):
    return render(request, 'biografia.html', {
        'titulo': 'Mi Biografía',
        'biografia': {
            'nombre': 'Juan Pérez',
            'profesion': 'Desarrollador de Software',
            'resumen': 'Apasionado desarrollador con más de 5 años de experiencia en desarrollo web.',
            'experiencia': [
                'Desarrollador Full Stack en Empresa ABC (2020-presente)',
                'Desarrollador Frontend en XYZ Corp (2018-2020)',
                'Desarrollador Junior en StartUp Inc (2016-2018)'
            ],
            'educacion': [
                'Ingeniería en Informática - Universidad Nacional (2015)',
                'Certificación en Desarrollo Web - Instituto Tech (2016)'
            ],
            'habilidades': [
                'Python/Django',
                'JavaScript/React',
                'HTML5/CSS3',
                'SQL/PostgreSQL',
                'Git/GitHub'
            ]
        }
    })


