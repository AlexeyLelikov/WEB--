var canv = document.getElementById("myCanvas");
var contx = canv.getContext("2d");
contx.fillStyle = "#008B8B";
contx.fillRect(200,200,100,50);
contx.strokeRect(150,150,30,50);
contx.beginPath()
contx.arc(100,100,50,0,1.5*Math.PI);
contx.stroke();