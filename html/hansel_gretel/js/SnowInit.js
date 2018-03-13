

	///////////////////////////////////////////////////////////////////////////////////
	//
	// JavaScript HTML5 Canvas Snow in 3D
	// http://sebleedelisle.com/2010/11/javascript-html5-canvas-snow-in-3d/
	//
	///////////////////////////////////////////////////////////////////////////////////
		
	var SCREEN_WIDTH = window.innerWidth;
	var SCREEN_HEIGHT = window.innerHeight;

	var container;
	var particle;

	var camera;
	var scene;
	var renderer;

	var mouseX = 0;
	var mouseY = 0;

	var windowHalfX = window.innerWidth / 2;
	var windowHalfY = window.innerHeight / 2;

	var particles = []; 
	var particleImage = new Image();
	particleImage.src = './img/ipad2/page2/flake2.png'; 

	setTimeout(
		function(){
			init();
		},200
	)

	setTimeout(
		function(){
			setInterval( loop, 2500 / 60 );
		},500
	)

	function init() {

		//container = document.createElement('div');
		//document.body.appendChild(container);

		camera = new THREE.Camera( 75, SCREEN_WIDTH / SCREEN_HEIGHT, 1, 10000 );
		camera.position.z = 1000;

		scene = new THREE.Scene();

		renderer = new THREE.CanvasRenderer();
		renderer.setSize(SCREEN_WIDTH, SCREEN_HEIGHT);

		//for (var i = 0; i < 500; i++) {
		for (var i = 0; i < 115; i++) {

			particle = new Particle3D( new THREE.ParticleBitmapMaterial( particleImage));
			particle.position.x = Math.random() * 2000 - 1000;
			particle.position.y = Math.random() * 2000 - 1000;
			particle.position.z = Math.random() * 2000 - 1000;
			particle.scale.x = particle.scale.y =  1;
			scene.addObject( particle );
			
			particles.push(particle); 
		}

		//container.appendChild( renderer.domElement );
		$('#pg1').append(renderer.domElement);

		document.addEventListener( 'mousemove', onDocumentMouseMove, false );
		document.addEventListener( 'touchstart', onDocumentTouchStart, false );
		document.addEventListener( 'touchmove', onDocumentTouchMove, false );
	}



	//

	function onDocumentMouseMove( event ) {

		mouseX = event.clientX - windowHalfX;
		mouseY = event.clientY - windowHalfY;
	}

	function onDocumentTouchStart( event ) {

		if ( event.touches.length == 1 ) {

			event.preventDefault();

			mouseX = event.touches[ 0 ].pageX - windowHalfX;
			mouseY = event.touches[ 0 ].pageY - windowHalfY;
		}
	}

	function onDocumentTouchMove( event ) {

		if ( event.touches.length == 1 ) {

			event.preventDefault();

			mouseX = event.touches[ 0 ].pageX - windowHalfX;
			mouseY = event.touches[ 0 ].pageY - windowHalfY;
		}
	}

	//

	function loop() {

		for(var i = 0; i<particles.length; i++)
		{
		
			var particle = particles[i]; 
			particle.update(); 
			
			with(particle.position)
			{
				if(y<-1000) y+=2000; 
				if(x>1000) x-=2000; 
				else if(x<-1000) x+=2000; 
				if(z>1000) z-=2000; 
				else if(z<-1000) z+=2000; 
			}				
		}

		camera.position.x += ( mouseX - camera.position.x ) * 0.05;
		camera.position.y += ( - mouseY - camera.position.y ) * 0.05;
		

		renderer.render( scene, camera );

		
	}

