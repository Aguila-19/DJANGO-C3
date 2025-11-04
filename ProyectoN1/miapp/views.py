from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def limpieza(request):
    """Renderiza la plantilla limpienza.html.

    Nota: el nombre del archivo lo he tomado tal cual como "limpienza.html"
    según tu solicitud. Si la plantilla se llama "limpieza.html" cambia el
    nombre en el render.
    """
    return render(request, 'limpieza.html')
