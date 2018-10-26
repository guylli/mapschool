from django.contrib import admin
from . import models
from django.conf import settings

# Register your models here.

#Cette classe me permet de definir l'affichge de mes donnees dans la partie admin
# list_display permet de choisir les elementrs que je souhaite dans ma liste
#list_filter me permet d'assig,er des filtres
#search_fields me permettra dans le champ de recherche d'effectuer une recherche sur les elements choisis
#fieldsets permettra d'inserer les champs du formiulaire de creation ou de modification

class EtablissementAdmin(admin.ModelAdmin):
	list_display = ('nom','ville', 'quartier', 'repere', 'telephone','email', 'adresse','longitude', 'latitude')
	list_filter = ('nom','ville', 'quartier', 'repere', 'telephone','email', 'adresse','longitude', 'latitude')
	search_fields = ('nom','ville', 'quartier')

	fieldsets = (
			(None, {
				'fields': ('nom','ville', 'quartier', 'repere', 'telephone', 
					'email', 'adresse','longitude', 'latitude')
				}),
			)
	

admin.site.register(models.Etablissement, EtablissementAdmin)


