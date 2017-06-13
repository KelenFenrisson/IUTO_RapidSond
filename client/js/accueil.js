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

function afficheAccueil(){
	$("#main").empty();
	$("#main").append($(accueil_Connexion).html());
}

function seConnecter(){
	// console.log($("#role option:selected").val());
	if($("#role option:selected").val()=="concepteur")
		accueilConcepteur();
	if($("#role option:selected").val()=="sondeur")
		accueilSondeur();
}
