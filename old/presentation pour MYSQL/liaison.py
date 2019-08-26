from flask import Flask, render_template, request
from flask_mysqldb import MySQL

import os
import mysql.connector

#mysql = MySQL()
app = Flask(__name__)


cnx = mysql.connector.connect(user = 'root', password = 'root', host='127.0.0.1', database = 'best_project') 
cursor = cnx.cursor()

app._static_folder = os.path.abspath("templates/static/")


@app.route('/')
def formulaire():
    return render_template('formulaire_V0.html')

@app.route('/valide', methods=['GET', 'POST'])
def formulaire_V0():
    if request.method == "POST":
        details = request.form
        User_name = details['prenom']
        User_surname = details['nom']
        User_pseudo = details['pseudo']
        User_password = details['mdp']
        User_email = details['email']
        User_phone = details['tel']
        cursor.execute("INSERT INTO User(User_name, User_surname, User_pseudo, User_password, User_email, User_phone) VALUES (%s, %s, %s, %s, %s, %s)", (User_name, User_surname, User_pseudo, User_password, User_email, User_phone))
        cnx.commit()
        cnx.close()
        return 'success'

if __name__ == '__main__':
    app.run()