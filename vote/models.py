from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.crypto import get_random_string

from django.dispatch import receiver
from django.db.models.signals import post_save
from .utils import classproperty
from django.core.cache import cache
from django.core.validators import validate_slug
from django_bleach.models import BleachField


class Section(models.Model):
	nom = models.CharField(max_length=50)

	def __str__(self):
		return self.nom

class Etudiant(AbstractUser): #CustomUser
	a_vote = models.BooleanField(default=False)
	date_vote = models.DateTimeField('date vote', default=None, blank=True, null=True)

def _get_file_path(instance, filename):
	return "{rand}_{filename}".format(rand=get_random_string(),
        filename=filename)

class Candidat(models.Model):
	nom = models.CharField(max_length=50)
	prenom = models.CharField(max_length=50)
	img = models.ImageField(upload_to=_get_file_path)
	description	= models.TextField(blank=True)
	section = models.CharField(max_length=30)

	def __str__(self):
		return (self.nom + ', '  + self.prenom)
	
class CandidatsNbVote(models.Model):
    candidat = models.OneToOneField(Candidat, related_name='vote', on_delete=models.PROTECT)
    nb_votes = models.PositiveIntegerField(default=0)

class HTMLTemplate(models.Model):
	key = models.CharField(primary_key=True, max_length=30)
	value = models.TextField(max_length=1000)
	description = models.CharField(max_length=300)

class Config(models.Model):
    """Table config, les entrées sont hard-codées.

    Supposée contenir qu'une seule entrée.

    """

    _active = models.BooleanField("Indique si les votes sont actifs", default=False)
    _start_date = models.DateTimeField("Date de début des votes", null=True, blank=True)
    _end_date = models.DateTimeField("Date de fin des votes", null=True, blank=True)

    def __str__(self):
        return "Configuration"

    @classproperty
    def active(cls):
        return cls.objects.first()._active

    @classproperty
    def start_date(cls):
        return cls.objects.first()._start_date

    @classproperty
    def end_date(cls):
        return cls.objects.first()._end_date