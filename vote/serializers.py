from rest_framework import serializers
from vote.models import Candidat, CandidatsNbVote, Etudiant
from vote import models

class TestSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Candidat
		fields = ['id', 'nom', 'prenom', 'description', 'section', 'img']

class VoteSerializer(serializers.HyperlinkedModelSerializer):
	candidat = serializers.PrimaryKeyRelatedField(queryset=Candidat.objects.all())

	class Meta:
		model = CandidatsNbVote
		fields = ['id', 'nb_votes', 'candidat']

class UserSerializer(serializers.HyperlinkedModelSerializer):
	groups = serializers.StringRelatedField(many=True)

	class Meta:
		model = Etudiant
		fields = ['id', 'username', 'groups', 'a_vote']

class ConfigSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = models.Config
		fields = ['_active', '_start_date', '_end_date']

"""
{
    "nb_votes": 5
    "candidat": 3
}
"""