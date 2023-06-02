from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from .views import View_Appointment,View_Doctor,View_Patient,Add_Doctor,Add_Appointment,Add_Patient
from .models import Doktor
class FilmyTests(TestCase):


    def setUp(self):
        User.objects.create_superuser(username='admin', password='admin')

# Testowanie urls
    def test_urls_add_doctor(self):
        url = reverse('add_doctor/')
        self.assertEquals(resolve(url).func,Add_Doctor)

    def test_urls_add_patient(self):
        url = reverse('add_patient/')
        self.assertEquals(resolve(url).func, Add_Patient)

    def test_urls_add_appointment(self):
        url = reverse('add_appointment/')
        self.assertEquals(resolve(url).func, Add_Appointment)

    def test_urls_view_doctor(self):
        url = reverse('view_doctor/')
        self.assertEquals(resolve(url).func, View_Doctor)

    def test_urls_view_patient(self):
        url = reverse('view_patient/')
        self.assertEquals(resolve(url).func, View_Patient)

    def test_urls_view_appointment(self):
        url = reverse('view_appointment/')
        self.assertEquals(resolve(url).func, View_Appointment)

# Testowanie models
    def test_models_doctor_jako_text(self):
        doktor = Doktor.objects.create(telefon="424152421")
        self.assertEquals(str(doktor), doktor.telefon+' ('+str(doktor.telefon)+')')

    def test_models_add_doctor_nie_jest_pusty(self):
        doktor = Doktor.objects.create(imie="Janek")
        self.assertNotEquals(doktor,None)

    def test_models_doctor_jest_unikalny(self):
        doktor1 = Doktor.objects.create(imie="Maja")
        with self.assertRaises(Exception):
            doktor2 = Doktor.objects.create(imie="Maja")

    def test_models_add_doctor_jest_tylko_1(self):
        Doktor.objects.create(imie="Damian",telefon="424321324")
        self.assertEquals(Doktor.objects.all().count(),1)

