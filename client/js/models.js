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

// Début fonction Léo
function remplirInfosFormulaire(idFormulaire){
  connect("/api/questionnaire/"+idFormulaire,testJSON);
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
