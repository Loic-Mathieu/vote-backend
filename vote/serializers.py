from rest_framework import serializers
from vote.models import Candidat, CandidatsNbVote, Etudiant

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


"""
{
    "nb_votes": 5
    "candidat": 3
}
"""