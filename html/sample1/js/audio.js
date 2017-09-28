/**/
// Audio player
//{numberOfLoops:"infinite"}
var my_media = null;
var mediaTimer = null;

// Play audio
//
function playAudio(src) {
    //return false;
    var sound = $("#sound").html();
    if(sound =='off'){
       return false;  
    }
   var audio_file = $("#audio_file").html();
   if(audio_file!=src){
         stopAudio()    
   }else{
       return false;
   }
  // Create Media object from src
  $("#audio_file").html(src);
  my_media = new Media(src, onSuccess, onError);
  var lang = $("#lang").html();

    if (src.indexOf("pg_") !=-1){
       my_media.play();
    }else{
       my_media.play({numberOfLoops:"infinite"});
    }
    

}


// Stop audio
// 
function stopAudio() {
    if (my_media) {
        my_media.stop();
        $("#audio_file").html("");
    }
}

// onSuccess Callback
//
function onSuccess() {
   // console.log("playAudio():Audio Success");
}

// onError Callback 
//
function onError(error) {
   // alert('code: '    + error.code    + '\n' +
    //      'message: ' + error.message + '\n');
}




