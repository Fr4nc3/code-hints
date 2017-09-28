$(function() {

  $.fn.rotateObject = function(options) {
    //pass turn = true to move clockwise
    var defaults = {
                animateTiming: 'cubic-bezier(0.50,0,1,1)',
                degree: 45,
                duration: '7s infinite',
                interval: 4000
            };
             
    var options = $.extend(defaults, options);

    return this.each(function(){
      var o = options;
      var obj = $(this);
      setInterval(
              function () {
                obj.animate({  borderSpacing: o.degree }, {
                                        step: function(now,fx) {
                                        if(o.turn == true){
                                          now = now * -1; //go the oposite way
                                        }
                                        $(this).css({'-webkit-transform':'rotate('+now+'deg)',
                                                    '-webkit-transition':'width'});
                                        }, duration:o.duration }, o.animateTiming);
                    },
                o.interval
              );
    });
  };
  
$(' .draggable, .pg5_rat, .draggables20, .drag-cookies, #pg5 .pg5_spin,.pg8_gretel, .pg8_hansel, #pg8 .birds, #pg13 .objects, .pg18_goldencoin,  #pg4 .pg4_rock1, #pg4 .pg4_rock2')
  .draggable({ containment: $(this).parent() });


$('.pg3_bird').click(function(){
  $(this).addClass('pg3_bird_translate');
});


  

});

