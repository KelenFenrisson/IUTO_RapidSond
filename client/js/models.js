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



function modif(adresse,data){
    $.ajax({
        url:urlBase+adresse,
        type:'PUT',
        data:data,
        //JSON.stringify({"id":1,"nom":"MABITE"})
        contentType: "application/json",
        success: function (msg) {
            console.log('Update Success');
        },
        error: function (err){
            console.log('Update Error');
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

function modifSonde(idSond){
  data =
  modif(adresse,data)
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
