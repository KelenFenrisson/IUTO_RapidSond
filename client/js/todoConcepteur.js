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
function affiche_Question_Affichage(data){
	console.log(data);
	console.log(data["data"]["id_type"]);
	console.log(data["data"]["id"]);

	var id = data["data"]["id"];

	switch(data["data"]["id_type"]) {
		// si Question est de type note
    case "n":
		console.log("C'est un type Note");
		//création et affichage de la question
		$("#main").append($(formulaire_Question_A_Remplir).html());
		$("#typeQuestionnaire").attr("id","typeQuestionnaire"+id);
		$("#legendeQuestion").attr("id","legendeQuestion"+id);
		$("#question").attr("id","question"+id);
		$("#boutonValider").attr("id","boutonValider"+id);
		$("#boutonAnnuler").attr("id","boutonAnnuler"+id);

		//changement des noms des Ids  ******************************************************
		// change le numéro de la question
		$("#legendeQuestion"+id).text("Question"+id);
		//remplit la question
		$("#question"+id).val(data["data"]["intitule"]);
		//désactive la question
		$("#question"+id).prop('disabled', true);
		//change le boutton en edit avec sa fonction du onclick
		$("#boutonValider"+id).attr("value","Edit");
		$("#boutonValider"+id).attr("onclick","editQuestion()");
		//change le boutton en suppr avec sa fonction du onclick
		$("#boutonAnnuler"+id).attr("value","Suppr");
		$("#boutonAnnuler"+id).attr("onclick","suppressionQuestion()");
		//cache les bouttons
		$("#boutonAjoutReponse").hide();
		$("#boutonSupprimerReponse").hide();
		$("#choixTypeQuestion").hide();


		var reponses = data["data"]["reponses"];

		//juste pour test
		reponses[0]="cool";
		reponses[1]="Pas top";
		reponses[2]="NULLLLLLLLL";
		//juste pour test

		// affiche les réponses dans les input avec désactivation 
		for(var i=0;i<reponses.length;++i){
			$("#reponse"+i).val(reponses[i]);
			$("#reponse"+i).prop('disabled', true);
		}

        break;
    // case "u":
	// 	console.log("C'est un type Unique");
	// 	$("#main").append($(formulaire_Question_A_Remplir3).html());
    //     break;
	// case "c":
	// 	console.log("C'est un type Classement");
	// 	break;
	// case "l":
	// 	console.log("C'est un type Libre");
	// 	$("#main").append($(formulaire_Question_A_Remplir2).html());
	// 	break;
	// case "m":
	// 	console.log("C'est un type Multiple");
	// 	$("#main").append($(formulaire_Question_A_Remplir).html());
	// 	break;

	}
}

function modifierSondageAffichage(data){
	console.log(JSON.stringify(data));
	console.log(data["data"]["questions"]);
	console.log(data["data"]["id"]);

	var listeQuestion = data["data"]["questions"];
	for(var i=0;i<listeQuestion.length;++i){
		console.log(listeQuestion[i]);
		affiche_Question_Donnees(listeQuestion[i]);

	}

	$('#TitreFormulaire').text("Formulaire N°"+data["data"]["id"]);
}

// function affiche_client_par_sondage(data){
// 	console.log(JSON.stringify(data));
// 	console.log(data["data"]["adresse"]);
// 	$
// }
//Fin fonction Julien
