#!/usr/bin/env python3

from flask import Flask, request, redirect, render_template, session
import sqlite3

app = Flask(__name__, static_folder="public", static_url_path="")
app.secret_key = b'best_project'

conn = sqlite3.connect('best_project.db', check_same_thread=False) #pabien
c = conn.cursor()
# pas de date de naissance dans la base de donnée
c.execute(""" 
    CREATE TABLE IF NOT EXISTS User (
        idUser INTEGER PRIMARY KEY AUTOINCREMENT, 
        User_name VARCHAR(45) NOT NULL, 
        User_surname VARCHAR(45) NOT NULL, 
        User_pseudo VARCHAR(45) NOT NULL, 
        User_password VARCHAR(20) NOT NULL, 
        User_email VARCHAR(20) NULL, 
        User_phone VARCHAR(20) NULL)
    """)

#    CREATE TABLE IF NOT EXISTS `best_project`.`Location` (
#        `idLocation` INT NOT NULL AUTO_INCREMENT,
#        `city` VARCHAR(45) NOT NULL,
#        `adress` VARCHAR(45) NOT NULL,
#        `idUser` INT NOT NULL,
#        PRIMARY KEY (`idLocation`, `idUser`),
#        INDEX `idUser_idx` (`idUser` ASC) VISIBLE,
#        CONSTRAINT `idUser`
#            FOREIGN KEY (`idUser`)
#            REFERENCES `best_project`.`User` (`idUser`)
#    )
            
#    CREATE TABLE IF NOT EXISTS `best_project`.`Cours` (
#        `idCours` INT NOT NULL AUTO_INCREMENT,
#        `IndiceCours` VARCHAR(2) NOT NULL,
#        PRIMARY KEY (`idCours`),
#        INDEX () VISIBLE,
#        UNIQUE INDEX `idCours_UNIQUE` (`idCours` ASC) VISIBLE
#    )



@app.route("/")
def home():
    return redirect('/page_accueil.html')

@app.route("/login", methods=["POST"])
def login():
    if 'connexion_ok' in session:
        return redirect('/mon_profil.html')
    else:
        c.execute("""SELECT User_pseudo, User_password FROM User""")
        pseudo =request.form["pseudo"]
        mdp = request.form["mdp"]
        print("test")
        for row in c:
            if row[0] == pseudo:
                if row[1] == mdp:
                    session['connexion_ok'] = True
                    print("vous etes connecté")
                    return redirect('/')
                else:
                    print("mdp incorrect")
                    return redirect('/login.html')
            else:
                print("pseudo incorrect")
                return redirect('/login.html')

@app.route("/mon_profil")
def mon_profil_co():
    if 'connexion_ok' in session:
        return redirect('/mon_profil.html')

    else:
        return redirect('/connexion.html')

@app.route("/recherche_cours")
def recherche_cours_co():
    if 'connexion_ok' in session:
        return redirect('/TrouverUnCours.html')

    else:
        return redirect('/connexion.html')

@app.route("/inscription", methods=["POST"])
def inscription():
    prenom = request.form["prenom"]
    nom = request.form["nom"]
    tel = request.form["tel"]
    pseudo = request.form["pseudo"]
    mdp = request.form["mdp"]
    email = request.form["email"]
    date = request.form["date"]

    c.execute("INSERT INTO User (User_name, User_surname, User_pseudo, User_password, User_email, User_phone) VALUES (?, ?, ?, ?, ?, ?)", (nom, prenom, pseudo, mdp, email, tel))
    conn.commit()

    print("Vous etes {} {} (alias {}), votre mot de passe est {}, votre mail est {} et votre numéro de téléphone est {}".format(prenom, nom, pseudo, mdp, email, tel))
    return redirect('/page_acceuil.html')
    

app.run()