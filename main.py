from ast import Global
from tkinter import *

#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
dico = {}
dico[1] = {"question" :"Une fois sur les lieux du crime, souhaitez vous interroger Thomas l'ainé de la fraterie ?","reponseA" :"Thomas vous révèle qu'au moment du crime il était avec Julie dans le salon en train de ranger des livres dans la bibliothèque","reponseB" : "Vous pouvez interroger quelqu'un d'autre "}

dico[2] = {"question" :"Désirez vous interroger Julie pour confirmer les dires de Thomas ?","reponseA" :"Julie vous confirme les faits","reponseB" :"Vous pouvez faire autre chose"}
dico[3] = {"question" :"Souhaitez vous inerroger Deniz ?","reponseA" :"Deniz vous dévoile qu'il était seul dans sa chambre en train de réviser ses partiels","reponseB" :"Vous pouvez faire autre chose"}

dico[4] = {"question" :"Souhaitez vous vérifier si les livres dans la bibliothèque du salon sont bien rangés ?", "reponseA" :"Vous découvrez qu'il n'y a pas de livre dans cette bibliothèque mais des dessins d'Hervé", "reponseB" :"Vous pouvez faire autre chose"}
dico[5] = {"question" :"Souhaitez vous inerroger Deniz ?","reponseA" :"Deniz vous dévoile qu'il était seul dans sa chambre en train de réviser ses partiels","reponseB" :"Vous pouvez faire autre chose"}
dico[6] = {"question" :"Souhaitez vous inspecter la chambre de deniz ?","reponseA" :"Vous découvrez que les livres et cahiers de deniz sont toujours ouverts et que l'encre est à peine sèche ce qui confirme l'alibi de deniz","reponseB" :"Vous pouvez faire autre chose" }
dico[7] = {"question" :"Souhaitez vous interroger Margaux ? ","reponseA" :"Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","reponseB" :"Vous pouvez faire autre chose"}

dico[8] = {"question" :"Souhaitez vous inspecter la chambre de Julie ?", "reponseA" :"Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "reponseB" :"Vous pouvez faire autre chose"}
dico[9] = {"question" :"Souhaitez vous interroger Margaux ? ","reponseA" :"Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","reponseB" :"Vous pouvez faire autre chose"}
dico[10] = {"question" :"Souhaitez vous inspecter la chambre de deniz ?","reponseA" :"Vous découvrez que les livres et cahiers de deniz sont toujours ouverts et que l'encre est à peine sèche ce qui confirme l'alibi de deniz","reponseB" :"Vous pouvez faire autre chose" }
dico[11] = {"question" :"Souhaitez vous interroger Margaux ? ","reponseA" :"Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","reponseB" :"Vous pouvez faire autre chose"}
dico[12] = {"question" :"Souhaitez vous interroger Margaux ? ","reponseA" :"Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","reponseB" :"Vous pouvez faire autre chose"}
dico[13] = {"question" :"Souhaitez vous interroger Julie ?","reponseA" :"Julie vous révèle qu'au moment du crime elle était avec Thomas dans le salon en train de ranger des livres dans la bibliothèque","reponseB" :"Vous pouvez faire autre chose"}
dico[14] = {"question" :"Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ?","reponseA" :"Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé","reponseB" :"Vous pouvez faire autre chose"}
dico[15] = {"question" :"Souhaitez vous interroger Julie ?","reponseA" :"Julie vous révèle qu'au moment du crime elle était avec Thomas dans le salon en train de ranger des livres dans la bibliothèque","reponseB" :"Vous pouvez faire autre chose"}

dico[16] = {"question" :"Souhaitez vous inerroger Deniz ?","reponseA" :"Deniz vous dévoile qu'il était seul dans sa chambre en train de réviser ses partiels","reponseB" :"Vous pouvez faire autre chose"}
dico[17] = {"question" :"Souhaitez vous interroger Margaux ? ","reponseA" :"Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","reponseB" :"Vous pouvez faire autre chose"}
dico[18] = {"question" :"Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ?","reponseA" :"Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé","reponseB" :"Vous pouvez faire autre chose"}
dico[19] = {"question" :"C'est la fin de l'enquête"}
dico[20] = {"question" :"Souhaitez vous interroger Margaux ? ","reponseA" :"Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","reponseB" :"Vous pouvez faire autre chose"}
dico[21] = {"question" :"Souhaitez vous interroger Margaux ? ","reponseA" :"Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","reponseB" :"Vous pouvez faire autre chose"}
dico[22] = {"question" :"Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ?","reponseA" :"Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé","reponseB" :"Vous pouvez faire autre chose"}
dico[23] = {"question" :"C'est la fin de l'enquête"}
dico[24] = {"question" :"Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ?","reponseA" :"Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé","reponseB" :"Vous pouvez faire autre chose"}
dico[25] = {"question" :"Souhaitez vous interroger Julie ?","reponseA" :"Julie vous révèle qu'au moment du crime elle était avec Thomas dans le salon en train de ranger des livres dans la bibliothèque","reponseB" :"Vous pouvez faire autre chose"}
dico[26] = {"question" :"Souhaitez vous vérifier si les livres dans la bibliothèque du salon sont bien rangés ?", "reponseA" :"Vous découvrez qu'il n'y a pas de livre dans cette bibliothèque mais des dessins d'Hervé", "reponseB" :"Vous pouvez faire autre chose"}
dico[27] = {"question" :"Souhaitez vous interroger Margaux ? ","reponseA" :"Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","reponseB" :"Vous pouvez faire autre chose"}
dico[28] = {"question" :"Souhaitez vous interroger Julie ?","reponseA" :"Julie vous révèle qu'au moment du crime elle était avec Thomas dans le salon en train de ranger des livres dans la bibliothèque","reponseB" :"Vous pouvez faire autre chose"}
dico[29] = {"question" :"Souhaitez vous interroger Julie ?","reponseA" :"Julie vous révèle qu'au moment du crime elle était avec Thomas dans le salon en train de ranger des livres dans la bibliothèque","reponseB" :"Vous pouvez faire autre chose"}
dico[30] = {"question" :"Souhaitez vous vérifier si les livres dans la bibliothèque du salon sont bien rangés ?", "reponseA" :"Vous découvrez qu'il n'y a pas de livre dans cette bibliothèque mais des dessins d'Hervé","reponseB" : "Vous pouvez faire autre chose"}
dico[31] = {"question" :"C'est la fin de l'enquête"}

dico[32] = {"question" :"Souhaitez vous inspecter la chambre de deniz ?","reponseA" :"Vous découvrez que les livres et cahiers de deniz sont toujours ouverts et que l'encre est à peine sèche ce qui confirme l'alibi de deniz","reponseB" :"Vous pouvez faire autre chose" }
dico[33] = {"question" :"C'est la fin de l'enquête"}
dico[34] = {"question" :"Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ?","reponseA" :"Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé","reponseB" :"Vous pouvez faire autre chose"}
dico[35] = {"question" :"C'est la fin de l'enquête"}
dico[36] = {"question" :"Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ?","reponseA" :"Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé","reponseB" :"Vous pouvez faire autre chose"}
dico[37] = {"question" :"C'est la fin de l'enquête"}
dico[38] = {"question" :"Souhaitez vous interroger Julie ?","reponseA" :"Julie vous révèle qu'au moment du crime elle était avec Thomas dans le salon en train de ranger des livres dans la bibliothèque","reponseB" :"Vous pouvez faire autre chose"}
dico[39] = {"question" :"Souhaitez vous interroger Julie ?","reponseA" :"Julie vous révèle qu'au moment du crime elle était avec Thomas dans le salon en train de ranger des livres dans la bibliothèque","reponseB" :"Vous pouvez faire autre chose"}
dico[40] = {"question" :"Souhaitez vous vérifier si les livres dans la bibliothèque du salon sont bien rangés ?", "reponseA" :"Vous découvrez qu'il n'y a pas de livre dans cette bibliothèque mais des dessins d'Hervé", "reponseB" :"Vous pouvez faire autre chose"}
dico[41] = {"question" :"C'est la fin de l'enquête"}
dico[42] = {"question" :"Souhaitez vous inspecter la chambre de Julie ?", "reponseA" :"Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "reponseB" :"Vous pouvez faire autre chose"}
dico[43] = {"question" :"Souhaitez vous interroger Margaux ? ","reponseA" :"Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","reponseB" :"Vous pouvez faire autre chose"}
dico[44] = {"question" :"Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ?","reponseA" :"Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé","reponseB" :"Vous pouvez faire autre chose"}
dico[45] = {"question" :"C'est la fin de l'enquête"}
dico[46] = {"question" :"Souhaitez vous vérifier si les livres dans la bibliothèque du salon sont bien rangés ?","reponseA" : "Vous découvrez qu'il n'y a pas de livre dans cette bibliothèque mais des dessins d'Hervé", "reponseB" :"Vous pouvez faire autre chose"}
dico[47] = {"question" :"C'est la fin de l'enquête"}
dico[48] = {"question" :"Souhaitez vous vérifier si les livres dans la bibliothèque du salon sont bien rangés ?","reponseA" : "Vous découvrez qu'il n'y a pas de livre dans cette bibliothèque mais des dessins d'Hervé", "reponseB" :"Vous pouvez faire autre chose"}
dico[49] = {"question" :"C'est la fin de l'enquête"}
dico[50] = {"question" :"Souhaitez vous inspecter la chambre de Julie ?","reponseA" : "Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "reponseB" :"Vous pouvez faire autre chose"}
dico[51] = {"question" :"C'est la fin de l'enquête"}

dico[52] = {"question" :"Souhaitez vous vérifier si les livres dans la bibliothèque du salon sont bien rangés ?","reponseA" : "Vous découvrez qu'il n'y a pas de livre dans cette bibliothèque mais des dessins d'Hervé", "reponseB" :"Vous pouvez faire autre chose"}
dico[53] = {"question" :"C'est la fin de l'enquête"}
dico[54] = {"question" :"Souhaitez vous vérifier si les livres dans la bibliothèque du salon sont bien rangés ?", "reponseA" :"Vous découvrez qu'il n'y a pas de livre dans cette bibliothèque mais des dessins d'Hervé", "reponseB" :"Vous pouvez faire autre chose"}
dico[55] = {"question" :"C'est la fin de l'enquête"}
dico[56] = {"question" :"Souhaitez vous inspecter la chambre de Julie ?", "reponseA" :"Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "reponseB" :"Vous pouvez faire autre chose"}
dico[57] = {"question" :"C'est la fin de l'enquête"}
dico[58] = {"question" :"Souhaitez vous interroger Margaux ? ","reponseA" :"Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","reponseB" :"Vous pouvez faire autre chose"}
dico[59] = {"question" :"Souhaitez vous interroger Margaux ? ","reponseA" :"Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau","reponseB" :"Vous pouvez faire autre chose"}
dico[60] = {"question" :"Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ?","reponseA" :"Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé","reponseB" :"Vous pouvez faire autre chose"}
dico[61] = {"question" :"C'est la fin de l'enquête"}
dico[62] = {"question" :"Souhaitez vous inspecter la chambre de Julie ?", "reponseA" :"Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "reponseB" :"Vous pouvez faire autre chose"}
dico[63] = {"question" :"C'est la fin de l'enquête"}
dico[64] = {"question" :"Souhaitez vous inspecter la chambre de Julie ?", "reponseA" :"Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau","reponseB" : "Vous pouvez faire autre chose"}
dico[65] = {"question" :"C'est la fin de l'enquête"}

dico[66] = {"question" :"Souhaitez vous inspecter la chambre de Julie ?", "reponseA" :"Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "reponseB" :"Vous pouvez faire autre chose"}
dico[67] = {"question" :"C'est la fin de l'enquête"}
dico[68] = {"question" :"Souhaitez vous inspecter la chambre de Julie ?", "reponseA" :"Vous découvrez que dans le fond d'un tirroir une substance dont le labo vous confirme sa dangerosité si elle est diluée dans l'eau", "reponseB" :"Vous pouvez faire autre chose"}
dico[69] = {"question" :"C'est la fin de l'enquête"}
dico[70] = {"question" :"Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ?","reponseA" :"Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé","reponseB" :"Vous pouvez faire autre chose"}
dico[71] = {"question" :"C'est la fin de l'enquête"}
dico[72] = {"question" :"Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ?","reponseA" :"Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé","reponseB" :"Vous pouvez faire autre chose"}
dico[73] = {"question" :"C'est la fin de l'enquête"}

#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################

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
    
#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################


#Racine de l'arbre, création des 2 premières branches
racine = CreationArbre(dico[1])
racine.insert_gauche(dico[2])
racine.insert_droit(dico[3])


#Premier niveau de noeuds, alpha 
alpha_node = racine.get_gauche()
alpha_node.insert_gauche(dico[4])
alpha_node.insert_droit(dico[5])


#Deuxième niveau de noeuds, beta / gamma
beta_node = alpha_node.get_gauche()
beta_node.insert_gauche(dico[6])
beta_node.insert_droit(dico[7])

gamma_node = alpha_node.get_droit()
gamma_node.insert_gauche(dico[8])
gamma_node.insert_droit(dico[9])


#Troisième niveau de noeuds, delta ; epsilon / zeta ; eta
delta_node = beta_node.get_gauche()
delta_node.insert_gauche(dico[10])
delta_node.insert_droit(dico[11])

epsilon_node = beta_node.get_droit()
epsilon_node.insert_gauche(dico[12])
epsilon_node.insert_droit(dico[13])

zeta_node = gamma_node.get_gauche()
zeta_node.insert_gauche(dico[14])
zeta_node.insert_droit(dico[15])

eta_node = gamma_node.get_droit()
eta_node.insert_gauche(dico[16])
eta_node.insert_droit(dico[17])


#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################


fenetre = Tk()
fenetre.geometry("1400x1000")
fenetre.bind('<Escape>', lambda e: fenetre.destroy())
# On affiche l'image du fond du jeu

fenetre.title("image en fond")
img_fond = PhotoImage(file = "C:\\Users\\Thomas\\Documents\\Mon_image.png")
img_label = Label(image = img_fond)
img_label.pack()

def game_over():
    fenetre.destroy()
    
question = StringVar()
situation1 = StringVar()
situation2 = StringVar()

def texte(dico):
    question = ""
    situation1 = ""
    situation2 = ""
    compteur = 0
    question = dico["question"]
    situation1 = dico["reponseA"]
    situation2 = dico["reponseB"]
    return question,situation1,situation2
            
question_bis,situation1_bis,situation2_bis = texte(dico[1])
question.set(question_bis)
situation1.set(situation1_bis)
situation2.set(situation2_bis)


def Button1():
    global racine
    if racine.get_gauche() != None :
        racine = racine.get_gauche()
        question_bis,situation1_bis,situation2_bis = texte(racine.get_valeur())
        question.set(question_bis)
        situation1.set(situation1_bis)
        situation2.set(situation2_bis)
    else :
        game_over()
def Button2():
    global racine
    if racine.get_droit() != None :
        racine = racine.get_droit()
        question_bis,situation1_bis,situation2_bis = texte(racine.get_valeur())
        question.set(question_bis)
        situation1.set(situation1_bis)
        situation2.set(situation2_bis)
    else :
        game_over()


#################################################################################################################################################################
#################################################################################################################################################################
#################################################################################################################################################################
    
# frame 0
Frame0 = Frame(fenetre,borderwidth=2, relief=GROOVE)
Frame0.pack(side=BOTTOM, padx=50, pady=50)

Label(Frame0,textvariable=question).pack(side = TOP, padx=10, pady=10)
label = Label()
label.pack()

# frame 1
Frame1 = Frame(Frame0, borderwidth=2, relief=GROOVE)
Frame1.pack(side=LEFT, padx=50, pady=10)

# frame 2
Frame2 = Frame(Frame0, borderwidth=2, relief=GROOVE)
Frame2.pack(side=RIGHT, padx=50, pady=10)

bouton1 = Button(Frame1, command = Button1, text="situation1")
bouton2 = Button(Frame2, command = Button2, text="situation2")
bouton1.pack()
bouton2.pack()

# Ajout de labels
Label(Frame1, textvariable=situation1).pack(padx=10, pady=10)
Label(Frame2, textvariable=situation2).pack(padx=10, pady=10)
label.pack()

fenetre.mainloop()

from tkinter.messagebox import *# boîte de dialogue
from tkinter.filedialog import *

def Verification():
    if tueur.get() == 'Thomas' or tueur.get() == 'thomas':
        showinfo('Résultat','Tu as gagné')
        Mafenetre.destroy()
    else:
        showinfo('Résultat','tu as perdu')
        Mafenetre.destroy()

# Création de la fenêtre principale (main window)
Mafenetre = Tk()
Mafenetre.title('Identification requise')

# Création d'un widget Label (texte 'Mot de passe')
Label1 = Label(Mafenetre, text = 'Qui est le tueur ?')
Label1.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Entry (champ de saisie)
tueur= StringVar()
Champ = Entry(Mafenetre, textvariable= tueur, bg ='bisque', fg='maroon')
Champ.focus_set()
Champ.pack(side = LEFT, padx = 5, pady = 5)

# Création d'un widget Button (bouton Valider)
Bouton = Button(Mafenetre, text ='Valider', command = Verification)
Bouton.pack(side = LEFT, padx = 5, pady = 5)

Mafenetre.mainloop()
