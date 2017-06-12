function accueilSondeur(){

  $("#main").empty();
  $("#main").append('<div id="test" class = "top-10-pour"/>');
  $("#test").append($('<div>').load("formulaire_infoSonde.html"));

  $("#test").append($('<div>').load("formulaire_infoQuest.html"));
  $("#test").append($("<div>").load("formulaire_Appel.html"));


}
