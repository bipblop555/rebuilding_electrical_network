import infra, building

import pandas


network_df = pandas.read_csv("./reseau_en_arbre.csv").drop_duplicate()

def prepare_data(network_df):
	# construire un dictionnaire d'infra key : id_infra => value : infra_object
	# construire une liste de building
	# revoyer les 2 structures de données
	pass


def plannification(dict_infra, list_building):
	# roule l'algo décrit dans les slides.