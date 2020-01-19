# accounts/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import BaseFormSet, formset_factory
from .models import Etudiant, Candidat

class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Etudiant
        fields = ('username', 'a_vote', 'date_vote')

class MyUserChangeForm(UserChangeForm):

    class Meta(UserChangeForm):
        model = Etudiant
        fields = ('username', 'a_vote', 'date_vote')

class LoginForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	
	class Meta():
		model = Etudiant
		fields = ('username', 'password')
			

class CandidatForm(forms.Form):
    """Formulaire récoltant le choix des votes.

    L'utilisateur peut faire deux choix, mais au moins un.

    """

    candidat = forms.IntegerField(min_value=0)

    def clean_candidat(self):
        candidat = self.cleaned_data['candidat']

        if not Candidat.objects.filter(pk=candidat).exists():
            raise forms.ValidationError("Le candidat choisi n'existe pas")
        return candidat

    def save(self):
        instance = Candidat.objects.get(pk=candidat)
        instance.nbvotes += 1
        instance.save()


class BaseCandidatFormSet(BaseFormSet):
    validate_max = validate_min = True
    min_num = 1
    max_num = 2


CandidatFormSet = formset_factory(CandidatForm, formset=BaseCandidatFormSet)