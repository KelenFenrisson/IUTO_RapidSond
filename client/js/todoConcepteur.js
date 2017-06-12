function accueilConcepteur(){

		$("#main").empty();
		//ajout du bouton de cration de questionnaire
		$("#main").append('<input type="button" value="Créer un nouveau sondage" class="btn btn-primary btn-lg active top-10 col-md-offset-3 col-md-6 bot-10" onclick="creerFormulaire()">');
		//ajout de recherche filtre

		// $("#main").append($("<div>").append('<div id="formulaire_Recherche_Sondage" class="col-md-offset-1 col-md-10"><form id="formFiltre" class="col-md-12 form-horizontal border" method="GET" ><div class="row"><label id="labelEntreprise" for="listeEntreprise" class="col-md-2 top-10 text-center">Entreprise </label><div class="col-md-2">	<select id="listeEntreprise" name="listeEntreprise" class="col-md-10 top-10 text-center"><option value="1" selected="selected">test</option></select></div><label id="labelStatut" for="listeStatut" class="col-md-2 top-10 text-center">Statut </label><div class="col-md-2"><select id="listeStatut" name="listeStatut" class="col-md-10 top-10 text-center" /></select></div><label id="labelConcepteur" for="listeConcepteur" class="col-md-2 top-10 text-center">Concepteur </label><div class="col-md-2"> <select id="listeConcepteur" name="listeConcepteur" class="col-md-10 top-10 text-center" /></select></div></div><div class="row"><label id="labelPanel" for="listePanel" class="col-md-2 top-10 text-center">Panel</label><div class="col-md-2"><select id="listePanel" name="listePanel" class="col-md-10 top-10 text-center" /></select></div><label id="labelDateDebut" for="choixDateDebut" class="col-md-2 top-10 text-center">Date</label><div class="col-md-3"><select id="choixDateDebut" name="choixDateDebut" class="col-md-4 top-10 text-center" /></select><label id="labelDateFin" for="choixDateFin" class="col-md-4 text-center top-10"> à </label><select id="choixDateFin" name="choixDateFin" class="col-md-4 top-10 text-center" /></select></div><input type="submit" value="Actualiser" class="btn btn-primary top-10 col-md-offset-1 col-md-1 bot-10"></div></form></div>'));
			$( "#main" ).append(formulaire_Recherche_Sondage.html.text());
		// CECI EST POUR LEXEMPLE, à EDITER PAR LA SUITE AVEC UNE RECHERCHE DANS LA BASE
		for(var i =0;i<4;i++)
		$("#main").append($("<div>").load("formulaire_Info_Sondage.html"));

		console.log("test");
		console.log($("#listeEntreprise option:selected").text());

}


function creerFormulaire(){
	console.log("test");
	console.log($("#listeEntreprise option:selected").text());
		$("#main").empty();
		$("#main").append($("<div id='typeQuestionnaire'>").load("formulaire_Question_A_Remplir.html"));

}

function choisirTypeQuestion(type){
	if(type.value=="choixM")
		$("#typeQuestionnaire").load("formulaire_Question_A_Remplir.html");
	if(type.value=="yesOrNo")
		$("#typeQuestionnaire").load("formulaire_Question_A_Remplir3.html");
	if(type.value=="reponseLibre")
		$("#typeQuestionnaire").load("formulaire_Question_A_Remplir2.html");
}


// Pour les questions
function ajoutReponse(){
  $('#checkboxReponses').append('<div class="row" id="row">\n<input type="checkbox" id="checkboxreponse" value="reponse"/>\n<input type="text" id="reponse" placeholder="Entrer une réponse"/>\n</div>');
}

function supprReponse(){
  $('#row').last().remove();
}
