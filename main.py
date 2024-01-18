import infra, building

import pandas


network_df = pandas.read_csv("./reseau_en_arbre.csv").drop_duplicates()

def prepare_data(network_df):
	# éliminer les buildings qui n'ont pas été touchés
	# construire un dictionnaire d'infra key : infra_id => value : infra_object
	# construire une liste de building
	# revoyer les 2 structures de données
	network_df = network_df[network_df["infra_type"] != "infra_intacte"]

	infra_subdfs = network_df.groupby(by="infra_id")
	dict_infras = {}
	for infra_id, infra_subdf in infra_subdfs:

		length = 
		infra_type = 
		nb_houses = 

		dict_infras[infra_id] = infra.Infra(length, infra_type, nb_houses)


def plannification(dict_infra, list_building):
	# roule l'algo décrit dans les slides.
	pass


if __name__ == "__main__":
	prepare_data(network_df)
	# plannification(dict_infra, list_building)