function accueilConcepteur(){

		$("#main").empty();
		$("#main").append('<input type="button" value="Créer un nouveau sondage" class="btn btn-primary btn-lg active top-10 col-md-offset-3 col-md-6 bot-10" onclick="creerFormulaire()">');
		$("#main").append($("<div>").load("formulaire_Recherche_Sondage.html"));
		// CECI EST POUR LEXEMPLE, à EDITER PAR LA SUITE AVEC UNE RECHERCHE DANS LA BASE
		for(var i =0;i<4;i++)
		$("#main").append($("<div>").load("formulaire_Info_Sondage.html"));

}


function creerFormulaire(){

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
