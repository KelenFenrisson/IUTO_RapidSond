function accueilConcepteur(){

		$("#main").empty();
		$("#main").append('<input type="button" value="Créer un nouveau sondage" class="btn btn-primary btn-lg active top-10 col-md-offset-3 col-md-6 bot-10" onclick="afficheQuestionnaires()">');
		$("#main").append($("<div>").load("formulaire_Recherche_Sondage.html"));
		// CECI EST POUR LEXEMPLE, à EDITER PAR LA SUITE AVEC UNE RECHERCHE DANS LA BASE
		for(var i =0;i<4;i++)
		$("#main").append($("<div>").load("formulaire_Info_Sondage.html"));


}
