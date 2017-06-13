var urlBase = "http://192.168.13.162:5000";

// function connect(adresse){
//
//       $.ajax({
//          url: "http://192.168.13.162:5000"+adresse,
//          type: "GET",
//          // This is the important part
//          xhrFields: {
//              withCredentials: true
//          },
//          // This is the important part
//          crossDomain: true,
//          dataType: 'jsonp',
//          success: function (reponse) {
// 			 console.log(JSON.stringify(reponse));
//          },
//          error: function (xhr, status) {
//              console.log("Erreur de connexion");
//          }
//       });
// }

function remplirlisteEntreprise(){
  console.log("OCUOCU");
    $('#listeEntreprise').append("<option value ='1'>couille</option>");
}

function appui(){
  console.log($("#listeEntreprise").val());
}

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
