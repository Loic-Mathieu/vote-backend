# mixins.py
from .models import Config
from django.shortcuts import redirect
from django.utils import timezone


class IsActiveMixin:
    """Vérifie qu'il est possible de voter.

    On peut voter si le vote est active, et que l'on est entre la date
    de début des votes et de fin.

    """

    def dispatch(self, request, *args, **kwargs):

        if (not Config.active
            or (Config.start_date and timezone.now() < Config.start_date)
            or (Config.end_date and Config.end_date < timezone.now())):

            return redirect('vote:status')

        return super().dispatch(request, *args, **kwargs)


class AlreadyVoteMixin:
    """Redirige vers la page status si un utilisateur a déjà voté."""

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.has_voted:
            return redirect('vote:status')
        return super().dispatch(request, *args, **kwargs)