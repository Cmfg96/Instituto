from django.shortcuts import render

# Create your views here.

#declaracion de un objeto persona
class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()

def index(request):

    hijo=persona("Juan Perez", "7")

    lista=["Lazaña", "Charquican", "Porotos Granados"]

    context={"hijo":hijo, "nombre":"Claudia Andrea", "comidas":lista}

    return render(request, 'alumnos/index.html', context)