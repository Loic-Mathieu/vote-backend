from .models import Candidat, HTMLTemplate, CandidatsNbVote, Etudiant, Config

from rest_framework import viewsets
from vote.serializers import TestSerializer, VoteSerializer, UserSerializer

from rest_framework.permissions import IsAuthenticated
from vote import serializers


#####
#API#
#####

#Candidats
class TestViewSet(viewsets.ModelViewSet):
    queryset = Candidat.objects.all()
    serializer_class = TestSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'head', 'patch', 'options']
    ordering_fields = ['nom']


# Votes
class VoteViewSet(viewsets.ModelViewSet):
    queryset = CandidatsNbVote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'head', 'patch', 'options']

class ResultatsViewSet(viewsets.ModelViewSet):
    queryset = CandidatsNbVote.objects.all()
    serializer_class = serializers.ResultatsSerializer
    http_method_names = ['get', 'head', 'options']
    ordering_fields = ['nb_votes']
    # permission_classes = (IsAuthenticated,)


# Etudiants
class UserViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'head', 'patch', 'options']

    def get_queryset(self):
        queryset = Etudiant.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset


# Dates
class ConfigViewSet(viewsets.ModelViewSet):
    queryset = Config.objects.all()
    serializer_class = serializers.ConfigSerializer
    # permission_classes = (IsAuthenticated,)
    http_method_names = ['get', 'head', 'put', 'options']