from django.http import HttpResponse
from django.template import loader



def RunIndex(request):
    Titulo = "Hola Mundo"
    Body = "Hola Mundo 2"
    head = "Head"
    Plantilla = loader.get_template("index.html")
    Documento = Plantilla.render({"titulo":Titulo,"body": Body, "head": head})

    return HttpResponse(Documento) 