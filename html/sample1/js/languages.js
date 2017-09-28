$('#cover').live('swipeleft swiperight',function(){
                
                    $.mobile.changePage("#main_page",  { transition: "slide"});
                    event.preventDefault();
                    
});
$('#home').live('swipeleft swiperight',function(){
                
                    $.mobile.changePage("#menu_principal",  { transition: "slide"});
                    event.preventDefault();
                    
}); 
$('#menu_principal').live('taphold',function(){

                // $.mobile.changePage("#main_page", "slidedown");
              //  event.preventDefault();
                          
});

$('#spanish_btn').live('tap',function(){
                      
                      
                       language('spanish');
                       
});
$('#english_btn').live('tap',function(){
                    
                      // $.mobile.loadingMessage = 'Loading...';
                       //$.mobile.loadingMessageTextVisible = true;

                       language('english');
                       
});
$('#french_btn').live('tap',function(){

                       language('french');
                       
});
$('#german_btn').live('tap',function(){

                       language('german');
});
$('#portuguese_btn').live('tap',function(){
                      language('portuguese');
 });
$('#gramophone_btn').live('tap',function(){
                          mute();
            
});
$('#facebook_btn').live('tap',function(){
        alert('facebook');
}); 
$('#twitter_btn').live('tap',function(){
     alert('twitter');

}); 
$('#rank_btn').live('tap',function(){ 
   alert('rank');

}); 
$('#info_btn').live('tap',function(){
   $.mobile.changePage("#info_page", { transition: "slideup"});

}); 
$('#mainmenu_btn').live('tap',function(){
  $.mobile.changePage("#menu_principal", { transition: "slide"});

}); 


$('#in_cover').live('tap',function(){
                            reset_book();
                            $.mobile.changePage("#home", { transition: "slide"});
});
$('#startover_common').live('tap',function(){
     reset_book();
     $.mobile.changePage("#home", { transition: "slide"});
});

$('#startover_txt').live('tap',function(){
      reset_book();
      $.mobile.changePage("#home", { transition: "slide"});
});



$('#mainmenu_btn').live('vmouseove',function(){
    $('#menu_c_cookie').removeClass().addClass('mc_main_on');  
});

$('#common_mute').live('tap',function(){
      mute();
});
$('#mutecommon_txt').live('tap',function(){
      mute();
});

//btn_mute_principal
$('.btn_mute_principal').live('tap',function(){
    mute();
                          
});

$('.hand_nav_swape').live('swipe',function(){
                          
        var href = $(this).attr('href');
        var direction = $(this).attr('data-direction');
        var transition = $(this).attr('data-transition')

        $.mobile.changePage(href, { transition: transition, direction: direction});
        // data-direction="reverse" data-transition="slide"
                              
});

$('#pglink_rank').live('tap',function(){
var lang = $("#lang").html();
if(lang=="spanish"){
     window.open("https://itunes.apple.com/es/app/hansel-gretel-miel-producciones/id586321565");
     return false;
  }else{
      window.open("https://itunes.apple.com/us/app/hansel-gretel-miel-producciones/id586321565");
      return false;
 }
                       
 });



function mute(){
        //id="common_mute" class="txt common_mute_off"
        var sound =  $("#sound").html();
            if( sound =='on'){// make in off
                 $('#common_mute').removeClass().addClass('common_mute_off txt');
                 $('.globo_menu').addClass('hidden');
                  
                 $("#sound").html('off');
                  stopAudio();// just in case it was running
            }else{
                $('#common_mute').removeClass().addClass('common_mute_on txt');
                $('.globo_menu').removeClass('hidden');
                  
                $("#sound").html('on');
                 playAudio('/audio/mmt_menu.mp3');
            }

}
function reset_book(){
  stopAudio();
  $("body").find("*").removeAttr('style');
    /*reset();
    $('#movie').get(0).currentTime = 0;
    $('#movie').get(0).play();
     */
    var myvideoplayer = $('#movie');
    var myvid = $('#movie').get(0);
        myvid.currentTime = 0;
        myvid.play();
    

}
function language(lang){
    /*
     this should be more pretty
     */
     $("#lang").html(lang);
   // $('#menu_p_cookie').removeClass().addClass('mp_'+lang);
    $("div[class*=_btn_on]").each(function () {
        this.className = this.className.replace("_on", "_off");
    });
    $("div[id*="+lang+"_btn]").each(function () {
        this.className = this.className.replace("_off", "_on");
           
    });
    $("div[class*=_txt_spanish]").each(function () {
          this.className = this.className.replace("spanish", lang);
    });
    $("div[class*=_txt_english]").each(function () {
          this.className = this.className.replace("english", lang);
    });
    $("div[class*=_txt_french]").each(function () {
         this.className = this.className.replace("french", lang);
     });
    $("div[class*=_txt_german]").each(function () {
         this.className = this.className.replace("german", lang);
     });
    $("div[class*=_txt_portuguese]").each(function () {
        this.className = this.className.replace("portuguese", lang);
    });

}