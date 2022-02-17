
class ArbreBinaire:
    """Définition de la classe arbre Binaire à partir du site de
    David Roche pixees.fr"""
    def __init__(self, valeur) -> None:
        self.valeur = valeur
        self.enfant_gauche = None
        self.enfant_droit = None
        
    def insert_gauche(self, valeur):
        """Ajoute une étiquette à l'enfant gauche"""
        if self.enfant_gauche == None:
            self.enfant_gauche = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
            new_node.enfant_gauche = self.enfant_gauche
            self.enfant_gauche = new_node
            
    def insert_droit(self, valeur):
        """Ajoute une étiquette à l'enfant droit"""
        if self.enfant_droit == None:
            self.enfant_droit = ArbreBinaire(valeur)
        else:
            new_node = ArbreBinaire(valeur)
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

    def hauteur(self):
        if racine is None :
            return -1
        if self.enfant_gauche is None and self.enfant_droit is None:


if __name__ == "__main__":
    racine = ArbreBinaire("A")
    racine.insert_gauche('B')
    racine.insert_droit("F")

    b_node = racine.get_gauche()
    b_node.insert_gauche('C')
    b_node.insert_droit('D')

    f_node = racine.get_droit()
    f_node.insert_gauche('G')
    f_node.insert_droit('H')

    c_node = b_node.get_gauche()
    c_node.insert_gauche('E')

    g_node = f_node.get_gauche()
    g_node.insert_gauche('I')
    
    h_node = f_node.get_droit()
    h_node.insert_gauche('J')

    print(racine)