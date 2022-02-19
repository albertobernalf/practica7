import json
from django import forms
import cv2
import numpy as np
#import onnx as onnx
#import onnxruntime as ort
import pyttsx3
import speech_recognition as sr
from django.core.serializers import serialize

from django.db.models.functions import Cast, Coalesce
from django.utils.timezone import now
from django.db.models import Avg, Max, Min
from .forms import historiaForm, historiaExamenesForm

from clinico.models import Historia, HistoriaExamenes, Examenes, TiposExamen, EspecialidadesMedicos, Medicos
from usuarios.models import Usuarios, TiposDocumento

from django.contrib import messages
from django.shortcuts import  render, get_object_or_404, redirect, HttpResponse, HttpResponseRedirect
from django.core.exceptions import ValidationError
from django.urls import reverse, reverse_lazy
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView
from django.http import JsonResponse
import MySQLdb

# Create your views here.


def prueba(request):
    return render(request, "index.html")

def resMotivoInvidente(request):
    print("Entre a Reconocer audio Motivo Consulta")
    r = sr.Recognizer()
    print(sr.Microphone.list_microphone_names())

    with sr.Microphone(device_index=0) as source:  # use the default microphone as the audio source
        print("Por Favor cuenteme :")

        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)  # listen for the first phrase and extract it into audio data
        print("pase")
    try:
        print("No haga nada")
        # print("You said " + r.recognize_google(audio , language = 'en-IN', show_all = True))  # recognize speech using Google Speech Recognition
        # text = r.recognize_google(audio, language = 'es-CO', show_all = True )
        text = r.recognize_google(audio, language='es-CO', show_all=True)
      #  jsonToPython = json.loads(format(text))
        print('You said: {}'.format(text))


    except LookupError:  # speech is unintelligible
        print("Could not understand audio")

     # return render(request, "home.html")

    datos = {"Respuesta": format(text)}
    print(datos)

    return HttpResponse(json.dumps(datos))




def motivoInvidente(request):
    print("Entre al Moivo invidente Audio")
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    texto = request.GET["nombre"]
    engine.say(texto)
    engine.runAndWait()

    return redirect('/menu/')


def buscaExamenes(request):
    print("Entre a Buscar Examenes Clinicos")

    id = request.GET.get('id')
    print (id)



    datos = {"id": id}
    print(datos)

    return  HttpResponse(json.dumps(datos))

def consecutivo_folios(request):

    print ("Entre a Consecutivo_folios")
    id_tipo_doc =  request.POST["id_tipo_doc"]
    documento = request.POST["documento"]

    id_tipo_doc1 = TiposDocumento.objects.get(id=id_tipo_doc)

    ultimofolio = Historia.objects.all().filter(id_tipo_doc=id_tipo_doc1.id).filter(documento=documento).aggregate(maximo = Coalesce(Max('folio'), 0))
    ultimofolio2= (ultimofolio['maximo'] + 1)

    datos = {"ultimofolio": ultimofolio2}
    print(datos)

    return HttpResponse(json.dumps(datos))


def historiaExamenesView(request):
    print("Entre por historiaExamenesView")
    form2 = historiaExamenesForm(request.POST or None)
    print("Esta es form2")
    print(form2)
    data = {}
    if request.is_ajax():
        if form2.is_valid():
            print("Entere a Grabar")
            form2.save()
            data['Nombre'] = form2.cleaned_data.get('documento')
    context = {'form2': form2}

    # return redirect('/menu/')
    # return render(request, 'historia_form.html', context)
    return HttpResponse(data)


def historia1View(request):
    print("Entre Ajax de Historia1View")

    form = historiaForm(request.POST)
    print(form)
    data1 = {}
    if request.is_ajax():
        print("Entre Ajax Historia a validadr Form")
        if form.is_valid():
            print("Entre a Grabar Ajax Historia")
            form.save()
            data1 ={'Nombre', form.cleaned_data.get('documento')}

            return HttpResponse(data1)
        else:
            print("Formulario Ajax invalido")
            return HttpResponse("Formulario Ajax invalido")
    return HttpResponse("Problemas con AJAx")


def historiaView(request):
    print("Entre por el view historiaView")

    form = historiaForm(request.POST)

    if request.method == 'POST':
        print("entre por POST")

        # Check if the form is valid:
        if form.is_valid():
            form1 = form.cleaned_data
            print("A grabar")

            grabo = Historia(id_tipo_doc=form1['id_tipo_doc'],
                             documento=form1['documento'],
                             folio=form1['folio'],
                             fecha=form1['fecha'],
                             id_especialidad=form1['id_especialidad'],
                             id_medico=form1['id_medico'],
                             motivo=form1['motivo'],
                             subjetivo=form1['subjetivo'],
                             objetivo=form1['objetivo'],
                             analisis=form1['analisis'],
                             plan=form1['plan'],
                             estado_folio=form1['estado_folio'])
            grabo.save()
            grabo.id
            print("yA grabe")

            messages.success(request, 'Informacion guardada')

            return redirect('/historiaView')
        else:
            print("Error")
            print(form.errors)
            messages.error(request, form.errors['documento'])

    else:
        print("pase por el else")

        form = historiaForm()
        form2 = historiaExamenesForm()

        return render(request, 'historia_form.html', {'form': form, 'form2': form2})

    form2 = historiaExamenesForm()
    return render(request, 'historia_form.html', {'form': form, 'form2': form2})


def motivoSeñas(request):
    print("Entre Reproduce SeÃ±as")
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    texto = step_5_camera()
    print("De devuelta el texto es : ")
    print(texto)

    #  texto = request.GET["nombre"]
    engine.say(texto)
    engine.runAndWait()

    datos = {"mensaje": texto}
    print(datos)

    return HttpResponse(json.dumps(datos))

    return redirect('/menu/')


def subjetivoSeñas(request):
    print("Entre Reproduce SubjetivoSeñas")
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)

    texto = step_5_camera()
    print("De devuelta el texto es : ")
    print(texto)

    #  texto = request.GET["nombre"]
    engine.say(texto)
    engine.runAndWait()

    datos = {"mensaje": texto}
    print(datos)

    return HttpResponse(json.dumps(datos))

    return redirect('/menu/')


def step_5_camera():
    print("Entree a Camara")
    onnx_file = 'C:\\EntornosPython\\vulne\\vulnerable\\signlanguage.onnx'
    onnx_model = onnx.load(onnx_file)
    onnx.checker.check_model(onnx_model)
    print('The model is checked!')

    # constants
    index_to_letter = list('ABCDEFGHIKLMNOPQRSTUVWXY')
    mean = 0.485 * 255.
    std = 0.229 * 255.
    print("Adentro1")
    # create runnable session with exported model
    ort_session = ort.InferenceSession(onnx_file)
    print("Adentro11")
    cap = cv2.VideoCapture(0)
    mensaje = []
    print("Adentro2")

    # while True:
    for t in range(15):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # preprocess data
        frame = center_crop(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
        x = cv2.resize(frame, (28, 28))
        x = (x - mean) / std

        x = x.reshape(1, 1, 28, 28).astype(np.float32)
        y = ort_session.run(None, {'input': x})[0]

        index = np.argmax(y, axis=1)
        letter = index_to_letter[int(index)]

        mensaje.append(letter)
        print("las letras son: %s", mensaje)

        cv2.putText(frame, letter, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0, 255, 0), thickness=2)
        cv2.imshow("Sign Language Translator", frame)
        print("Adentro3")
        #  if cv2.waitKey(1) & 0xFF == ord('q'):
        #  break

    # cv2.waitKey(0)
    cv2.destroyAllWindows()
    cap.release()

    print("El mensaje Final es : ")

    resultado = ''

    for x in range(0, len(mensaje)):
        resultado = resultado + mensaje[x]

    return (resultado)


def center_crop(frame):
    h, w, _ = frame.shape
    start = abs(h - w) // 2
    if h > w:
        return frame[start: start + w]
    return frame[:, start: start + h]


class nuevoView(TemplateView):
    print("Encontre")
    template_name = 'historia_form.html'

    def post(self, request, *args, **kwargs):
        print("Entre POST")
        data = {}
        try:
            print("Entre try")
            if 'action' in request.POST:
                action = request.POST['action']
                id = request.POST['id']
            else:
                print ("Falsa action")
                action = False
            print(action)
            print(id)
           
            action = request.POST.get('action', False)

            if action == 'BuscaExamenes':
                print("Entre Action")
                data = []
                for s in Examenes.objects.all().filter(id_TipoExamen=request.POST["id"]):
                      data.append({'id': s.id, 'nombre': s.nombre})
                      print (data[0])
            else:
              data[0] = "Ha ocurrido un error"

            if action == 'BuscaEspecialidad':
                  print("Entre Action especialidad")
                  print (id)
                  data = []
                  for s in EspecialidadesMedicos.objects.all().filter(id_especialidad=request.POST["id"]):
                      medico = Medicos.objects.get(nombre=s.id_medico)

                      data.append({'id': s.id, 'nombre': medico.nombre})
                      print(data[0])
            else:
                  data[0] = "Ha ocurrido un error"

        except Exception as  e:
              print ("Exception")
              data[0] = atrr(e)

        print("me devuelvo con ")

        return HttpResponse(json.dumps(data))

       # return JsonResponse(data, safe=False)

    def get_context_data(self, documento, **kwargs):
        print("Entre a Contexto")
        print (documento)
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mi gran Template'
        context['form']  = historiaForm
        context['form2'] = historiaExamenesForm
        return context



class crearHistoriaClinica(TemplateView):
    print("Entre a Crear Historia Clinica")

    template_name = 'clinico/historiaClinica.html'
    print("Entre a Registrar Historia")

    def post(self, request, *args, **kwargs):
        print("Entre POST de Crear Admisiones")
        data = {}
        context = {}
        return HttpResponse(json.dumps(data))

    def get_context_data(self,  **kwargs):
        print("Entre a Contexto Historia Clinica")

        context = super().get_context_data(**kwargs)
        context['title'] = 'Mi gran Template'

        return context



class crearHistoriaClinica1(TemplateView):
    print("Entre a Crear Historia Clinica1")




    template_name = 'clinico/historiaClinica.html'
    print("Entre a Registrar Historia")

    def post(self, request, *args, **kwargs):
        print("Entre POST de crearHistoriaClinica1")
        data = {}
        context = {}

        form = historiaForm(request.POST)

        if self.request.is_ajax and self.request.method == "POST":
            print ("Entre Ajax")

            motivo = request.POST["motivo"]
            print (motivo)
            objetivo = request.POST["objetivo"]
            print(objetivo)
            subjetivo = request.POST["subjetivo"]
            print(subjetivo)
            analisis = request.POST["analisis"]
            plan = request.POST["plan"]
            print(plan)
            print(analisis)
            tipoDoc = request.POST["tipoDoc"]
            documento = request.POST["documento"]
            fecha = request.POST["fecha"]

            causasExterna = request.POST["causasExterna"]
            dependeciadRealizado = request.POST["dependeciadRealizado"]
            planta = request.POST["planta"]
            usuarioRegistro = request.POST["usuarioRegistro"]
            #tablaExamenes = request.POST["tablaExamenes"]
            #print (tablaExamenes)


            #tablaExamenesRad = request.POST["tablaExamenesRad"]
            #print (tablaExamenesRad)


            if form.is_valid():
              nueva_historia = Historia(
                    tipoDoc = form.cleaned_data.get('tipoDoc'),
                    documento=form.cleaned_data.get('documento'),
                    consecAdmision=form.cleaned_data.get('consecAdmision'),
                    folio=form.cleaned_data.get('folio'),
                    fecha=form.cleaned_data.get('fecha'),
                    tiposFolio=form.cleaned_data.get('tiposFolio'),
                    causasExterna=form.cleaned_data.get('causasExterna'),
                    dependenciasRealizado=form.cleaned_data.get('dependenciasRealizado'),
                    especialidades=form.cleaned_data.get('especialidades'),
                    planta=form.cleaned_data.get('planta'),
                    motivo=form.cleaned_data.get('motivo'),
                    subjetivo=form.cleaned_data.get('subjetivo'),
                    objetivo=form.cleaned_data.get('objetivo'),
                    analisis=form.cleaned_data.get('analisis'),
                    plan=form.cleaned_data.get('plan'),
                    fechaRegistro=form.cleaned_data.get('fechaRegistro'),
                    usuarioRegistro=form.cleaned_data.get('usuarioRegistro'),
                    estadoReg=form.cleaned_data.get('estadoReg'))
              nueva_historia.save
            return HttpResponse(json.dumps(data))





    def get_context_data(self,  **kwargs):
        print("Entre a Contexto Historia Clinica")

        context = super().get_context_data(**kwargs)
        context['title'] = 'Mi gran Template'
        context['historiaForm'] = historiaForm

        # Combo Diagnosticos



        miConexiont = MySQLdb.connect(host='localhost', user='root', passwd='', db='vulnerable9')
        curt = miConexiont.cursor()

        comando = "SELECT p.id id, p.nombre  nombre FROM clinico_diagnosticos p"

        curt.execute(comando)
        print(comando)

        diagnosticos = []
        diagnosticos.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            diagnosticos.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(diagnosticos)

        context['Diagnosticos'] = diagnosticos

        # Fin combo Diagnosticos

        # Combo Laboratorios

        miConexiont = MySQLdb.connect(host='localhost', user='root', passwd='', db='vulnerable9')
        curt = miConexiont.cursor()

        comando = "SELECT e.id id, e.nombre nombre FROM clinico_tiposExamen t, clinico_examenes e WHERE t.id = e.TiposExamen_id and t.id ='2'"

        curt.execute(comando)
        print(comando)

        laboratorios = []
        laboratorios.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            laboratorios.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(laboratorios)

        context['Laboratorios'] = laboratorios

        # Fin combo Laboratorios

        # Combo Radiologia


        miConexiont = MySQLdb.connect(host='localhost', user='root', passwd='', db='vulnerable9')
        curt = miConexiont.cursor()

        comando = "SELECT e.id id, e.nombre nombre FROM clinico_tiposExamen t, clinico_examenes e WHERE t.id = e.TiposExamen_id and t.id ='1'"

        curt.execute(comando)
        print(comando)

        radiologias = []
        radiologias.append({'id': '', 'nombre': ''})

        for id, nombre in curt.fetchall():
            radiologias.append({'id': id, 'nombre': nombre})

        miConexiont.close()
        print(radiologias)

        context['Radiologias'] = radiologias

        # Fin combo Radiologia



        return context



def buscarAdmisionClinico(request):
    context = {}


    print("Entre Buscar Admision" )
    BusTipoDoc = request.POST["busTipoDoc"]
    BusDocumento = request.POST["busDocumento"]
    BusHabitacion = request.POST["busHabitacion"]



    BusDesde = request.POST["busDesde"]
    BusHasta = request.POST["busHasta"]
    BusEspecialidad = request.POST["busEspecialidad"]
    print ("Especialidad = ", BusEspecialidad )
    BusMedico = request.POST["busMedico"]
    BusServicio = request.POST["busServicio"]
    BusPaciente = request.POST["busPaciente"]
    Perfil = request.POST['Perfil']

    Sede = request.POST["Sede"]
    context['Sede'] = Sede

    # Consigo la sede Nombre

    miConexion = MySQLdb.connect(host='localhost', user='root', passwd='', db='vulnerable9')
    cur = miConexion.cursor()
    comando = "SELECT nombre   FROM sitios_sedesClinica WHERE id ='" + Sede + "'"
    cur.execute(comando)
    print(comando)

    nombreSedes = []

    for nombre in cur.fetchall():
        nombreSedes.append({'nombre': nombre})

    miConexion.close()
    print(nombreSedes)
    nombresede1 = nombreSedes[0]

    context['NombreSede'] = nombresede1


    Username = request.POST["Username"]
    context['Username'] = Username
    Username_id = request.POST["Username_id"]
    context['Username_id'] = Username_id




    print("Sede  = ", Sede)

    print("BusHabitacion= ", BusHabitacion)
    print("BusTipoDoc=", BusTipoDoc)
    print("BusDocumento=" , BusDocumento)
    print("BusDesde=", BusDesde)
    print("BusHasta=", BusHasta)
    print("La sede es = " , Sede)
    print("El busServicio = ", BusServicio)
    print("El busEspecialidad = ", BusEspecialidad)
    print("El busSMedico = ", BusMedico)
    print("El busSMedico = ", BusPaciente)

    ingresos = []

    # Combo de Servicios
    miConexiont = MySQLdb.connect(host='localhost', user='root', passwd='', db='vulnerable9')
    curt = miConexiont.cursor()
    comando = "SELECT ser.id id ,ser.nombre nombre FROM sitios_serviciosSedes sed, clinico_servicios ser Where sed.sedesClinica_id ='" + str(Sede) + "' AND sed.servicios_id = ser.id"
    curt.execute(comando)
    print(comando)

    servicios = []
    servicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        servicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(servicios)

    context['Servicios'] = servicios

    # Fin combo servicios

    # Combo de SubServicios
    miConexiont = MySQLdb.connect(host='localhost', user='root', passwd='', db='vulnerable9')
    curt = miConexiont.cursor()
    comando = "SELECT sub.id id ,sub.nombre nombre  FROM sitios_serviciosSedes sed, clinico_servicios ser  , sitios_subserviciossedes sub Where sed.sedesClinica_id ='" + str(
        Sede) + "' AND sed.servicios_id = ser.id and  sed.sedesClinica_id = sub.sedesClinica_id and sed.servicios_id =sub.servicios_id"
    curt.execute(comando)
    print(comando)

    subServicios = []
    subServicios.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        subServicios.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(subServicios)

    context['SubServicios'] = subServicios

    # Fin combo SubServicios


    # Combo TiposDOc
    miConexiont = MySQLdb.connect(host='localhost', user='root', passwd='', db='vulnerable9')
    curt = miConexiont.cursor()
    comando = "SELECT id ,nombre FROM usuarios_TiposDocumento"
    curt.execute(comando)
    print(comando)

    tiposDoc = []
    tiposDoc.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        tiposDoc.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(tiposDoc)

    context['TiposDoc'] = tiposDoc

    # Fin combo TiposDOc


    # Combo Habitaciones
    miConexiont = MySQLdb.connect(host='localhost', user='root', passwd='', db='vulnerable9')
    curt = miConexiont.cursor()
    comando = "SELECT id ,nombre FROM sitios_dependencias where sedesClinica_id = '" + str(Sede) +"' AND dependenciasTipo_id = 2"
    curt.execute(comando)
    print(comando)

    habitaciones = []
    habitaciones.append({'id': '', 'nombre': ''})


    for id, nombre in curt.fetchall():
        habitaciones.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(habitaciones)

    context['Habitaciones'] = habitaciones

    # Fin combo Habitaciones

    # Combo Especialidades
    miConexiont = MySQLdb.connect(host='localhost', user='root', passwd='', db='vulnerable9')
    curt = miConexiont.cursor()
    comando = "SELECT id ,nombre FROM clinico_Especialidades"
    curt.execute(comando)
    print(comando)

    especialidades = []
    especialidades.append({'id': '', 'nombre': ''})

    for id, nombre in curt.fetchall():
        especialidades.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(especialidades)

    context['Especialidades'] = especialidades

    # Fin combo Especialidades

    # Combo Medicos
    miConexiont = MySQLdb.connect(host='localhost', user='root', passwd='', db='vulnerable9')
    curt = miConexiont.cursor()
    comando = "SELECT p.id id, p.nombre  nombre FROM planta_planta p ,  planta_perfilesplanta perf WHERE p.sedesClinica_id = perf.sedesClinica_id and  perf.sedesClinica_id = '" + str(
        Sede) + "' AND perf.tiposPlanta_id = 1 and p.id = perf.planta_id"

    curt.execute(comando)
    print(comando)

    medicos = []
    medicos.append({'id': '', 'nombre': ''})


    for id, nombre in curt.fetchall():
        medicos.append({'id': id, 'nombre': nombre})

    miConexiont.close()
    print(medicos)



    context['Medicos'] = medicos

    # Fin combo Medicos


    # Busco Nombre de Habitacion

    miConexiont = MySQLdb.connect(host='localhost', user='root', passwd='', db='vulnerable9')
    curt = miConexiont.cursor()
    comando = "SELECT d.id id, d.nombre  nombre FROM sitios_dependencias d WHERE d.id = '" + str(BusHabitacion) + "'"
    curt.execute(comando)
    print(comando)

    NombreHabitacion = ""


    for id, nombre in curt.fetchall():
        NombreHabitacion = nombre

    miConexiont.close()
    print("NombreHabitacion = ", NombreHabitacion)


    # Fin busco nombre de habitacion



    miConexion1 = MySQLdb.connect(host='localhost', user='root', passwd='', db='vulnerable9')
    cur1 = miConexion1.cursor()

 #   detalle = "SELECT i.tipoDoc_id tipoDoc, i.documento_id documento, u.nombre  nombre , i.consec consec , fechaIngreso , fechaSalida, serviciosIng_id,  dependenciasIngreso_id , dxIngreso_id FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep  WHERE i.sedesClinica_id = dep.sedesClinica_id AND i.dependenciasActual_id = dep.id AND i.sedesClinica_id = '" +    str(Sede) +"'"
  #  detalle = "SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , fechaIngreso , fechaSalida, ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag  WHERE i.sedesClinica_id = dep.sedesClinica_id AND i.serviciosActual_id = dep.servicios_id AND i.serviciosActual_id = ser.id  AND i.dependenciasActual_id = dep.id AND  i.dependenciasIngreso_id = dep.id AND i.sedesClinica_id= '" + str(Sede) + "' AND dep.sedesClinica_id = i.sedesClinica_id AND i.sedesClinica_id = ser.sedesClinica_id AND deptip.id = dep.dependenciasTipo_id  AND i.salidaDefinitiva = 'N' and tp.id = u.tipoDoc_id and diag.id = i.dxactual_id"
    detalle = "SELECT  tp.nombre tipoDoc,  u.documento documento, u.nombre  nombre , i.consec consec , fechaIngreso , fechaSalida, ser.nombre servicioNombreIng, dep.nombre camaNombreIng , diag.nombre dxActual FROM admisiones_ingresos i, usuarios_usuarios u, sitios_dependencias dep , clinico_servicios ser ,usuarios_tiposDocumento tp , sitios_dependenciastipo deptip  , clinico_Diagnosticos diag , sitios_serviciosSedes sd  WHERE sd.sedesClinica_id = i.sedesClinica_id  and   sd.servicios_id  = ser.id and   i.sedesClinica_id = dep.sedesClinica_id AND i.dependenciasActual_id = dep.id AND i.sedesClinica_id= '" + str(Sede) + "'  AND  deptip.id = dep.dependenciasTipo_id and dep.servicios_id = ser.id AND i.salidaDefinitiva = 'N' and tp.id = u.tipoDoc_id and u.id = i.documento_id and diag.id = i.dxactual_id"


    print(detalle)

    desdeTiempo = BusDesde[11:16]
    hastaTiempo = BusHasta[11:16]
    desdeFecha = BusDesde[0:10]
    hastaFecha = BusHasta[0:10]

    print ("desdeTiempo = ", desdeTiempo)
    print("desdeTiempo = " ,hastaTiempo)

    print (" desde fecha = " , desdeFecha)
    print("hasta "
          " = ", hastaFecha)


    if BusServicio != "":
      detalle = detalle + " AND  ser.id = '" + str(BusServicio) + "'"
    print(detalle)

    if BusDesde != "":
        detalle = detalle +  " AND i.fechaIngreso >= '" + str(desdeFecha) + " " + desdeTiempo + ":00'"
        print (detalle)

    if BusHasta != "":
        detalle = detalle + " AND i.fechaIngreso <=  '" + str(hastaFecha) + " " + hastaTiempo + ":00'"
        print(detalle)

    if BusHabitacion != "":
        detalle = detalle + " AND dep.id = '" + str(BusHabitacion) + "'"
        print(detalle)

    if BusTipoDoc != "":
            detalle = detalle + " AND i.tipoDoc_id= '" + str(BusTipoDoc) + "'"
            print(detalle)

    if BusDocumento != "":
                detalle = detalle + " AND u.documento= '" + str(BusDocumento) + "'"
                print(detalle)

    if BusPaciente != "":
        detalle = detalle + " AND u.nombre like '%" + str(BusPaciente) + "%'"
        print(detalle)

    if BusMedico != "":
        detalle = detalle + " AND i.medicoActual_id = '"  + str(BusMedico) + "'"
        print(detalle)


    if BusEspecialidad != "":
        detalle = detalle + " AND i.dxIngreso_id = '" + str(BusEspecialidad) + "'"
        print(detalle)




    cur1.execute(detalle)



    for tipoDoc, documento_id, nombre , consec, fechaIngreso,  fechaSalida, servicioNombreIng, camaNombreIng, dxActual  in cur1.fetchall():

        ingresos.append ({'tipoDoc' : tipoDoc, 'Documento': documento_id, 'Nombre': nombre , 'Consec': consec, 'FechaIngreso': fechaIngreso, 'FechaSalida': fechaSalida, 'servicioNombreIng': servicioNombreIng, 'camaNombreIng': camaNombreIng, 'DxActual': dxActual})

    miConexion1.close()
    print(ingresos)
    context['Ingresos'] = ingresos




    return render(request, "admisiones/panelHospAdmisionesBravo.html", context)

