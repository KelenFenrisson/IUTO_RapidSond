function afficheAccueil(){

	$("#main").empty();
	$("#main").append($("<div>").load("accueil_Connexion.html"));

}

function seConnecter(){
	// console.log($("#role option:selected").val());
	if($("#role option:selected").val()=="concepteur")
		accueilConcepteur();
	if($("#role option:selected").val()=="sondeur")
		accueilSondeur();
}
