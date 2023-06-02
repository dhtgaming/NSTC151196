from django.db import models

# Create your models here.
class Doktor(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50)
    telefon = models.IntegerField()
    specjalnosc = models.CharField(max_length=50)

    def __str__(self):
        return self.imie

class Pacjent(models.Model):
    id = models.AutoField(primary_key=True)
    imie = models.CharField(max_length=50)
    plec = models.CharField(max_length=10)
    telefon = models.IntegerField(null=True)
    adres = models.TextField()

    def __str__(self):
        return self.imie

class Spotkanie(models.Model):
    id = models.AutoField(primary_key=True)
    doktor = models.ForeignKey(Doktor, on_delete=models.CASCADE)
    pacjent = models.ForeignKey(Pacjent, on_delete=models.CASCADE)
    data = models.DateField()
    czas = models.TimeField()

    def __str__(self):
        return self.doktor.imie + "__" +self.pacjent.imie