

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
    
    
#Premier niveau de noeuds, alpha / beta
    alpha_node = racine.get_gauche()
    alpha_node.insert_gauche(dico[3])
    alpha_node.insert_droit(dico[4])

    beta_node = racine.get_droit()
    beta_node.insert_gauche(dico[5])
    beta_node.insert_droit(dico[6])


#Deuxième niveau de noeuds, gamma ; delta / epsilon ; zeta
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
    
    
#Troisième niveau de noeuds, eta ; theta / iota ; kappa / lambda ; mu /
    eta_node = gamma_node.get_gauche()
    eta_node.insert_gauche(dico[15])
    eta_node.insert_droit(dico[16])
    
    theta_node = gamma_node.get_droit()
    theta_node.insert_gauche(dico[17])
    theta_node.insert_droit(dico[18])
    
    iota_node = delta_node.get_gauche()
    iota_node.insert_gauche(dico[19])
    iota_node.insert_droit(dico[20])
    
    kappa_node = delta_node.get_droit()
    kappa_node.insert_gauche(dico[21])
    kappa_node.insert_droit(dico[22])
    
    lambda_node = epsilon_node.get_gauche()
    lambda_node.insert_gauche(dico[23])
    lambda_node.insert_droit(dico[24])
    
    mu_node = epsilon_node.get_droit()
    mu_node.insert_gauche(dico[25])
    mu_node.insert_droit(dico[26])
    
    nu_node = zeta_node.get_gauche()
    nu_node.insert_gauche(dico[27])
    nu_node.insert_droit(dico[28])
    
    xi_node = zeta_node.get_droit()
    xi_node.insert_gauche(dico[29])
    xi_node.insert_droit(dico[30])
    
    
    print(racine)
