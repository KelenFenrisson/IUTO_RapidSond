//création des variables html
var formulaire_Recherche_Sondage = affiche_HTML("formulaire_Recherche_Sondage.html");
var formulaire_Sondage_A_Remplir = affiche_HTML("formulaire_Sondage_A_Remplir.html");
var formulaire_Question_A_Remplir3 = affiche_HTML("formulaire_Question_A_Remplir3.html");
var formulaire_Question_A_Remplir2 = affiche_HTML("formulaire_Question_A_Remplir2.html");
var formulaire_Question_A_Remplir = affiche_HTML("formulaire_Question_A_Remplir.html");
var formulaire_Info_Sondage = affiche_HTML("formulaire_Info_Sondage.html");
var accueil_Connexion = affiche_HTML("accueil_Connexion.html");

// Début fonction récup HTML en string *******************************************************************************
function affiche_HTML(fichierHTML)
{
     var result = null;
     $.ajax({
        url: fichierHTML,
        type: 'get',
        dataType: 'html',
				data:'',
        async: false,
        success: function(data) {
            result = data;

        }
     });
     return result;
}

//Fin fonction récup HTML en string *******************************************************************************
function accueilConcepteur(){

		$("#main").empty();
		$("#main").append('<input type="button" value="Créer un nouveau sondage" class="btn btn-primary btn-lg active top-10 col-md-offset-3 col-md-6 bot-10" onclick="creerFormulaire()">');
<<<<<<< HEAD
    $("#main").append($(formulaire_Recherche_Sondage).html());
=======
		$("#main").append($("<div>").load("formulaire_Recherche_Sondage.html"));
>>>>>>> rom/master
		// CECI EST POUR LEXEMPLE, à EDITER PAR LA SUITE AVEC UNE RECHERCHE DANS LA BASE
		for(var i =0;i<4;i++)
		$("#main").append($(formulaire_Info_Sondage).html());


}


function creerFormulaire(){
		remplirlisteEntreprise();

		// $("#main").empty();
		// $("#main").append($("<div id='typeQuestionnaire'>").load("formulaire_Question_A_Remplir.html"));

}

function choisirTypeQuestion(type){
	if(type.value=="choixM")
		$("#typeQuestionnaire").load("formulaire_Question_A_Remplir.html");
	if(type.value=="yesOrNo")
		$("#typeQuestionnaire").load("formulaire_Question_A_Remplir3.html");
	if(type.value=="reponseLibre")
		$("#typeQuestionnaire").load("formulaire_Question_A_Remplir2.html");

}
