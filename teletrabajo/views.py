#from django.http import HttpResponse 1era opción
#from django.shortcuts import render # 2da opción

#def hello_world(request):
    #return HttpResponse("Hola Mundo") 1era opción
    #return render(request, 'HOME.html') # 2da opción

from django.shortcuts import render, redirect
from django.contrib.auth import logout as do_logout
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth.forms import UserCreationForm

def welcome(request):
    #Si estamos identificados devolvemos a la portada
    if request.user.is_authenticated:
        #return render(request, "welcome.html")
        return render(request, "welcome.html")
    return redirect('/login')

def register(request):
    #Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    #Añadimos los datos recibidos al formulario
    form = UserCreationForm(data=request.POST)
    #Si el formulario es válido.
    if form.is_valid():
        #Creamos la nueva cuenta de usuario
        user = form.save()
        #Si el usuario se crea correctamente
        if user is not None:
            #Hacemos el llogin manualmente
            do_login(request,user)
            #Y le redireccionamos a la portada
            return redirect('/')
        #Si queremos borramos los campos de ayuda
    form.fields['username'].help_text = None
    form.fields['password1'].help_text = None
    form.fields['password2'].help_text = None
    #Si llegamos al final renderizamos el formulario
    return render(request, "register.html", {'form':form})

def login(request):
    #Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        #Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        #Si el formulario es válido.
        if form.is_valid():
            #Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)
            #Si existe un usuario con ese nombre y contraseña
            if user is not None:
                #Hacemos el login manualmente
                do_login(request, user)
                #Y le redireccionamos a la portada
                return redirect('tareas/tareas_lista')
    #Si llegamos al final renderizamos el formulario
    return render(request, "login.html", {'form': form})

def logout(request):
    #Finalizamos la sesión
    do_logout(request)
    #Redireccionamos a la portada
    return redirect('/')
