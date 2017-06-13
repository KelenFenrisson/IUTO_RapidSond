
function connect(adresse){
      $.ajax({
         url: "192.168.13.162:5000"+adresse,
         type: "GET",
         // This is the important part
         xhrFields: {
             withCredentials: true
         },
         // This is the important part
         crossDomain: true,
         dataType: 'jsonp',
         success: function (response) {
             return response;
         },
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
