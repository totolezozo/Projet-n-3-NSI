
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
    
    
#Premier niveau de noeuds, alpha 
    alpha_node = racine.get_gauche()
    alpha_node.insert_gauche(dico[2])
    alpha_node.insert_droit(dico[3])
    
    
#Deuxième niveau de noeuds, beta / gamma
    beta_node = alpha_node.get_gauche()
    beta_node.insert_gauche(dico[4])
    beta_node.insert_droit(dico[5])

    gamma_node = alpha_node.get_droit()
    gamma_node.insert_gauche(dico[6])
    gamma_node.insert_droit(dico[7])

    
#Troisième niveau de noeuds, delta ; epsilon / zeta ; eta
    delta_node = beta_node.get_gauche()
    delta_node.insert_gauche(dico[8])
    delta_node.insert_droit(dico[9])
    
    epsilon_node = beta_node.get_droit()
    epsilon_node.insert_gauche(dico[10])
    epsilon_node.insert_droit(dico[11])
    
    zeta_node = gamma_node.get_gauche()
    zeta_node.insert_gauche(dico[12])
    zeta_node.insert_droit(dico[13])
    
    eta_node = gamma_node.get_droit()
    eta_node.insert_gauche(dico[14])
    eta_node.insert_droit(dico[15])
    
#Quatrième niveau
    theta_node = delta_node.get_gauche()
    theta_node.insert_gauche(dico[16])
    theta_node.insert_droit(dico[17])
    
    iota_node = delta_node.get_droit()
    iota_node.insert_gauche(dico[18])
    iota_node.insert_droit(dico[19])
    
    kappa_node = epsilon_node.get_gauche()
    kappa_node.insert_gauche(dico[20])
    kappa_node.insert_droit(dico[21])
    
    lambda_node = epsilon_node.get_droit()
    lambda_node.insert_gauche(dico[22])
    lambda_node.insert_droit(dico[23])
    
    mu_node = zeta_node.get_gauche()
    mu_node.insert_gauche(dico[24])
    mu_node.insert_droit(dico[25])
    
    nu_node = zeta_node.get_droit()
    nu_node.insert_gauche(dico[26])
    nu_node.insert_droit(dico[27])  
    
    xi_node = eta_node.get_gauche()
    xi_node.insert_gauche(dico[28])
    xi_node.insert_droit(dico[29])
    
    omicron_node = eta_node.get_droit()
    omicron_node.insert_gauche(dico[30])
    omicron_node.insert_droit(dico[31])
    
#Cinquième niveau
    pi_node = theta_node.get_gauche()
    pi_node.insert_gauche(dico[32])
    pi_node.insert_droit(dico[33])
    
    rho_node = kappa_node.get_gauche()
    rho_node.insert_gauche(dico[34])
    rho_node.insert_droit(dico[35])
    
    sigma_node = kappa_node.get_droit()
    sigma_node.insert_gauche(dico[36])
    sigma_node.insert_droit(dico[37])
    
    tau_node = mu_node.get_gauche()
    tau_node.insert_gauche(dico[38])
    tau_node.insert_droit(dico[39])
    
    upsilon_node = mu_node.get_droit()
    upsilon_node.insert_gauche(dico[40])
    upsilon_node.insert_droit(dico[41])
    
    phi_node = nu_node.get_gauche()
    phi_node.insert_gauche(dico[42])
    phi_node.insert_droit(dico[43])
    
    chi_node = nu_node.get_droit()
    chi_node.insert_gauche(dico[44])
    chi_node.insert_droit(dico[45])
    
    psi_node = xi_node.get_gauche()
    psi_node.insert_gauche(dico[46])
    psi_node.insert_droit(dico[47])
    
    omega_node = xi_node.get_droit()
    omega_node.insert_gauche(dico[48])
    omega_node.insert_droit(dico[49])
    
    ah_node = omicron_node.get_gauche()
    ah_node.insert_gauche(dico[50])
    ah_node.insert_droit(dico[51])
    
#Sixième niveau
    bay_node = tau_node.get_gauche()
    bay_node.insert_gauche(dico[52])
    bay_node.insert_droit(dico[53])
    
    tsay_node = tau_node.get_droit()
    tsay_node.insert_gauche(dico[54])
    tsay_node.insert_droit(dico[55])
    
    day_node = upsilon_node.get_gauche()
    day_node.insert_gauche(dico[56])
    day_node.insert_droit(dico[57])
    
    ay_node = phi_node.get_gauche()
    ay_node.insert_gauche(dico[58])
    ay_node.insert_droit(dico[59])
    
    eff_node = phi_node.get_droit()
    eff_node.insert_gauche(dico[60])
    eff_node.insert_droit(dico[61])
    
    gay_node = psi_node.get_gauche()
    gay_node.insert_gauche(dico[62])
    gay_node.insert_droit(dico[63])
    
    ha_node = psi_node.get_droit()
    ha_node.insert_gauche(dico[64])
    ha_node.insert_droit(dico[65])
    
#Septième niveau   
    ee_node = bay_node.get_gauche
    ee_node.insert_gauche(dico[66])
    ee_node.insert_droit(dico[67])
    
    yacht_node = tsay_node.get_gauche
    yacht_node.insert_gauche(dico[68])
    yacht_node.insert_droit(dico[69])
    
    car_node = ay_node.get_gauche()
    car_node.insert_gauche(dico[70])
    car_node.insert_droit(dico[71])
    
    ell_node = ay_node.get_droit()
    ell_node.insert_gauche(dico[72])
    ell_node.insert_droit(dico[73])
    
        
    print(racine)
