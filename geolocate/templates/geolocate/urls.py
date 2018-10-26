app_name = 'geolocate'

urlpatterns = [

	# charegement des urls du suet d'administration depuis mon appli geolocate
	url(r'^admin', admin.site.urls),

	#Les routes de mon APi
	#Pour mieux comprendren la syntaxe des urls, il faut savoir que la partie de gauche
	# affichera l'url que l'utilisateur verra sur son navigateur.
	# La partie du milieu indique la vue de  traitement correspondant dans le fichier views.py
	# La parite de droite s'il y'en a indique juste le nom que l'on choisit de donner à notre url
	# afin que l'on puisse pouvoir pointer dessus comme avec un lien
	#Exemple: <a href="{% url 'geolocate:admin' %}"> Aller à la page d'admin</a>

	url(r'^api/liste/etablissement/$', views.EtablissementList.as_view()),
	#?Ppk>\d+) cette expression reguliere permet d'afficher l'identifiant correspondant
	# Exemple: /api/ets/1/ ou api/ets/101
	# La route suivante affichera les detailsd'un ets

	url(r'^api/etablissement/(?P<pk>\d+)/$', views.EtablissementDetailList.as_view()),

	# Les routes de mon site
	url(r'^etablissement_list/$', views.EtablissementListView.as_view(),
		name= 'etablissement_list'),
	url(r'^etablissement_detail/(?P<pk>\d+)/$', views.EtablissementDetailView.as_view(),
		name='etablissement-detail'), 
	]