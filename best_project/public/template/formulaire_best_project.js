function date_default(){document.getElementById('date').valueAsDate = new Date();}

function selection_niveau_maths(){
    if (document.getElementById("Mathematique").checked == true){
        document.getElementById("container_maths").style.visibility="visible";
    } else{
        document.getElementById("container_maths").style.visibility="hidden";
    }
}

function selection_niveau_francais() {
    if (document.getElementById("Francais").checked == true){
        document.getElementById("container_francais").style.visibility="visible";
    } else{
        document.getElementById("container_francais").style.visibility="hidden";
    }

}

function selection_niveau_histoire() {
    if (document.getElementById("Histoire").checked == true){
        document.getElementById("container_histoire").style.visibility="visible";
    } else{
        document.getElementById("container_histoire").style.visibility="hidden";
    }

}

function selection_niveau_chimie() {
    if (document.getElementById("Chimie").checked == true){
        document.getElementById("container_chimie").style.visibility="visible";
    } else{
        document.getElementById("container_chimie").style.visibility="hidden";
    }
}

function verif_formulaire() {

    //si il y a une erreur on ne déverouille pas le bouton d'envoie
    var erreur =0
    // on incremente a chaque fois qu'il y a une erreur

    // definit un RegExp pour le telephone
    var Regegex_tel = new RegExp("^(0|\\+33|0033)[1-9][0-9]{8}$")
    if (Regegex_tel.test(document.getElementById("tel").value)) {
        document.getElementById("numero_incorrect").style.visibility="hidden";
    } else {
        document.getElementById("numero_incorrect").style.visibility="visible";
        erreur +=1;
    }
    // affiche le message d'erreur du tel
    
    var Regegex_mail = new RegExp("^[a-zA-Z0-9._-]+@[a-zA-Z0-9._-]{2,}\.[a-z]{2,4}$")
    if ((Regegex_mail.test(document.getElementById("email").value)) || (document.getElementById("email").value.length === 0)) {
        document.getElementById("email_incorrect").style.visibility="hidden";
    } else {
        document.getElementById("email_incorrect").style.visibility="visible";
        erreur +=1;
    }
    // le || permet de faire un OR; je test la longueyr de la chaine email et si elle est nulle alors cela veux dire qu'il n'y a pas d'email renseigné -->ok
    
// pour le mot de passe je verifie qu'il y ai 1 minuscule (score_pass + 1), 1 majuscule, 1 nombre et 8 caractères    
    score_pass=0
    if (document.getElementById("mdp").value.length != 0) {
        var pass = document.getElementById("mdp").value
        if (pass.match(/[a-z]/)){
            score_pass +=1;
        } if (pass.match(/[A-Z]/)){
            score_pass +=1;
        } if (pass.match(/[0-9]/)){
            score_pass +=1;
        } if (pass.length > 7){
            score_pass +=1;
        } if (score_pass == 4){
            document.getElementById("password_incorrect").style.visibility="hidden";
        }
    } else {
        document.getElementById("password_incorrect").style.visibility="visible";
        erreur +=1;
    } 
//donc si le score final est =4 c'est que toutes les conditions sont respectées
//si on veux je peux assigner une lettre à chaque erreur et ainsi afficher quelle erreur l'utilisateur a fait


// on calcule le nombre d'année d'écart et on affiche le message d'erreur (la division sert à transformer la difference en seconde en difference en année)
// j'ai mis <17 car sinon toute l'année des 18 part aussi (je crois)  
    d1= new Date()
    d2= new Date(document.querySelector('input[type="date"]').value)
    if (Number((d1.getTime() - d2.getTime()) / 31536000000).toFixed(0) < 17 ||Number((d1.getTime() - d2.getTime()) / 31536000000).toFixed(0) >100) {
        document.getElementById("age_incorrect").style.visibility="visible";
        erreur +=1;
    } else {
        document.getElementById("age_incorrect").style.visibility="hidden";
    }


    //si il n'y a aucune erreur on autorise l'envoie du formulaire, sinon on décoche la case (et on fait apparaitre les differents messages d'erreur)
    if (erreur==0){
        document.getElementById("bouton_d_envoie").disabled = false
    } else {
        document.getElementById("verification").checked = false
        document.getElementById("bouton_d_envoie").disabled = true
    }
}