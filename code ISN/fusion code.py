#-*- coding: utf-8 -*-
# 'fetchall()' récupère toutes les données d'une colonne d'une table sqlite3
# 'fetchone()' récupère lignes par lignes les données d'une colonne d'une table sqlite3

import sqlite3
conn = sqlite3.connect('ta.db')
c = conn.cursor()
c.execute('''DROP TABLE IF EXISTS eleve_table;''')
c.execute('''CREATE TABLE eleve_table(
            id INTEGER PRIMARY KEY,
            pseudo TEXT,
            choix TEXT,                 
            choix2 TEXT,
            choix3 TEXT,
            choix4 TEXT,
            justice INTEGER,
            veto INTEGER);''')
# création d'une table de données sqlite3 avec paramètres

conn.commit()

# fonction insert de données dans la table. 
# Redondante mais pas le choix avec sqlite3 n'est-ce pas ? 
# dans le projet finale les inserts se font automatiquement avec la plateforme.
def donnees_entrer():
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('lazare', 'maths', 'philosophie', 'svt', 'histoire', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('thibault', 'svt', 'histoire', 'maths', 'philosophie', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('david', 'maths', 'histoire', 'svt', 'philosophie', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('léo', 'histoire', 'philosophie', 'svt', 'maths', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('elise', 'philosophie', 'histoire', 'svt', 'maths', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('alex', 'maths', 'philosophie', 'svt', 'histoire', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('titou', 'svt', 'philosophie', 'maths', 'histoire', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('jacob', 'maths', 'svt', 'histoire', 'philosophie', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('dalailama', 'histoire', 'philosophie', 'svt', 'maths', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('hugues', 'maths', 'svt', 'histoire', 'philosophie', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('lele', 'maths', 'philosophie', 'svt', 'histoire', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('ludo', 'svt', 'histoire', 'maths', 'philosophie', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('dada', 'maths', 'histoire', 'svt', 'philosophie', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('choucroute', 'histoire', 'philosophie', 'svt', 'maths', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('hamon', 'philosophie', 'histoire', 'svt', 'maths', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('violette', 'maths', 'philosophie', 'svt', 'histoire', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('lala', 'svt', 'philosophie', 'maths', 'histoire', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('hadrien', 'maths', 'svt', 'histoire', 'philosophie', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('bouda', 'histoire', 'philosophie', 'svt', 'maths', 0, 0)")
    c.execute("INSERT INTO eleve_table(pseudo, choix, choix2, choix3, choix4, justice, veto) VALUES('dubai', 'maths', 'svt', 'histoire', 'philosophie', 0, 0)")

    conn.commit()

nbeleves = 20 # nombre d'élèves totale
eleve1 = [0]*nbeleves # liste des élèves inscrit
from itertools import repeat
eleve2 = [[[]for j in repeat(None, 6)] for i in repeat(None, nbeleves)] 
# list of list pour (choix, choix2, choix3, choix4, justice, veto)


donnees_entrer()

# recupération des données de la table et insertion dans des listes python.
conn.row_factory = lambda cursor, row: row[0] # manip trouvé pour enlever les tuples
c = conn.cursor()
eleve1 = c.execute('SELECT pseudo FROM eleve_table').fetchall()

conn.row_factory = lambda cursor, row: row[0]
c = conn.cursor() 
c.execute("SELECT pseudo FROM eleve_table") 
for loop in range(nbeleves):
    eleve1[loop] = c.fetchone() # liste python crée avec des valeurs en tuples alors qu'on veut des chaines de caractères

c.execute("SELECT choix FROM eleve_table") 
for loop in range(nbeleves):
    eleve2[loop][0] = c.fetchone() # ""

c.execute("SELECT choix2 FROM eleve_table") 
for loop in range(nbeleves):
    eleve2[loop][1] = c.fetchone() # ""

c.execute("SELECT choix3 FROM eleve_table") 
for loop in range(nbeleves):
    eleve2[loop][2] = c.fetchone() # ""

c.execute("SELECT choix4 FROM eleve_table") 
for loop in range(nbeleves):
    eleve2[loop][3] = c.fetchone()  # ""    

c.execute("SELECT justice FROM eleve_table") 
for loop in range(nbeleves):
    eleve2[loop][4] = c.fetchone()  # ""     

c.execute("SELECT veto FROM eleve_table") 
for loop in range(nbeleves):
    eleve2[loop][5] = c.fetchone() # ""


maths = [0]*5
histoire = [0]*5
svt = [0]*5
philosophie = [0]*5  # initialisation de quelques variables
x = 0
y = 0
z = 0
t = 0
def a() :
    eleve2[loop][5] = eleve2[loop][5] - 2


c = conn.cursor() 
c.execute("SELECT choix FROM eleve_table") 
m = c.fetchall()

#choix 

for loop in range(nbeleves) :
    if m[loop] == 'maths' :
        maths[x] = eleve1[loop]
        x = x + 1
        eleve2[loop][5] = eleve2[loop][5] - 2
        if x == 5 :
            break

for loop in range(nbeleves) :
    if m[loop] == 'svt' :
        svt[y] = eleve1[loop]
        y = y + 1
        eleve2[loop][5] = eleve2[loop][5] - 2
        if y == 5 :
            break

for loop in range(nbeleves) :
    if m[loop] == 'histoire' :
        histoire[z] = eleve1[loop]
        z = z + 1
        eleve2[loop][5] = eleve2[loop][5] - 2
        if z == 5 :
            break


for loop in range(nbeleves) :
    if m[loop] == 'philosophie' :
        philosophie[t] = eleve1[loop]
        t = t + 1
        eleve2[loop][5] = eleve2[loop][5] - 2
        if t == 5 :
            break

eleve3 = nbeleves - (x + y + z + t)
# eleve3 est le nombre d'élève n'ayant pas eu leurs choix 1 (choix) par ordre chronologique


# choix2

c = conn.cursor() 
c.execute("SELECT choix2 FROM eleve_table") # récupéation des choix 2
m = c.fetchall() 

for loop in range(eleve3) :
    if a() :
        












conn.close()




# essai d'affection, algorythme pour les variable justice, les listes de TA, les veux des élèves

print(maths, svt, histoire, philosophie)


