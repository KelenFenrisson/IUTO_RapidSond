function accueilConcepteur(){

		$("#main").empty();
		$("#main").append('<input type="submit" value="Créer un nouveau sondage" class="btn btn-primary btn-lg active top-10 col-md-offset-3 col-md-6 bot-10">');
		$("#main").append($("<div>").load("formulaire_Recherche_Sondage.html"));
		// CECI EST POUR LEXEMPLE, à EDITER PAR LA SUITE AVEC UNE RECHERCHE DANS LA BASE
		for(var i =0;i<4;i++)
		$("#main").append($("<div>").load("formulaire_Info_Sondage.html"));


<<<<<<< HEAD
	//création de la div de filtrage

	$('#main').append('<div id="filreSondage" class="col-md-12 " />');
	$('#filreSondage').append('<form id="formFiltre" class="col-md-12 form-horizontal" method="GET" /></form>');
	$('#formFiltre').append('<label id=labelFiltre for="labelEntreprise"  class="col-md-1 col-md-offset-1" >Filtre : <label/> ');

	$('#formFiltre').append('<label id="labelEntreprise" for="listeEntreprise" class="col-md-1 ">Entreprise <label /> ');
	$('#formFiltre').append('<select id="listeEntreprise" name="listeEntreprise" class="col-md-2 " /> ');

	$('#formFiltre').append('<label id="labelStatut" for="listeStatut" class="col-md-1 ">Statut <label /> ');
	$('#formFiltre').append('<select id="listeStatut" name="listeStatut" class="col-md-2 " /> ');

	$('#formFiltre').append('<label id="labelConcepteur" for="listeConcepteur" class="col-md-1 ">Concepteur <label /> ');
	$('#formFiltre').append('<select id="listeConcepteur" name="listeConcepteur" class="col-md-2 " /> ');


}

function creationFormulaire(){

  $('#main').hide();
	$('#div2').on("click",function(){
		$("#main").show()
	}
>>>>>>> jeremy/master
=======
>>>>>>> leo/master
}
