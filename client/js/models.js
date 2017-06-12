
function connect(adresse, fonction){
      $.ajax({
         url: adresse,
         type: "GET",
         // This is the important part
         xhrFields: {
             withCredentials: true
         },
         // This is the important part
         crossDomain: true,
         dataType: 'jsonp',
         success: fonction,
         error: function (xhr, status) {
             console.log("Erreur de connexion");
         }
      });
}

function remplirlisteEntreprise(){


  console.log("OCUOCU");



    $('#listeEntreprise').append("<option value ='1'>couille</option>");






}

function appui(){
  console.log($("#listeEntreprise").val());
}
