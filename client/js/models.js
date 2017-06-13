var urlBase = "http://192.168.13.162:5000";

//La fonction principale
function connect(adresse,fonc){
    var rep = null;
      $.ajax({
         url: "http://192.168.13.162:5000"+adresse,
         type: "GET",
         // This is the important part
         xhrFields: {
             withCredentials: true
         },
         // This is the important part
         crossDomain: true,
         dataType: 'jsonp',
         success: fonc,
         error: function (xhr, status) {
             console.log("Erreur de connexion");
         }
      });

}


function Sonde(nom){
    this.nom=nom;
}


function modif(){
    $.ajax({
        url:"http://192.168.13.162:5000/api/sonde/1",
        type:'PUT',
        contentType: "application/json",
        data:JSON.stringify({"id":1,"nom":"picouille"}),
        xhrFields: {
            withCredentials: true
        },
        // This is the important part
        crossDomain: true,
        dataType: 'jsonp',
        success: function (msg) {
            alert('Update Success');
        },
        error: function (err){
            alert('Update Error');
        }
        });

}
// Début fonction Léo
function remplirInfosFormulaireQuestionnaire(idFormulaire){
  connect("/api/questionnaire/"+idFormulaire,ajoutJSONformulaire);
}
function setNomPanel(lienPanel){
    connect(lienPanel,setNomPanelJSON);
}
function setNomClient(lienClient){
  connect(lienClient,setNomClientJSON);
}
function setNomConcepteur(lienConcept){
  connect(lienConcept,setNomConcepteurJSON);
}
function remplirInfosFormulaireSonde(idSonde){
  connect("/api/sonde/"+idSonde,ajoutJSONsonde);
}
function remplirInfoQuestionnaireDetails(idFormulaire){
  connect("/api/questionnaire/"+idFormulaire,ajoutJSONQuestDetail);
}
function setNomSonde(idSonde){
  connect("/api/sonde/"+idSonde,setNomSondeJSON);
}
function afficheLesTitresQuestions(idFormulaire){
    connect("/api/questionnaire/"+idFormulaire,afficheJSONQuestion);
}

function setNomQuestion(lienQuest){
  connect(lienQuest,setNomQuestionJSON);
}
// Fin fonction Léo

//Debut fonction Roméo
//Fin fonction Roméo
//Debut fonction Jérémie
//Fin fonction Jérémie
//Debut fonction Olivier
//Fin fonction Olivier
//Debut fonction Julien
//Fin fonction Julien

function modifSondage(){

	  $.ajax({
		 url: urlBase+"/api/questionnaire/1",
		 type: "GET",
		 // This is the important part
		 xhrFields: {
			 withCredentials: true
		 },
		 // This is the important part
		 crossDomain: true,
		 dataType: 'jsonp',
		 success: function (data) {
			console.log(JSON.stringify(data));
			console.log(data["data"]["id"])
		},
		 error: function (xhr, status) {
			 console.log("Erreur de connexion");
		 }
	  });

}
