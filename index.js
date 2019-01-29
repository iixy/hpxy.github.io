var cover = document.getElementById("cover")
var navigationbar = document.getElementById("navigationbar")
var article = document.getElementById("allarticle")
var greeting = document.getElementById("greeting")

navigationbar.hidden = "true";
article.hidden = "true"
cover.style.color = "black";

greeting.onclick = function() { cover.style.backgroundColor = "white"; };