var formulaire_Appel = affiche_HTML("formulaire_Appel.html");
var formulaire_infoQuest = affiche_HTML("formulaire_infoQuest.html");
var formulaire_infoSonde = affiche_HTML("formulaire_infoSonde.html");

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


function accueilSondeur(){

  $("#main").empty();
  $("#main").append('<div id="sondeInfo" class="col-md-6"/>');
  $("#sondeInfo").append($(formulaire_infoSonde).html());

  $("#main").append('<div id="questInfo" class="col-md-6"/>');
  $("#questInfo").append($(formulaire_infoQuest).html());

  $("#main").append($(formulaire_Appel).html());
}




function remplirInfosFormulaire(idFormulaire){
  
}
