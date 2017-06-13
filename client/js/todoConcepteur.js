//création des variables html
var formulaire_Recherche_Sondage = affiche_HTML("formulaire_Recherche_Sondage.html");
var formulaire_Sondage_A_Remplir = affiche_HTML("formulaire_Sondage_A_Remplir.html");
var formulaire_Question_A_Remplir3 = affiche_HTML("formulaire_Question_A_Remplir3.html");
var formulaire_Question_A_Remplir2 = affiche_HTML("formulaire_Question_A_Remplir2.html");
var formulaire_Question_A_Remplir = affiche_HTML("formulaire_Question_A_Remplir.html");
var formulaire_Info_Sondage = affiche_HTML("formulaire_Info_Sondage.html");
var formulaire_Sondage_A_Remplir = affiche_HTML("formulaire_Sondage_A_Remplir.html");

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

//Début fonction affichage des différentes DIVS

function accueilConcepteur(){
	$("#main").empty();
	$("#main").append('<input type="button" value="Créer un nouveau sondage" class="btn btn-primary btn-lg active top-10 col-md-offset-3 col-md-6 bot-10" onclick="creerFormulaire()">');
    $("#main").append($(formulaire_Recherche_Sondage).html());
	// CECI EST POUR LEXEMPLE, à EDITER PAR LA SUITE AVEC UNE RECHERCHE DANS LA BASE
	for(var i =0;i<4;i++)
	$("#main").append($(formulaire_Info_Sondage).html());

}

function creerFormulaire(){
	$("#main").empty();
  $("#main").append($(formulaire_Sondage_A_Remplir).html());
	$("#main").append($(formulaire_Question_A_Remplir).html());
  $("#main").append($(formulaire_Question_A_Remplir3).html());
  $("#main").append($(formulaire_Question_A_Remplir2).html());
	$("#typeQuestionnaire").empty();
  $("#typeQuestionnaire2").empty();
  $("#typeQuestionnaire3").empty();
  remplissageFormQuest();
}

function choisirTypeQuestion(type){

	if(type.value=="choixM"){
		$("#typeQuestionnaire2").empty();
	    $("#typeQuestionnaire3").empty();
	    $("#typeQuestionnaire").replaceWith($(formulaire_Question_A_Remplir).html());
	  }

	if(type.value=="yesOrNo"){
	  $("#typeQuestionnaire").empty();
	  $("#typeQuestionnaire2").empty();
	  $("#typeQuestionnaire3").replaceWith($(formulaire_Question_A_Remplir3).html());
	}

	if(type.value=="reponseLibre"){
	  $("#typeQuestionnaire").empty();
	  $("#typeQuestionnaire3").empty();
	  $("#typeQuestionnaire2").replaceWith($(formulaire_Question_A_Remplir2).html());
  	}

}


// Pour les questions avec une choix multiple
function ajoutReponse(){
  $('#checkboxReponses').append('<div class="row" id="row">\n<input type="checkbox" id="checkboxreponse" value="reponse"/>\n<input type="text" id="reponse" placeholder="Entrer une réponse"/>\n</div>');
}

function supprReponse(){
  $('#row').last().remove();
}

//Debut fonction Jérémie
//Fin fonction Jérémie
//Debut fonction Olivier
function ajouteClient(client){
  for(var i=0; i<client["data"]["num_results"]; i++){
    $('#listeClient').append('<option value="'+client['data']['objects'][i]['raison']+'">'+client['data']['objects'][i]['raison']+'</option>');
  }
}

function ajouteUtilisateur(utilisateur){
  for(var i=0; i<utilisateur["data"]["num_results"]; i++){
    $('#choixConcepteur').append('<option value="'+utilisateur['data']['objects'][i]['nom']+'">'+utilisateur['data']['objects'][i]['nom']+'</option>');
  }
}

function ajoutePanel(panel){
  for(var i=0; i<panel["data"]["num_results"]; i++){
    $('#choixPanel').append('<option value="'+panel['data']['objects'][i]['intitule']+'">'+panel['data']['objects'][i]['intitule']+'</option>');
  }
}

//Fin fonction Olivier
//Debut fonction Julien
//Fin fonction Julien
