from django.shortcuts import redirect, render
from .models import Encuesta
from django.db.models import Avg, Count, F, Sum


# Create your views here.

def index(request):
    return render(request, 'index.html')

def reguistrarEncuesta(request):
    correo = request.POST['txtCorreo']
    edad = request.POST['txtEdad']
    sexo = request.POST['txtSexo']
    fav = request.POST['txtFav']
    promFB = request.POST['intFB']
    promWA = request.POST['intWA']
    promTW = request.POST['intTW']
    promIN = request.POST['intIN']
    promTK = request.POST['intTK']

    encuesta = Encuesta.objects.create(
        correo = correo,
        rango_edad = edad,
        sexo = sexo,
        red_social_fav = fav, 
        prom_FB = promFB,
        prom_WA = promWA,
        prom_TW = promTW,
        prom_IN = promIN,
        prom_TK = promTK
    )
    return redirect('/')

def estadisticas(request):
    if (Encuesta.objects.count() < 1):
        mensaje  = "No hay datos suficientes, pruebe llenando una encuesta primero"
        return render(request, 'vacio.html',{'mensaje':mensaje})
    # Total de encuestas
    encuestas = Encuesta.objects.count()

    # Tiempo promedio por red social
    prom_FB = Encuesta.objects.aggregate(Avg('prom_FB'))
    prom_WA = Encuesta.objects.aggregate(Avg('prom_WA'))
    prom_TW = Encuesta.objects.aggregate(Avg('prom_TW'))
    prom_IN = Encuesta.objects.aggregate(Avg('prom_IN'))
    prom_TK = Encuesta.objects.aggregate(Avg('prom_TK'))

    # Redes favoritas
    fav_FB = Encuesta.objects.filter(red_social_fav = "Facebook").count()
    fav_WA = Encuesta.objects.filter(red_social_fav = "WhastApp").count()
    fav_TW = Encuesta.objects.filter(red_social_fav = "Twitter").count()
    fav_IN = Encuesta.objects.filter(red_social_fav = "Instagram").count()
    fav_TK = Encuesta.objects.filter(red_social_fav = "Tiktok").count()

    # Rango de edad que más use cada red social
    
    rangos = ['18-25', '26-33', '34-40', '40+']
    promedios = ['prom_FB', "prom_WA", "prom_TW", "prom_IN", "prom_TK"]
    redes = []
    for p in promedios:
        maximo = []
        for r in rangos:
            if (Encuesta.objects.filter(rango_edad = r).count() < 1):
                maximo.append(0)
                continue
            else:
                prom = Encuesta.objects.filter(rango_edad = r).aggregate(promedio = Sum(F(p))/Count('rango_edad'))
                maximo.append(prom['promedio'])
                index_max = max(range(len(maximo)), key = maximo.__getitem__)

        if(max(maximo) < 1):
            redes.append('----')
        else:
            redes.append(rangos[index_max])

    rango_FB = redes[0]
    rango_WA = redes[1]
    rango_TW = redes[2]
    rango_IN = redes[3]
    rango_TK = redes[4]


    return render(request,'estadisticas.html',{"encuestas": encuestas,
                                                "prom_WA": prom_WA,
                                                "prom_FB": prom_FB,
                                                "prom_TW": prom_TW,
                                                "prom_IN": prom_IN,
                                                "prom_TK": prom_TK,
                                                "fav_FB": fav_FB,
                                                "fav_WA": fav_WA, 
                                                "fav_TW": fav_TW, 
                                                "fav_IN": fav_IN, 
                                                "fav_TK": fav_TK,
                                                "rango_FB": rango_FB,
                                                "rango_WA": rango_WA,
                                                "rango_TW": rango_TW,
                                                "rango_IN": rango_IN,
                                                "rango_TK": rango_TK})
