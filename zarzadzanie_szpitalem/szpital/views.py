from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from .models import Doktor, Pacjent, Spotkanie

# Create your views here.
def Onas(request):
    return render(request, 'onas.html')

def StronaGlowna(request):
    return render(request, 'stronaglowna.html')

def Kontakt(request):
    return render(request, 'kontakt.html')

def Index(request):
    if not request.user.is_staff:
        return redirect('login')
    doctors = Doktor.objects.all()
    patients = Pacjent.objects.all()
    appointments = Spotkanie.objects.all()
    d = 0
    p = 0
    a = 0
    for i in doctors:
        d+=1
    for i in patients:
        p+=1
    for i in appointments:
        a+=1
    d1 = {'d':d, 'p':p, 'a':a}
    return render(request, 'index.html', d1)

def Login(request):
    error = ""
    if request.method == "POST":
        u = request.POST['uname']
        p = request.POST['pwd']
        user = authenticate(username=u, password=p)
        try:
            if user.is_staff:
                login(request, user)
                error="Nie"

            else:
                error="Tak"
        except:
            error="Tak"
    d={'error': error}
    return render(request,'login.html', d)

def Logout_admin(request):
    if not request.user.is_staff:
        return redirect('login')
    logout(request)
    return redirect('admin_login')

def View_Doctor(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Doktor.objects.all()
    d = {'doc':doc}
    return render(request, 'view_doctor.html', d)

def Delete_Doctor(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    doctor = Doktor.objects.get(id=pid)
    doctor.delete()
    return redirect('view_doctor')
    
def Add_Doctor(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == "POST":
        n = request.POST['imie']
        t = request.POST['telefon']
        sp = request.POST['specjalnosc']
        try:
            Doktor.objects.create(imie=n, telefon=t, specjalnosc=sp)
            error = 'Nie'

        except:
            error = 'Tak'
    d = {'error':error}
    return render(request,'add_doctor.html', d)
    
def View_Patient(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Pacjent.objects.all()
    d = {'doc':doc}
    return render(request, 'view_patient.html', d)

def Delete_Patient(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    patient = Pacjent.objects.get(id=pid)
    patient.delete()
    return redirect('view_patient')

def Add_Patient(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')

    if request.method == "POST":
        n = request.POST['imie']
        p = request.POST['plec']
        t = request.POST['telefon']
        a = request.POST['adres']
        try:
            Pacjent.objects.create(imie=n, plec=p, telefon=t, adres=a)
            error = 'Nie'

        except:
            error = 'Tak'
    d = {'error':error}
    return render(request,'add_patient.html', d)

def Add_Appointment(request):
    error = ""
    if not request.user.is_staff:
        return redirect('login')
    doctor1 = Doktor.objects.all()
    patient1 = Pacjent.objects.all()

    if request.method == "POST":
        d = request.POST['doktor']
        p = request.POST['pacjent']
        da = request.POST['data']
        cz = request.POST['czas']
        doktor = Doktor.objects.filter(imie=d).first()
        pacjent = Pacjent.objects.filter(imie=p).first()
        try:
            Spotkanie.objects.create(doktor=doktor,pacjent=pacjent,data=da,czas=cz)
            error = 'Nie'

        except:
            error = 'Tak'
    d = {'doktor': doctor1, 'pacjent': patient1, 'error': error}
    return render(request,'add_appointment.html', d)

def View_Appointment(request):
    if not request.user.is_staff:
        return redirect('login')
    doc = Spotkanie.objects.all()
    d = {'doc':doc}
    return render(request, 'view_appointment.html', d)

def Delete_Appointment(request,pid):
    if not request.user.is_staff:
        return redirect('login')
    app = Spotkanie.objects.get(id=pid)
    app.delete()
    return redirect('view_appointment')