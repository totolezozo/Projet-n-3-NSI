
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

