
#Class pour créer l'arbre qui servira à faire les suites de questions
class CréationArbre:
    """Définition de la classe arbre Binaire à partir du site de
    David Roche pixees.fr"""
    def __init__(self, valeur) -> None:
        self.valeur = valeur
        self.enfant_gauche = None
        self.enfant_droit = None
        
    def insert_gauche(self, valeur):
        """Ajoute une étiquette à l'enfant gauche"""
        if self.enfant_gauche == None:
            self.enfant_gauche = CréationArbre(valeur)
        else:
            new_node = CréationArbre(valeur)
            new_node.enfant_gauche = self.enfant_gauche
            self.enfant_gauche = new_node
            
    def insert_droit(self, valeur):
        """Ajoute une étiquette à l'enfant droit"""
        if self.enfant_droit == None:
            self.enfant_droit = CréationArbre(valeur)
        else:
            new_node = CréationArbre(valeur)
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
    racine = CréationArbre(dico[0])
    racine.insert_gauche(dico[1])
    racine.insert_droit(dico[2])
    
    alpha_node = racine.get_gauche()
    alpha_node.insert_gauche(dico[3])
    alpha_node.insert_droit(dico[4])

    beta_node = racine.get_droit()
    beta_node.insert_gauche(dico[5])
    beta_node.insert_droit(dico[6])

    gamma_node = alpha_node.get_gauche()
    gamma_node.insert_gauche(dico[7])
    gamma_node.insert_droit(dico[8])

    delta_node = alpha_node.get_droit()
    delta_node.insert_gauche(dico[9])
    delta_node.insert_droit(dico[10])
    
    epsilon_node = beta_node.get_gauche()
    epsilon_node.insert_gauche(dico[11])
    epsilon_node.insert_droit(dico[12])
    
    zeta_node = beta_node.get_droit()
    zeta_node.insert_gauche(dico[13])
    zeta_node.insert_droit(dico[14])

    print(racine)
