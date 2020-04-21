from django.db import models

class Travel(models.Model):
    destination = models.CharField('Destination',max_length=50)
    reference = models.IntegerField('Référence', null=True, unique=True)
    description = models.TextField('Description',null=True)
    date_start = models.DateField('Date de départ',null=True)
    date_end = models.DateField('Date de retour',null=True)
    available = models.BooleanField('Disponible',default=True)
    nb_people = models.IntegerField('Nombre de personnes',null=True)
    price = models.IntegerField('Prix')
    picture = models.CharField(max_length=200)


    def __str__(self):
        return self.destination

    class Meta:
        verbose_name = "Voyage"
        verbose_name_plural = "Voyages"
    
class Contact(models.Model):
    name = models.CharField('Nom',max_length=20)
    email = models.EmailField('E-mail',max_length=200)
    message = models.TextField('Message', null=True)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

class Booking(models.Model):
    travel = models.OneToOneField(Travel, on_delete=models.CASCADE, verbose_name ="Destination")
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, verbose_name ="Contact")
    contacted = models.BooleanField('Demande traitée', default=False)


    def __str__(self):
        return self.contact.email


    class Meta:
        verbose_name = "Réservation"
        verbose_name_plural = "Réservations"




