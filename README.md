# Projet-n-3-NSI

Projet scolaire de Terminale en lien avec la matière Numérique et Science de l'Informatique.


Contexte : 
Le joueur est un enquêteur et dois résoudre une affaire criminel. L'histoire se déroule à Puteaux dans la richissime demeure des Mercury. Hervé, le doyen de la famille et propriétaire d'une grande entreprise d'huile d'olive basée à Cassis, est retrouvé inanimé dans baignoire. C'est Margaux, l'infirmière qui était à sa charge qui a découvert le corps à environ 19h30 en l'appelant pour diner. Hervé a 3 enfants, une fille Julie et deux fils, Thomas et Deniz. Toute la famille était réuni pour la semaine de Noël. 

Première partie : l'interrogatoire 

Question 1 : Désirez-vous vous rendre sur les lieux du crime ? 
oui --> la mission continue 
non --> le chef de la police vous remplace sur cette mission et vous partez en vacances 

Question 2 : Une fois sur les lieux du crime, souhaitez vous interroger Thomas l'ainé de la fraterie ? 
Oui --> Thomas vous révèle qu'au moment du crime il était avec Julie dans le salon en train de ranger des livres dans la bibliothèque
Non --> Vous pouvez interroger quelqu'un d'autre 

Question 3A(découle du oui à la Q2) : Désirez vous interroger Julie pour confirmer les dires de Thomas ?
Oui --> Julie vous confirme les faits 
Non --> Vous pouvez interroger quelqu'un d'autre 

Question 3B(découle du non à la Q2) : Souhaitez vous interroger Julie ?
Oui --> Julie vous révèle qu'au moment du crime elle était avec Thomas dans le salon en train de ranger des livres dans la bibliothèque
Non --> Vous pouvez interroger quelqu'un d'autre

Question 4A(découle du oui à la Q3A) : Souhaitez vous inerroger Deniz ?
Oui --> Deniz vous dévoile qu'il était seul dans sa chambre en train de réviser ses partiels 
Non --> Vous pouvez interroger quelqu'un d'autre (il ne reste que Margaux)

Question 4B(découle du non à la Q3A) : Souhaitez vous interroger Deniz ? 
Oui --> Deniz vous dévoile qu'il était seul dans sa chambre en train de réviser ses partiels 
Non --> Vous pouvez interroger quelqu'un d'autre (il ne reste que Margaux)

Question 4C(découle du oui à la Q3B) : Souhaitez vous interroger Deniz ?
Oui --> Deniz vous dévoile qu'il était seul dans sa chambre en train de réviser ses partiels 
Non --> Vous pouvez interroger quelqu'un d'autre (il ne reste que Margaux)

Question 4D(découle du non à la Q3B): Souhaitez vous interroger Deniz ?
Oui --> Deniz vous dévoile qu'il était seul dans sa chambre en train de réviser ses partiels 
Non --> Vous pouvez interroger quelqu'un d'autre (il ne reste que Margaux)

Question 5A(découle de oui à la Q4A): Souhaitez vous interroger Margaux ? 
Oui --> Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau
Non --> Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire 

Question 5C(découle de non à la Q4A): Souhaitez vous interroger Margaux ? 
Oui --> Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau
Non --> Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire 

Question 5C(découle de oui à la Q4B): Souhaitez vous interroger Margaux ? 
Oui --> Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau
Non --> Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire

Question 5D(découle de non à la Q4A): Souhaitez vous interroger Margaux ? 
Oui --> Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau
Non --> Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire 

Question 5E(découle de oui à la Q4C): Souhaitez vous interroger Margaux ? 
Oui --> Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau
Non --> Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire 

Question 5F(découle de non à la Q4C): Souhaitez vous interroger Margaux ? 
Oui --> Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau
Non --> Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire 

Question 5G(découle de oui à la Q4D): Souhaitez vous interroger Margaux ? 
Oui --> Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau
Non --> Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire 

Question 5H(découle de non à la Q4D): Souhaitez vous interroger Margaux ? 
Oui --> Margaux vous explique qu'après avoir préparer la piqure habituelle d'Hervé, elle découvre son corps inanimé dans la baignoire avec un liquide violet mélangé à l'eau
Non --> Vous n'avez plus personne à interroger c'est la fin de l'interrogatoire 

Fin de la première étape



Deuxième partie : inspection des pièces

Question 1 : Maintenant que vous avez fini d'inerroger tout le monde, souhaitez faire une inspection des chambres pour vérifier les alibis de chacun ?
Oui --> Vous continuez votre enquête pour avoir plus de preuve
Non --> Vous arrêter l'enquête ici et vos éléments ne sont pas suffisants pour accuser quelqu'un, vous êtes donc licencié

Question 2(découle de oui à la Q1): Souhaitez vous inspecter la chambre de deniz ? 
Oui --> Vous découvrez que les livres et cahiers de deniz sont toujours ouverts et que l'encre est à peine cèche ce qui confirme l'alibi de deniz
Non --> Vous pouvez inspecter une autre pièce 

Question 3A(découle de oui à la Q2): Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ? 
Oui --> Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé
Non --> Vous pouvez inspecter une autre pièce 

Question 3A(découle de oui à la Q2): Souhaitez vous inspecter l'infirmerie où Margaux prépare ses piqures ? 
Oui --> Vous découvrez que l'infirmerie était en ordre pour pouvoir faire la piqure et vous déduisez que de toute façon, Margaux n'ayant pas de part dans l'héritage, elle n'aurait pas de mobile de tuer Hervé
Non --> Vous pouvez inspecter une autre pièce







Dictionnaire :

Première Partie :

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
