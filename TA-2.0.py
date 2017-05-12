import pickle #importer la bibliothèque pickle
from operator import itemgetter #permet de trier une liste en fonction de critère : en fonction de la variable justice par exemple
from time import sleep #permet de ralentir l'execution d'une fonction (simple effet)

#exemple de ce que contient les principales listes utilisées :

#eleves = [["Thibault", "histoire", "français", "anglais", "maths", "123", 0, 0],["David", "français", "histoire", "anglais", "maths", "123", 0, 0], ["Lazare", "anglais", "maths", "français", "histoire", "123", 0, 0], ["Elise", "anglais", "maths", "français", "histoire", "123", 0, 0], ["Solena", "histoire", "français", "anglais", "maths", "123", 0, 0], ["Dana", "histoire", "français", "anglais", "maths", "123", 0, 0], ["Ines", "histoire", "français", "anglais", "maths", "123", 0, 0], ["Maxime", "histoire", "français", "anglais", "maths", "123", 0, 0], ["Quentin", "histoire", "français", "anglais", "maths", "123", 0, 0], ["Andrien", "histoire", "français", "anglais", "maths", "123", 0, 0], ["Raphael", "histoire", "français", "anglais", "maths", "123", 0, 0], ["Mathis", "histoire", "français", "anglais", "maths", "123", 0, 0], ["Pauline", "histoire", "français", "anglais", "maths", "123", 0, 0], ["Titouan", "histoire", "français", "anglais", "maths", "123", 0, 0], ["Nicolas", "histoire", "français", "anglais", "maths", "123", 0, 0], ["Vincent", "histoire", "français", "anglais", "maths", "123", 0, 0]]
#profs  = [["Léo", "123", "histoire"], ["Delphine", "123", "anglais"], ["Florence", "123", "maths"]]
#matiere = ["histoire", "maths", "anglais", "français"]


#On sort les données dans le fichier pickle (on pickel in)
pickle_in = open("list.pickle", "rb") 
eleves = pickle.load(pickle_in) #ouverture de la liste eleves
profs = pickle.load(pickle_in) #ouverture de la liste profs
matiere = pickle.load(pickle_in) #ouverture de la liste des matières


def menu1(eleves, matiere) : #on définis la fonction qui sera executer lorsque l'utilisateur est un élève
  testuser = 1# va nous servir a determiner si le nom d'utilisateur est bon 1 = echec / 0 = succès
  connexion = input("Entrer votre nom d'utilisateur: ") #entrer l'utilisateur

  for eleve in eleves : #Pour chaque élève dans la liste eleves
         if connexion == eleve[0]: #on regarde si le nom d'utilisateur correspond à un élève

                password = input("entrez votre mot de passe : ") #entrez le mot de passe

                testuser = 0 #la connexion est réuissi, on enrengistre dans une variable le succès

                if password == eleve[5]: #si le mot de passe correspond à l'élève

                       #rappel des matières proposées
                       print("")
                       print("matières :")
                       print("")
                       print("- ", matiere[0])
                       print("- ", matiere[1])
                       print("- ", matiere[2])
                       print("- ", matiere[3])
                       print("")

                       eleve[1] = input("entrez votre premier choix : ") #rentrer la matière correspondante au choix 1
                       choix1 = eleve[1] #on affecte la variable du choix1 dans le tableau
                       while eleve[1] != matiere[0] and eleve[1] != matiere[1] and eleve[1] != matiere[2] and eleve[1] != matiere[3] : #tant que la matière n'existe pas on redemande le choix
                         print("Matière innéxistante")
                         eleve[1] = input("entrez votre premier choix : ")
                         choix1 = eleve[1]

                       eleve[2] = input("entrez votre deuxième choix : ")#de même rentrer la matière correspondante au choix2
                       choix2 = eleve[2]
                       while eleve[2] != matiere[0] and eleve[2] != matiere[1] and eleve[2] != matiere[2] and eleve[2] != matiere[3] :
                         print("Matière innéxistante ")
                         eleve[2] = input("entrez votre deuxième choix : ")
                         choix2 = eleve[2]
                       while eleve[2] == choix1: #Tant que la matière rentrée a deja été rentrée on redemande le choix
                         print("matière déjà séléctionné")
                         eleve[2] = input("entrez votre deuxième choix : ")
                         choix2 = eleve[2]

                       eleve[3] = input("entrez votre troisième choix : ")#de même pour le choix 3
                       choix3 = eleve[3]
                       while eleve[3] != matiere[0] and eleve[3] != matiere[1] and eleve[3] != matiere[2] and eleve[3] != matiere[3] : #verifier qu'il n'y a pas d'erreur
                         print("Matière innéxistante")
                         eleve[3] = input("entrez votre troisième choix : ")
                         choix3 = eleve[3]
                       while eleve[3] == choix1 or eleve[3] == choix2: 
                         print("matière déjà séléctionné")
                         eleve[3] = input("entrez votre troisième choix : ")
                         choix3 = eleve[3]


                       eleve[4] = input("entrez votre quatrième choix : ") #de même pour le choix 4
                       while eleve[4] != matiere[0] and eleve[4] != matiere[1] and eleve[4] != matiere[2] and eleve[4] != matiere[3] : 
                         print("Matière innéxistante") #afficher 
                         eleve[4] = input("entrez votre quatrième choix : ")
                       while eleve[4] == choix1 or eleve[4] ==choix2 or eleve[4] == choix3:
                         print("matière déjà séléctionné")
                         eleve[4] = input("entrez votre quatrième choix : ")


                       print("choix bien pris en compte")

                else :

                       print("mot de passe éronné") #si password ne correspond pas à celui de la liste afficher

  if testuser == 1: #si la valeur de testuser est 1 le nom d'utilisateur n'existe pas
  	print("Nom d'utilisateur inconnue") 
  else:
  	testuser = 1 #remettre testuser=1 pour qu'on rentre de nouveau le nom

  return(eleves) # retourner les valeurs de la fonction

def menu2(profs, eleves) : #on définis la fonction à executer si l'utilisateur est un professeur
  testuser = 1 #va nous servir a determiner si le nom d'utilisateur est bon
  connexion = input("Entrez votre nom d'utilisateur: ") #entrer le nom du professeur

  for prof in profs : #pour chaque proffesseur dans la liste profs

     if connexion == prof[0]: #si le nom correspond à un nom de la liste
            password = input("entrez votre mot de passe : ") #on demande le mot de passe
            testuser = 0

            if password == prof[1]: #verifier le mot de passe

                   eleveVeto = input("Entrez le nom de élève à placer dans vore TA : ")

                   for eleve in eleves : #boucle pour le nombre d'eleve 

                          if eleveVeto == eleve[0]:  #si l'eleve à placer existe

                                 eleve[1] = prof[2] #l'eleve sera placé dans le TA du professeur (automatiquement dans sa matière)
                                 eleve[7] = 1 #on enregistre le fait que l'élève est prioritaire dans ce TA dans sa variable Veto en lui donnant la valeur 1

                                 print(eleve[0], "sera placé dans le TA", prof[2]) 
                                 
                          else :
                             print("Eleve inconnu")

            else:
                   print("mot de passe érroné")

     if testuser == 1 : #il y une erreur dans le nom d'utilisateur
       print("Nom d'utilisateur inconnue")
     else:
       testuser = 1
  return(eleves) #retourner les valeurs

def menu3(profs, eleves, matiere, SuperUser) : #on définit la fonction utilisée pour le superuser
   print("")
   connexion = input("entrez votre mot de passe : ")
   if connexion == SuperUser :#verifier si le mot de passe correspond
     print("")
     print("Menu")
     print("")
     print("1 -Lancer le programme-")    
     print("2 -Ajouter eleve-")
     print("3 -Ajouter professeur-")
     print("4 -Changer matière-")
     print("")

     menu = input("Choississez votre menu : ")#on demande le menu

     if menu == "1": #si on veux lancer le programme
       admin1(matiere, eleves)
     if menu == "2": #si on souhaite ajouter un utilisateur
       ajoutereleve(eleves)
     if menu == "3": # si on souhaite ajouter un professeur
       ajouterprof(profs)
     if menu == "4": #si on veux changer les matière à choisir
       admin3(matiere)
   else : #Si le mot de passe est faux
      print("")
      print("mot de passe erroné")

def admin1(matiere, eleves): # fonction de lancement du programme par l'Administrateur
     print("")
     print("running...")
     sleep(2) # ne sert pas vraiment mais ajoute un effet de temps d'attente (2 secondes) qui augmente l'éxperience
     #on tris par ordre croissant en fonction de la variable justice puis on met en premier les élèves dont la variable Veto est égale à 1 pour respecter l'ordre de priorité
     eleves.sort(key =itemgetter(6))
     eleves.sort(key=itemgetter(7), reverse=True) 

#remise à 0 des listes de TA, on donne 10 places par TA
     mat1 = [0]*10
     mat2 = [0]*10
     mat3 = [0]*10
     mat4 = [0]*10
     out = [0]*len(eleves)

#création d'une boucle itérative (iterateur : nombre d'élève (liste "eleves"))
     for loop in range(len(eleves)):
       m = 1 #compteur de tour qui demart à 1 pour pouvoire servir de compteur de choix (à la place 1,2,3 et 4 de la liste eleves)
       pull = 1 #permet de sortir de la boucle suivante

       while m <= 4 and pull == 1:
      
         if eleves[loop][m] == matiere[0] and mat1.count(0) > 0:
           for scoop in range(len(mat1)) :
             if mat1[scoop] == 0:
               mat1[scoop] = eleves[loop][0]
               pull = 0
               break

         elif eleves[loop][m] == matiere[1] and mat2.count(0) > 0:
           for scoop in range(len(mat2)):
             if mat2[scoop] == 0:
               mat2[scoop] = eleves[loop][0]
               pull = 0
               break

         elif eleves[loop][m] == matiere[2] and mat3.count(0) > 0:
           for scoop in range(len(mat3)):
             if mat3[scoop] == 0:
               mat3[scoop] = eleves[loop][0]
               pull = 0
               break

         elif eleves[loop][m] == matiere[3] and mat4.count(0) > 0 :
           for scoop in range(len(mat4)):
             if mat4[scoop] == 0:
               mat4[scoop] = eleves[loop][0]
               pull = 0
               break
         
         else :
           m = m + 1
           

       if m == 1 and eleves[loop][7] == 0 :     #on ajoute la justice correspondante au nombre de tour effectués
         eleves[loop][6] = eleves[loop][6] + 2

       if m == 2 and eleves[loop][7] == 0:
         eleves[loop][6] = eleves[loop][6] + 1

       if m == 3 and eleves[loop][7] == 0:
         eleves[loop][6] = eleves[loop][6] - 2

       if m == 4 and eleves[loop][7] == 0:
         eleves[loop][6] = eleves[loop][6] - 4
       
       if m == 5:
         for scoop in range(len(mat3)):
             if out[scoop] == 0:
               out[scoop] = eleves[loop][0]
               break
               
#affichage des listes de TA
     print("")
     print("done : ")
     print("")
     print(matiere[0], mat1)
     print("")
     print(matiere[1], mat2)
     print("")
     print(matiere[2], mat3)
     print("")
     print(matiere[3], mat4)
     print("")
     print("non inscrit : ", out)
     print("")

     for eleve in eleves: #on remet à 0 la variable Veto de tous les élèves
       eleve[7] = 0
     return(eleves, matiere)

def admin3(matiere): #fonction qui permet de remplacer le nom des matière 
#on demande les 4 matières une par une
      matiere[0] = input("entrez la première matière : ")
      matiere[1] = input("entrez la deuxième matière : ")
      matiere[2] = input("entrez la troisième matière : ")
      matiere[3] = input("entrez la quatrième matière : ")
      return(matiere) #retourner la liste matière afin qu'elle puisse être effective en dehors de la fonction

def ajoutereleve(eleves): #fonction d'ajout d'élèves dans la liste des eleves (accès admin)
  eleves.append([input("Entrez Pseudo : "), 0 ,0 ,0 ,0 ,input("Entrez mot de passe : "), 0, 1]) 
  #append = ajouter un élément à la fin de la liste "eleves"
  return(eleves)

def ajouterprof(profs): #idem pour les proffesseurs
  profs.append([input("Entrez Pseudo : "), input("Entrez mot de passe : "), input("Entrez matière : ")])
  return(profs)

#algorythme d'affichage du menu + déclenchement des fonctions associées
SuperUser = "123" # mot de passe admin (superuser)
i = 0 
menu = "0" #on donne une valeur par defaut à menu

#affichage du menu principal dans la commande
while  i==0:
   print("")
   print("Menus")
   print("")
   print("1 -Espace Eleve-")
   print("2 -Espace Proffesseur-")
   print("3 -Espace Admin-")
   print("0 -Quitter")
   print("")

   menu = input("Choississez votre menu : ")  
#déclenchement des fonctions associées
   if menu == "1":
     menu1(eleves, matiere)
   elif menu == "2":
     menu2(profs, eleves)
   elif menu == "3":
     menu3(profs, eleves, matiere, SuperUser)
   elif menu == "0":
     i = 1

#On rentre les données dans le fichier pickle (on pickel out)
pickle_out = open("list.pickle", "wb") #chemin d'accès au dossier
#enregistrement des listes dans le dossier
pickle.dump(eleves, pickle_out)
pickle.dump(profs, pickle_out)
pickle.dump(matiere, pickle_out)
pickle_out.close() #fermeture de l'accès


