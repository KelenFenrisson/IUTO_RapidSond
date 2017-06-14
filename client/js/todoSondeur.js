var formulaire_Appel = affiche_HTML("formulaire_Appel.html");
var formulaire_infoQuest = affiche_HTML("formulaire_infoQuest.html");
var formulaire_infoSonde = affiche_HTML("formulaire_infoSonde.html");
var reponse_questions_sonde = affiche_HTML("reponse_questions_sonde.html");
var choixlibre_sonde=affiche_HTML('choixlibre_sonde.html');
var choixmultiple_sonde=affiche_HTML('choixmultiple_sonde.html');
var choixunique_sonde=affiche_HTML('choixunique_sonde.html');


var questionnaireCourant;
var sondeCourant;

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

  questionnaireCourant=trouverQuestionnaireCourant();
  sondeCourant = trouverSondeCourant();


  remplirInfosFormulaireQuestionnaire(questionnaireCourant);
  remplirInfosFormulaireSonde(sondeCourant);
}


function retourSondeur(){

  $("#main").empty();
  $("#main").append('<div id="sondeInfo" class="col-md-6"/>');
  $("#sondeInfo").append($(formulaire_infoSonde).html());

  $("#main").append('<div id="questInfo" class="col-md-6"/>');
  $("#questInfo").append($(formulaire_infoQuest).html());


  $("#main").append($(formulaire_Appel).html());


  remplirInfosFormulaireQuestionnaire(questionnaireCourant);
  remplirInfosFormulaireSonde(sondeCourant);
}


function afficheReponseQuestionSonde(){

  $("#main").empty();
  $("#main").append($(reponse_questions_sonde).html());
  remplirInfoQuestionnaireDetails(questionnaireCourant);
  afficheLesQuestions(questionnaireCourant);
}

function ajoutJSONformulaire(data){
    //console.log(JSON.stringify(data));
    console.log(data["data"]["id"]);
  //  $(#titreForm).empty();
    $("#titreForm").text("Formulaire n° "+data["data"]["id"]);
    $("#titre").text(data["data"]["titre"]);
    setNomPanel(data["data"]["panel"]);
    setNomClient(data["data"]["client"]);

}


function setNomPanelJSON(data){
       $("#titrepan").text(data["data"]["intitule"]);
}



function setNomClientJSON(data){
  $("#titrecli").text(data["data"]["raison"])
}

function ajoutJSONsonde(data){


    $("#numTel").text("Téléphone : "+data["data"]["telephone"]);
    $("#titreformSonde").text("Sondé n° "+data["data"]["id"]);
    $("#nomsond").val(data["data"]["nom"]);
    $("#prenomsond").val(data["data"]["prenom"]);
    $("#datesond").val(data["data"]["date_naissance"]);
}


function trouverQuestionnaireCourant(){
  return "1";
}

function trouverSondeCourant(){
  return "1";
}

function ajoutJSONQuestDetail(data){
  $("#titrequestdet").text("Formulaire n° "+data["data"]["id"]);
  setNomConcepteur(data["data"]["concepteur"]);
  setNomClient(data["data"]["client"]);
  setNomSonde(sondeCourant);
}

function setNomConcepteurJSON(data){
  $("#createur").text(data["data"]["nom"]+" "+data["data"]["prenom"]);
}
function setNomSondeJSON(data){
  $("#sonde").text(data["data"]["nom"]+" "+data["data"]["prenom"]);}


function afficheJSONQuestion(data){
	var listeQuestion = data["data"]["questions"];
  console.log(listeQuestion[1]);

	for(var i=0;i<listeQuestion.length;++i){
		affiche_Question_Donnees_Sondeur(listeQuestion[i]);
	}

	$('#TitreFormulaire').text("Formulaire N°"+data["data"]["id"]);
}
function setNomQuestionJSON(data){
  $("#listeQuestions").append("<p>"+data["data"]["intitule"]+"</p>");
}


function annulationQuestion(){
  if (confirm("Voulez-vous vraiment annuler ?")) { // Clic sur OK
    retourSondeur();}
}


function affiche_Question_Affichage_Sondeur(data){

	var num = data["data"]["objects"][0]["numero"];

	console.log(data["data"]["objects"][0]["id_type"]);
	switch(data["data"]["objects"][0]["id_type"]) {

	    case "u":
			$("#listeQuestions").append($(choixunique_sonde).html());
			$("#choixunique").attr("id","typeQuestionnaire"+num);
	        break;

		case "l":
			$("#listeQuestions").append($(choixlibre_sonde).html());
			$("#choixlibre").attr("id","typeQuestionnaire"+num);
			break;

		case "m":

			//création et affichage de la question
			$("#listeQuestions").append($(choixmultiple_sonde).html());
			$("#choixmul").attr("id","typeQuestionnaire"+num);


			console.log("C'est un type Note");
			var reponses = data["data"]["objects"][0]["reponses"];

			//juste pour test
			// reponses[0]="cool";
			// reponses[1]="Pas top";
			// reponses[2]="NULLLLLLLLL";
			//juste pour test

			// affiche les réponses dans les input avec désactivation
			for(var i=0;i<reponses.length;++i){
				$("#reponse"+i).text(reponses[i]);


			}
			break;
	}
	try{
		$("#legendeQuestion").attr("id","legendeQuestion"+num);
		$("#question").attr("id","question"+num);

		//changement des noms des Ids  ******************************************************
		// change le numéro de la question

	$("#legendeQuestion"+num).text("Question "+num);
		//remplit la question
		$("#question"+num).text(data["data"]["objects"][0]["intitule"]);
		//désactive la question



	}
	catch(err)
	{
		console.log("Pas de questions")
	}


}
//Debut fonction Roméo
//Fin fonction Roméo
//Debut fonction Léo
//Fin fonction Léo
