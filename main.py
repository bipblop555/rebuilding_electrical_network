import infra, building

import pandas


network_df = pandas.read_csv("./reseau_en_arbre.csv").drop_duplicates()

def prepare_data(network_df):
	# éliminer les buildings qui n'ont pas été touchés
	# construire un dictionnaire d'infra key : infra_id => value : infra_object
	# construire une liste de building
	# renvoyer les 2 structures de données
	network_df = network_df[network_df["infra_type"] != "infra_intacte"]

	infra_subdfs = network_df.groupby(by="infra_id")
	dict_infras = {}
	for infra_id, infra_subdf in infra_subdfs:
		length = infra_subdf["longueur"].iloc[0]
		infra_type = infra_subdf["infra_type"].iloc[0]
		nb_houses = sum(infra_subdf["nb_maisons"].values)
		dict_infras[infra_id] = infra.Infra(infra_id, length, infra_type, nb_houses)

	building_subdfs = network_df.groupby(by= "id_batiment")
	list_buildings = []
	for building_id, building_subdf in building_subdfs:
		list_infras = [dict_infras[infra_id] for infra_id in building_subdf["infra_id"].values]
		list_buildings.append(building.Building(id_building, list_infra))

	return dict_infras, list_building



def plannification(dict_infra, list_building):
	# roule l'algo décrit dans les slides.
	pass


if __name__ == "__main__":
	prepare_data(network_df)
	# plannification(dict_infra, list_building)