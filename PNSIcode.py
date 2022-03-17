"""
Code principale qui regroupe les différents codes du projets 

"""

#Première partie des données servant pour l'arbre
dico[1] = {"Désirez-vous vous rendre sur les lieux du crime ? ","la mission continue","le chef de la police vous remplace sur cette mission et vous partez en vacances "}
dico[2] = {"Une fois sur les lieux du crime, souhaitez vous interroger Thomas l'ainé de la fraterie ?","Thomas vous révèle qu'au moment du crime il était avec Julie dans le salon en train de ranger des livres dans la bibliothèque","Vous pouvez interroger quelqu'un d'autre "}
dico[3] = {"Désirez vous interroger Julie pour confirmer les dires de Thomas ?","Julie vous confirme les faits","Vous pouvez interroger quelqu'un d'autre "}
dico[4] = {"Souhaitez vous interroger Julie ?","Julie vous révèle qu'au moment du crime elle était avec Thomas dans le salon en train de ranger des livres dans la bibliothèque","Vous pouvez interroger quelqu'un d'autre"}
dico[5] = {"Souhaitez vous inerroger Deniz ?","Deniz vous dévoile qu'il était seul dans sa chambre en train de réviser ses partiels","Vous pouvez interroger quelqu'un d'autre"}
dico[6] = {"Souhaitez vous interroger Deniz ?","Deniz vous dévoile qu'il était seul dans sa chambre en train de réviser ses partiels","Vous pouvez interroger quelqu'un d'autre"}
dico[7] = {"Souhaitez vous interroger Deniz ?","Deniz vous dévoile qu'il était seul dans sa chambre en train de réviser ses partiels","Vous pouvez interroger quelqu'un d'autre"}
dico[8] = {"Souhaitez vous interroger Deniz ?","Deniz vous dévoile qu'il était seul dans sa chambre en train de réviser ses partiels","Vous pouvez interroger quelqu'un d'autre"}
dico[9] = {"Souhaitez vous interroger Margaux ? ","Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire"}
dico[10] = {"Souhaitez vous interroger Margaux ? ","Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire"}
dico[11] = {"Souhaitez vous interroger Margaux ? ","Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire"}
dico[12] = {"Souhaitez vous interroger Margaux ? ","Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire"}
dico[13] = {"Souhaitez vous interroger Margaux ? ","Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire"}
dico[14] = {"Souhaitez vous interroger Margaux ? ","Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire"}
dico[15] = {"Souhaitez vous interroger Margaux ? ","Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire"}
dico[16] = {"Souhaitez vous interroger Margaux ? ","Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire"}

#Seconde partie des données servant pour l'arbre
dic[1] = {"Maintenant que vous avez fini d'inerroger tout le monde, souhaitez faire une inspection des chambres pour vérifier les alibis de chacun ?","Vous continuez votre enquête pour avoir plus de preuve","Vous arrêter l'enquête ici et vos éléments ne sont pas suffisants pour accuser quelqu'un, vous êtes donc licencié"}
dic[2] = {"Souhaitez vous inspecter la chambre de deniz ?","Vous découvrez que les livres et cahiers de deniz sont toujours ouverts et que l'encre est à peine cèche ce qui confirme l'alibi de deniz","Vous pouvez inspecter une autre pièce " }
dic[3] = {"Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ?","Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé","Vous pouvez inspecter une autre pièce"}
dic[4] = {"Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ?","Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé","Vous pouvez inspecter une autre pièce"}
dic[5] = {"Souhaitez vous vérifier si les livres dans la bibliothèque du salon", "Vous découvrez qu'il n'y a pas de livre dans cette bibliothèque mais des dessins d'Hervé", "Vous pouvez inspecter une autre pièce"}
dic[6] = {"Souhaitez vous vérifier si les livres dans la bibliothèque du salon", "Vous découvrez qu'il n'y a pas de livre dans cette bibliothèque mais des dessins d'Hervé", "Vous pouvez inspecter une autre pièce"}
dic[7] = {"Souhaitez vous vérifier si les livres dans la bibliothèque du salon", "Vous découvrez qu'il n'y a pas de livre dans cette bibliothèque mais des dessins d'Hervé", "Vous pouvez inspecter une autre pièce"}
dic[8] = {"Souhaitez vous vérifier si les livres dans la bibliothèque du salon", "Vous découvrez qu'il n'y a pas de livre dans cette bibliothèque mais des dessins d'Hervé", "Vous pouvez inspecter une autre pièce"} 
dic[9] = {"Souhaitez vous inspecter la chambre de Julie ?", "Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "C'est la fin de l'inspection des pièces, à l'aide des éléments que vous disposez il vous faut désignez un coupable "}
dic[10] = {"Souhaitez vous inspecter la chambre de Julie ?", "Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "C'est la fin de l'inspection des pièces, à l'aide des éléments que vous disposez il vous faut désignez un coupable "}
dic[11] = {"Souhaitez vous inspecter la chambre de Julie ?", "Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "C'est la fin de l'inspection des pièces, à l'aide des éléments que vous disposez il vous faut désignez un coupable "}
dic[12] = {"Souhaitez vous inspecter la chambre de Julie ?", "Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "C'est la fin de l'inspection des pièces, à l'aide des éléments que vous disposez il vous faut désignez un coupable "}
dic[13] = {"Souhaitez vous inspecter la chambre de Julie ?", "Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "C'est la fin de l'inspection des pièces, à l'aide des éléments que vous disposez il vous faut désignez un coupable "}
dic[14] = {"Souhaitez vous inspecter la chambre de Julie ?", "Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "C'est la fin de l'inspection des pièces, à l'aide des éléments que vous disposez il vous faut désignez un coupable "}
dic[15] = {"Souhaitez vous inspecter la chambre de Julie ?", "Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "C'est la fin de l'inspection des pièces, à l'aide des éléments que vous disposez il vous faut désignez un coupable "}
dic[16] = {"Souhaitez vous inspecter la chambre de Julie ?", "Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "C'est la fin de l'inspection des pièces, à l'aide des éléments que vous disposez il vous faut désignez un coupable "}


#Class pour créer l'arbre qui servira à faire les suites de questions
class CreationArbre:
    """Définition de la classe arbre Binaire à partir du site de
    David Roche pixees.fr"""
    def __init__(self, valeur) -> None:
        self.valeur = valeur
        self.enfant_gauche = None
        self.enfant_droit = None
        
    def insert_gauche(self, valeur):
        """Ajoute une étiquette à l'enfant gauche"""
        if self.enfant_gauche == None:
            self.enfant_gauche = CreationArbre(valeur)
        else:
            new_node = CreationArbre(valeur)
            new_node.enfant_gauche = self.enfant_gauche
            self.enfant_gauche = new_node
            
    def insert_droit(self, valeur):
        """Ajoute une étiquette à l'enfant droit"""
        if self.enfant_droit == None:
            self.enfant_droit = CreationArbre(valeur)
        else:
            new_node = CreationArbre(valeur)
            new_node.enfant_droit = self.enfant_droit
            self.enfant_droit = new_node
    
    def get_valeur(self):
        """Renvoie l'étiquette de la racine"""
        return self.valeur

    def get_gauche(self):
        """Renvoie l'étiquette de l'enfant gauche
        """
        return self.enfant_gauche
    
    def get_droit(self):
        """Renvoie l'étiquette de l'enfant droit"""
        return self.enfant_droit
    
    def __str__(self) -> str:
        return f'({self.valeur}, {self.enfant_gauche}, {self.enfant_droit})'

if __name__ == "__main__":
    
#Racine de l'arbre, création des 2 premières branches
    racine = CreationArbre(dico[0])
    racine.insert_gauche(dico[1])
    racine.insert_droit(dico[2])
    
    
#Premier niveau de noeuds, alpha 
    alpha_node = racine.get_gauche()
    alpha_node.insert_gauche(dico[3])
    alpha_node.insert_droit(dico[4])
    
    
#Deuxième niveau de noeuds, beta / gamma
    beta_node = alpha_node.get_gauche()
    beta_node.insert_gauche(dico[5])
    beta_node.insert_droit(dico[6])

    gamma_node = alpha_node.get_droit()
    gamma_node.insert_gauche(dico[7])
    gamma_node.insert_droit(dico[8])

    
#Troisième niveau de noeuds, delta ; epsilon / zeta ; eta
    delta_node = beta_node.get_gauche()
    delta_node.insert_gauche(dico[9])
    delta_node.insert_droit(dico[10])
    
    epsilon_node = beta_node.get_droit()
    epsilon_node.insert_gauche(dico[11])
    epsilon_node.insert_droit(dico[12])
    
    zeta_node = gamma_node.get_gauche()
    zeta_node.insert_gauche(dico[13])
    zeta_node.insert_droit(dico[14])
    
    eta_node = gamma_node.get_droit()
    eta_node.insert_gauche(dico[15])
    eta_node.insert_droit(dico[16])
    
    print(racine)



#Création du second arbre, soit le second chapitre 
#Racine de l'arbre, création des 2 premières branches
    racinebis = CreationArbre(dic[0])
    racinebis.insert_gauche(dic[1])
    racinebis.insert_droit(dic[2])
    
    
#Premier niveau de noeuds, alpha 
    ah_node = racinebis.get_gauche()
    ah_node.insert_gauche(dic[3])
    ah_node.insert_droit(dic[4])
    
    
#Deuxième niveau de noeuds, beta / gamma
    bay_node = ah_node.get_gauche()
    bay_node.insert_gauche(dic[5])
    bay_node.insert_droit(dic[6])

    tsay_node = ah_node.get_droit()
    tsay_node.insert_gauche(dic[7])
    tsay_node.insert_droit(dic[8])

    
#Troisième niveau de noeuds, delta ; epsilon / zeta ; eta
    day_node = bay_node.get_gauche()
    day_node.insert_gauche(dic[9])
    day_node.insert_droit(dic[10])
    
    ay_node = bay_node.get_droit()
    ay_node.insert_gauche(dic[11])
    ay_node.insert_droit(dic[12])
    
    eff_node = tsay_node.get_gauche()
    eff_node.insert_gauche(dic[13])
    eff_node.insert_droit(dic[14])
    
    gay_node = tsay_node.get_droit()
    gay_node.insert_gauche(dic[15])
    gay_node.insert_droit(dic[16])
    
    
    print(racinebis)
