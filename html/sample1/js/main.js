
$(document).bind( "mobileinit", function(event) {
   $.mobile.transitionFallbacks.slideout = "none";
                  //document.getElementById('movie').controls = false;
             //    $.mobile.transitionHandlers = { "default" : $.mobile.defaultTransitionHandler };
         });

$(document).bind("mobileinit", function () {
    /*This line to avoid blink JQM issue*/
    $.mobile.defaultPageTransition = 'none';
    $.mobile.defaultHomeScroll = 0;
});
$('#main').live('pageinit',function(){
  //$('.dot').remove();
  
  
});
$(document).ready(function() {
  document.getElementById('movie').controls = false;
 // $('.dot').remove();

  
  $('video#movie').bind('ended',function(){
           // $('#vid_container').remove();
           $.mobile.changePage($('#menu_principal'),{transition: "slide"});
       });

});
/*PAGE 1*/

$('#pg1').live('pageinit',function(){

});
$( '#pg1' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
    if(lang=="spanish"){
        playAudio('/audio/pg_1.mp3');      
    }else if(lang=="english"){
             playAudio('/audio/en_pg_1.mp3');
    }else{
        if(audio_file !='/audio/mmt_1.mp3'){
         stopAudio();
         playAudio('/audio/mmt_1.mp3');
     }
 }

});
$( '#pg1' ).live('pagehide',function(event, ui){
    audio_hide();
});
/*PAGE 2*/
$('#pg2').live('pageinit',function(){
 

});
$( '#pg2' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
        if(audio_file !='/audio/mmt_1.mp3'){
         stopAudio();
         playAudio('/audio/mmt_1.mp3');
        }
});
$( '#pg2' ).live('pagehide',function(event, ui){
   audio_hide();              

});
/*PAGE 3*/
$('#pg3').live('pageinit',function(){
   
});

$( '#pg3' ).live('pageshow',function(event, ui){
   var lang = $("#lang").html();
   var audio_file = $("#audio_file").html();
   if(lang=="spanish"){
     playAudio('/audio/pg_3.mp3');
   }else if(lang=="english"){
      playAudio('/audio/en_pg_3.mp3');
   }else{
    if(audio_file !='/audio/mmt_1.mp3'){
     stopAudio();
     playAudio('/audio/mmt_1.mp3');
    }
   }

});
$( '#pg3' ).live('pagehide',function(event, ui){
    audio_hide();

});
/*PAGE 4*/
$('#pg4').live('pageinit',function(){
    
});
$( '#pg4' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
        if(audio_file !='/audio/mmt_1.mp3'){
         stopAudio();
         playAudio('/audio/mmt_1.mp3');
     }
 
});
$( '#pg4' ).live('pagehide',function(event, ui){
   audio_hide();
});
/*PAGE 5*/
$('#pg5').live('pageinit',function(){
 
});

$( '#pg5' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
  if(lang=="spanish"){
     playAudio('/audio/pg_5.mp3');
  }else if(lang=="english"){
     playAudio('/audio/en_pg_5.mp3');
  }else{
    if(audio_file !='/audio/mmt_1.mp3'){
        stopAudio();
        playAudio('/audio/mmt_1.mp3');
    }
}

});
$( '#pg5' ).live('pagehide',function(event, ui){
    audio_hide();           
});
/*PAGE 6*/
$('#pg6').live('pageinit',function(){       

 
});
$( '#pg6' ).live('pageshow',function(event, ui){
   var lang = $("#lang").html();
   var audio_file = $("#audio_file").html();
   if(lang=="spanish"){
     playAudio('/audio/pg_6.mp3');
    }else if(lang=="english"){
      playAudio('/audio/en_pg_6.mp3');
   }else{
    if(audio_file !='/audio/mmt_2.mp3'){
        stopAudio();
        playAudio('/audio/mmt_2.mp3');
    }
}                
});
$( '#pg6' ).live('pagehide',function(event, ui){
 audio_hide();         
});

/*PAGE 7*/
$('#pg7').live('pageinit',function(){
 
});

$( '#pg7' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
    if(lang=="spanish"){
     playAudio('/audio/pg_7.mp3');
    }else if(lang=="english"){
     playAudio('/audio/en_pg_7.mp3');
   }else{
    if(audio_file !='/audio/mmt_3.mp3'){
        stopAudio();
        playAudio('/audio/mmt_3.mp3');
    }
}

});
$( '#pg7' ).live('pagehide',function(event, ui){
    audio_hide();         
});
/*PAGE 7*/
$('#pg8').live('pageinit',function(){
   
});
$( '#pg8' ).live('pageshow',function(event, ui){
   var lang = $("#lang").html();
   var audio_file = $("#audio_file").html();
    if(audio_file !='/audio/mmt_3.mp3'){
     stopAudio();
     playAudio('/audio/mmt_3.mp3');
    }

});
$( '#pg8' ).live('pagehide',function(event, ui){
   audio_hide();
});
/*PAGE 9*/
$('#pg9').live('pageinit',function(){

   
});
$( '#pg9' ).live('pageshow',function(event, ui){
                 $('.pg9_bird').css('display','inline');
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
    if(lang=="spanish"){
     playAudio('/audio/pg_9.mp3');
    }else if(lang=="english"){
        playAudio('/audio/en_pg_9.mp3');
    }else{
    if(audio_file !='/audio/mmt_3.mp3'){
        stopAudio();
        playAudio('/audio/mmt_3.mp3');
    }
}


$('.pg9_bird').click(function(){
   // $(this).toggleClass('pag9_animation');
});


});
$( '#pg9' ).live('pagehide',function(event, ui){
    $('.pg9_bird').css('display','none');
    audio_hide();

});
/*PAGE 10*/
$('#pg10').live('pageinit',function(){

});
$( '#pg10' ).live('pageshow',function(event, ui){
    
    var lang = $("#lang").html();
    var windowWitchInterval = 20000;
    var audio_file = $("#audio_file").html();
        if(audio_file !='/audio/mmt_4.mp3'){
            stopAudio();
            playAudio('/audio/mmt_4.mp3');
        }

    witchEl = $(this).find('.pg10_windowshadow');

    var toggleWitch = function(){
        witchEl.animate( {'border':'1px solid transparent'}, 5500, 
            function() {
                witchEl.css({ 'top':'63px', 'left': '427px' });
            })
        .animate({'border': '1px solid transparent'}, 5500,
            function(){
                witchEl.css({ 'top':'247px', 'left': '610px' });
            }
            );
    };
                  toggleWitch();
    window.setInterval(toggleWitch, windowWitchInterval); 



});
$( '#pg10' ).live('pagehide',function(event, ui){
    audio_hide();

});

/*PAGE 11*/
$('#pg11').live('pageinit',function(){  

  
});
$( '#pg11' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
    if(lang=="spanish"){
     playAudio('/audio/pg_11.mp3');
    }else if(lang=="english"){
     playAudio('/audio/en_pg_11.mp3');
    }else{
    if(audio_file !='/audio/mmt_4.mp3'){
        stopAudio();
        playAudio('/audio/mmt_4.mp3');
    }
}                 
});
$( '#pg11' ).live('pagehide',function(event, ui){
    audio_hide();
    
    
});
/*PAGE 12*/
$('#pg12').live('pageinit',function(){
   
  
});
$( '#pg12' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
    if(lang=="spanish"){
     playAudio('/audio/pg_12a.mp3');
    }else if(lang=="english"){
     playAudio('/audio/en_pg_12.mp3');
    }else{
    if(audio_file !='/audio/mmt_5.mp3'){
        stopAudio();
        playAudio('/audio/mmt_5.mp3');
    }
}

});
$( '#pg12' ).live('pagehide',function(event, ui){
    audio_hide();

});
/*PAGE 13*/
$('#pg13').live('pageinit',function(){
 
  
    
});
$( '#pg13' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
    if(lang=="spanish"){
     playAudio('/audio/pg_13a.mp3');
    }else if(lang=="english"){
     playAudio('/audio/en_pg_13.mp3');
    }else{
    if(audio_file !='/audio/mmt_5.mp3'){
        stopAudio();
        playAudio('/audio/mmt_5.mp3');
    }
}
$('.pg13_herbs').click(function(){
    $(this).toggleClass('herbs_osc');
});

$('.pg13_knifes:nth-child(odd)').click(function(){
    $(this).toggleClass('knife_osc');
});
$('.pg13_knifes:nth-child(even)').click(function(){
    $(this).toggleClass('knife_osc_counter');
});      

});
$( '#pg13' ).live('pagehide',function(event, ui){
  
  audio_hide();

});
/*PAGE 14*/
$('#pg14').live('pageinit',function(){
   
    
});
$( '#pg14' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
        if(audio_file !='/audio/mmt_5.mp3'){
            stopAudio();
            playAudio('/audio/mmt_5.mp3');
        }
});
$( '#pg14' ).live('pagehide',function(event, ui){
    audio_hide();

});
/*PAGE 15*/
$('#pg15').live('pageinit',function(){        

});
$( '#pg15' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
    if(lang=="spanish"){
     playAudio('/audio/pg_15a.mp3');
    }else if(lang=="english"){
     playAudio('/audio/en_pg_15.mp3');
    }else{
    if(audio_file !='/audio/mmt_5.mp3'){
        stopAudio();
        playAudio('/audio/mmt_5.mp3');
    }
}
});
$( '#pg15' ).live('pagehide',function(event, ui){
    audio_hide();

});
/*PAGE 16*/
$('#pg16').live('pageinit',function(){           

});
$( '#pg16' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
    if(lang=="spanish"){
     playAudio('/audio/pg_16a.mp3');
    }else if(lang=="english"){
     playAudio('/audio/en_pg_16.mp3');
    }else{
    if(audio_file !='/audio/mmt_5.mp3'){
        stopAudio();
        playAudio('/audio/mmt_5.mp3');
    }
}

$('.legs').click(function(){
    $(this).animate( {'-webkit-animation-duration':'.3s'}, 'fast');
});

});
$( '#pg16' ).live('pagehide',function(event, ui){
    audio_hide();
});
/*PAGE 17*/
$('#pg17').live('pageinit',function(){

});
$( '#pg17' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
    if(lang=="spanish"){
     playAudio('/audio/pg_17a.mp3');
    }else if(lang=="english"){
     playAudio('/audio/en_pg_17.mp3');
    }else{
    if(audio_file !='/audio/mmt_6.mp3'){
        stopAudio();
        playAudio('/audio/mmt_6.mp3');
    }
}

});
$( '#pg17' ).live('pagehide',function(event, ui){
   audio_hide();
});
/*PAGE 18*/
$('#pg18').live('pageinit',function(){     

});
$( '#pg18' ).live('pageshow',function(event, ui){           
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
    if(lang=="spanish"){
     playAudio('/audio/pg_18a.mp3');
    }else if(lang=="english"){
     playAudio('/audio/en_pg_18.mp3');
    }else{
    if(audio_file !='/audio/mmt_7.mp3'){
        stopAudio();
        playAudio('/audio/mmt_7.mp3');
    }
}


});
$( '#pg18' ).live('pagehide',function(event, ui){
  audio_hide();

});
/*PAGE 19*/
$('#pg19').live('pageinit',function(){
    
  
    
});
$( '#pg19' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
   // if(lang!="spanish"){
        if(audio_file !='/audio/mmt_7.mp3'){
            stopAudio();
            playAudio('/audio/mmt_7.mp3');
        }
   // }

});
$( '#pg19' ).live('pagehide',function(event, ui){
    audio_hide();
});
/*PAGE MAIN*/
$('#main_page').live('pageinit',function(){
  
    
});
$( '#main_page' ).live('pageshow',function(event, ui){
    var lang = $("#lang").html();
    var audio_file = $("#audio_file").html();
    if(lang=="spanish"){
        playAudio('/audio/pg_intro.mp3');      
    }else if(lang=="english"){
        playAudio('/audio/en_pg_intro.mp3');                         
    }else{
        if(audio_file !='/audio/mmt_menu.mp3'){
         stopAudio();
         playAudio('/audio/mmt_menu.mp3');
     }
 }
});
$( '#main_page' ).live('pagehide',function(event, ui){
   audio_hide();
});




$('#thumb_index').live('pageinit',function(){
                     
                     
});
$( '#thumb_index' ).live('pageshow',function(event, ui){
        var lang = $("#lang").html();
        var audio_file = $("#audio_file").html();

        if(audio_file !='/audio/mmt_menu.mp3'){
                stopAudio();
                playAudio('/audio/mmt_menu.mp3');
        }

});
$( '#thumb_index' ).live('pagehide',function(event, ui){
            audio_hide();
 });






/*credits*/
$('#credits').live('pageinit',function(){
 
    
});
$( '#credits' ).live('pageshow',function(event, ui){
   var audio_file = $("#audio_file").html();
   if(audio_file !='/audio/mmt_credits.mp3'){
     stopAudio();
     playAudio('/audio/mmt_credits.mp3');   
     
 }
 
 
});
/* Menu Common*/
$('#menu_common').live('pageinit',function(){
                     
                     
 });
$( '#menu_common' ).live('pageshow',function(event, ui){

                         
      var audio_file = $("#audio_file").html();
      if(audio_file !='/audio/mmt_menu.mp3'){
                         stopAudio();
                         playAudio('/audio/mmt_menu.mp3');
                         
      }
  });
$( '#menu_common' ).live('pagehide',function(event, ui){
        stopAudio();
});


$('#next').live('pageinit',function(){
                       
                       
                       });
$( '#next' ).live('pageshow',function(event, ui){
                         
      var audio_file = $("#audio_file").html();
      if(audio_file !='/audio/mmt_principe.mp3'){
                         stopAudio();
                         playAudio('/audio/mmt_principe.mp3');
      }
  });
$( '#next' ).live('pagehide',function(event, ui){
    stopAudio();
});






$('#menu_principal').live('pageinit',function(){
                       
                       
 });
$( '#menu_principal' ).live('pageshow',function(event, ui){
    var audio_file = $("#audio_file").html();
        if(audio_file !='/audio/mmt_menu.mp3'){
                stopAudio();
                playAudio('/audio/mmt_menu.mp3');
                         
        }
});
$( '#menu_principal' ).live('pagehide',function(event, ui){
            stopAudio();
 });


$( '#credits' ).live('pagehide',function(event, ui){
      stopAudio();
});


function checkConnection() {
    var networkState = navigator.connection.type;
    
    var states = {};
    states[Connection.UNKNOWN]  = 'Unknown connection';
    states[Connection.ETHERNET] = 'Ethernet connection';
    states[Connection.WIFI]     = 'WiFi connection';
    states[Connection.CELL_2G]  = 'Cell 2G connection';
    states[Connection.CELL_3G]  = 'Cell 3G connection';
    states[Connection.CELL_4G]  = 'Cell 4G connection';
    states[Connection.NONE]     = 'No network connection';
    
    alert('Connection type: ' + states[networkState]);
}





function audio_hide(){
    return false;
    var lang = $("#lang").html();
    stopAudio();
    if(lang=="spanish" || lang=="english"){
        stopAudio();
    }
}