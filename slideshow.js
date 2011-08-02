$(function() {
	$.getJSON(
		"slideshow.json",
		function(data) {
			console.log(data);
			var slideshow = $("<div>").addClass("slideshow");
			$("#slide").tmpl(data.images).appendTo(slideshow);
			$("body").empty().css("cursor", "none");
			slideshow.appendTo("body").cycle({
				speed: 10 * 1000,	//Rychlost přechodu
				timeout: 60 * 1000,	//Jak dlouho má být vidět snímek
				slideResize: 0,
				height: $(window).height(),
				width: $(window).width(),
				random: 1,
				before: function() {
						$("blockquote", this).text(data.quotes[Math.floor(Math.random() * data.quotes.length)]);
					}
			});
		}
	);
});
