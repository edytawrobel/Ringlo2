$(document).ready(function () {
	google.maps.event.addDomListener(window, 'load', init_map);
	popup();
	social();
});

// Init Google mpas
function init_map() {
	var var_location = new google.maps.LatLng(51.461387,-0.115185);
	var var_mapoptions = {
	  center: var_location,
	  zoom: 14
	};
	var var_marker = new google.maps.Marker({
	    position: var_location,
	    map: var_map,
	    title:"Brixton"});
	var var_map = new google.maps.Map(document.getElementById("map-container"),
	    var_mapoptions);
	var_marker.setMap(var_map); 
}


// Popup
function popup() {
	$('#getDiscount').on("click", function () {
		var $background = $('<div class="popup-background"></div>');
		$('body').append($background);
		$background.hide().fadeIn(600, function () {
			setTimeout(function () {
				showPopup();
			}, 100);
		});
	});
}

// Show Popup
function showPopup () {
	var $background = $('.popup-background');

	// Content
	var $content = $([
		'<div class="popup-body">',
			'<div class="popup-thankyou"></div>',
			'<div class="popup-close"></div>',
			'<input type="text" placeholder="Your email address...">',
			'<div class="popup-submit"></div>',
			'<div class="popup-ignore"></div>',
		'</div>'
	].join(""));

	$('body').append($content);
	$content.hide().fadeIn(600);

	// Close
	$('body').on("click", ".popup-background, .popup-ignore, .popup-close", function () {
		$content.fadeOut(600);
		$background.fadeOut(600);
	});

	// Submit
	$content.find(".popup-submit").on("click", function () {
		$content.find("input").hide();
		$content.find(".popup-thankyou").show(600, function () {
			setTimeout(function () {
				$content.fadeOut(600);
				$background.fadeOut(600);
			}, 3000);
		});

	});
}

// Social
function social () {
	var $content = $([
		'<div class="social-wrapper">',
			'<div class="social-element facebook"></div>',
			'<div class="social-element linkedin"></div>',
			'<div class="social-element twitter"></div>',
			'<div class="social-element email"></div>',
			'<div class="social-element dots"></div>',
		'</div>'
	].join(""));

	$('body').append($content);

	var $height = $(window).height();
	var dimension = ($height - $content.height()) / 2;
	$content.css("top", dimension);

	setTimeout(function () {
		$content.animate({
		    marginLeft: '10px'
		}, 1000);
	}, 2000); 

	$content.find(".social-element.dots").on("click", function () {
		$content.animate({
		    marginLeft: '-75px'
		}, 1000); 
	});
}







