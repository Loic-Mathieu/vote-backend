from django.contrib import admin

from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import MyUserCreationForm, MyUserChangeForm
from .models import Etudiant, Section, Candidat, CandidatsNbVote, HTMLTemplate, Config

class MyUserAdmin(UserAdmin):
    add_form = MyUserCreationForm
    form = MyUserChangeForm
    model = Etudiant
    list_display = ['username', 'a_vote', 'date_vote']
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('a_vote', 'date_vote')}),
    ) #this will allow to change these fields in admin module


admin.site.register(Etudiant, MyUserAdmin)
admin.site.register(Section)
admin.site.register(Candidat)
admin.site.register(CandidatsNbVote)
admin.site.register(HTMLTemplate)
admin.site.register(Config)