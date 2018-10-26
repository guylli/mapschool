# Ici je prepare mes modeles a etre serializer ou formater en json

from rest_framework.serializers import ModelSerialzer
from .models import Etablissement

class EtablissementSerializer(ModelSerialzer):

	class Meta:
		model = Etablissement
		fields = ['nom','ville', 'quartier', 'repere', 'telephone','email', 'adresse','longitude', 'latitude']