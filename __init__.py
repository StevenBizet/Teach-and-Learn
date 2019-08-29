#!/usr/bin/env python3

"""Mon docstring"""
import sqlite3
from flask import Flask, request, redirect, render_template, session, flash, url_for

CONN = sqlite3.connect('best_project.db', check_same_thread=False) #pabien
C = CONN.cursor()
# pas de date de naissance dans la base de donnée
C.execute("""
    CREATE TABLE IF NOT EXISTS User (
        idUser INTEGER PRIMARY KEY AUTOINCREMENT, 
        User_name VARCHAR(20) NOT NULL, 
        User_surname VARCHAR(20) NOT NULL, 
        User_pseudo VARCHAR(20) NOT NULL, 
        User_password VARCHAR(20) NOT NULL, 
        User_email VARCHAR(20) NOT NULL, 
        User_phone VARCHAR(20) NOT NULL,
        Maths INTEGER DEFAULT '0',
        Francais INTEGER DEFAULT '0',
        Histoire INTEGER DEFAULT '0',
        Chimie INTEGER DEFAULT '0')
    """)

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


def create_app():
    """ On créer notre fonction pour l'appeler dans server.py"""
    app = Flask(__name__, static_folder="public", static_url_path="")
    app.secret_key = b'best_project'


    @app.route("/")
    def home():
        return redirect('/page_accueil.html')

    @app.route("/login")
    def login():
        if 'connexion_ok' in session:
            session.pop("connexion_ok", None)
            flash("Vous êtes déconecté")
            return redirect('/')
        else:
            return redirect('/connexion.html')

    @app.route("/verif_co", methods=["POST"])
    def verif_co():
        C.execute("""SELECT idUser, User_pseudo, User_password FROM User""")
        pseudo = request.form["pseudo"]
        mdp = request.form["mdp"]
        print("test")
        for row in C:
            if row[1] == pseudo:
                if row[2] == mdp:
                    id_user = row[0]
                    session['connexion_ok'] = id_user
                    print("vous etes connecté")  #faire un pop up avec "vous etes connecté"
                    print(id_user)
                    return redirect('/')
                else:
                    print("mdp incorrect")
                    return redirect('/connexion.html')
            else:
                print("pseudo incorrect")
                return redirect('/connexion.html')

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
#        date = request.form["date"]
        math = request.form["niveau_maths"]
        francais = request.form["niveau_francais"]
        histoire = request.form["niveau_histoire"]
        chimie = request.form["niveau_chimie"]

        C.execute("INSERT INTO User \
                (User_name, User_surname, User_pseudo, User_password, User_email, User_phone, Maths, \
                Francais, Histoire, Chimie) \
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", \
                (nom, prenom, pseudo, mdp, email, tel, math, francais, histoire, chimie))
        CONN.commit()

        flash("Vous etes {} {} (alias {}), votre mot de passe est {}, \
                votre mail est {} et votre numéro de téléphone est {}"\
                .format(prenom, nom, pseudo, mdp, email, tel))
        return redirect('/page_accueil.html')

    return app

#app.run('127.0.0.1')
