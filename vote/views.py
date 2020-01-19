from .models import Candidat, HTMLTemplate, CandidatsNbVote, Etudiant

from rest_framework import viewsets
from vote.serializers import TestSerializer, VoteSerializer, UserSerializer

from rest_framework.permissions import IsAuthenticated


#####
#API#
#####

class TestViewSet(viewsets.ModelViewSet):
    queryset = Candidat.objects.all()
    serializer_class = TestSerializer
    permission_classes = (IsAuthenticated,)

class VoteViewSet(viewsets.ModelViewSet):
    queryset = CandidatsNbVote.objects.all()
    serializer_class = VoteSerializer
    permission_classes = (IsAuthenticated,)

class UserViewSet(viewsets.ModelViewSet):
    queryset = Etudiant.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Etudiant.objects.all()
        username = self.request.query_params.get('username', None)
        if username is not None:
            queryset = queryset.filter(username=username)
        return queryset