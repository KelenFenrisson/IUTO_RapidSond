var formulaire_Appel = affiche_HTML("formulaire_Appel.html");
var formulaire_infoQuest = affiche_HTML("formulaire_infoQuest.html");
var formulaire_infoSonde = affiche_HTML("formulaire_infoSonde.html");
var reponse_questions_sonde = affiche_HTML("reponse_questions_sonde.html");

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
  afficheLesTitresQuestions(questionnaireCourant);
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
  for (var i=0;i<data["data"]["questions"].length;i++)
  setNomQuestion(data["data"]["questions"][i])
}

function setNomQuestionJSON(data){
  $("#listeQuestions").append("<p>"+data["data"]["intitule"]+"</p>");
}


function annulationQuestion(){
  if (confirm("Voulez-vous vraiment annuler ?")) { // Clic sur OK
    retourSondeur();}
}

//Debut fonction Roméo
//Fin fonction Roméo
//Debut fonction Léo
//Fin fonction Léo
