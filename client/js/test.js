$(function() {


  $.ajax({
     url: "http://192.168.13.141:5000/api/questionnaire",
     type: "GET",
     // This is the important part
     xhrFields: {
         withCredentials: true
     },
     // This is the important part
     crossDomain: true,
     dataType: 'jsonp',
     success: function (response) {
         console.log(JSON.stringify(response));
     },
     error: function (xhr, status) {
         console.log("Mon cul");
     }
  });

})
