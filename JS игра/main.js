let canv = document.getElementById("myCanvas");
ctx = canv.getContext("2d"); 
let plane = new Image();
let bg = new Image();
let building = new Image();
plane.src = "img/plane.png";
bg.src = "img/sky.jpg";
building.src = "img/building.png";
width_plane = 168;
height_plane = 64;
width_bg = 1280;
height_bg = 720;

let xPos = 200;
let yPos = 200;
function draw(){
    ctx.drawImage(bg,0,0,width_bg,height_bg);
    ctx.drawImage(plane,xPos,yPos,width_plane,height_plane);
}
bg.onload = draw;

function moveUp(){
    yPos -= 25;
    draw();
}

document.addEventListener("click",moveUp);

