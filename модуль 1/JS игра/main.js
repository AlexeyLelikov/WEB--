// Создаем Convas
let canv = document.getElementById("myCanvas");
ctx = canv.getContext("2d");

// Cоздаем объекты изображения
let plane = new Image();
let bg = new Image();
let building_up = new Image();
let building_bottom = new Image();

// Создаем объект звука
let fly = new Audio();
let score_audio = new Audio();

// Задаем источники звука
fly.src = "audio/wing.mp3";
score_audio.src = "audio/point.mp3" ;

// Задаем источники изобрадения
plane.src = "img/plane.png";
bg.src = "img/sky.jpg";
building_up.src = "img/building.png";
building_bottom.src = "img/building.png";
// Задаем размеры
width_plane = 70;
height_plane = 30;
width_bg = 1280;
height_bg = 720;
width_building_up = 50;
height_building_up = 500;
width_building_bottom = 50;
height_building_bottom = 500;

// координаты для героя
const xPos = 400;
let yPos = 400;


function moveUp(){
    yPos -= 25;
    fly.play();
}

document.addEventListener("click",moveUp);

let build_xy = [];

build_xy[0] = {
    x : canv.width,
    y : 0
}
// гравитация 
let g = 1.5;
let score = 0;
let gap = 150;


function draw(){
    ctx.drawImage(bg,0,0,width_bg,height_bg);
    
    for (let i = 0; i < build_xy.length; i++)
    {
        ctx.drawImage(building_up,build_xy[i].x,build_xy[i].y,width_building_up,height_building_up);
        ctx.drawImage(building_bottom,build_xy[i].x,build_xy[i].y + height_building_up + gap,width_building_bottom,height_building_bottom);

        
        build_xy[i].x--;

        if (build_xy[i].x == 800){
            build_xy.push({x : canv.width,
                           y : Math.floor(Math.random() * height_building_up) - height_building_up});
        }
        // Отслеживание прикосновений 
        if (xPos + width_plane >= build_xy[i].x &&
            xPos <= build_xy[i].x + width_building_up &&
            (yPos <= build_xy[i].y + height_building_up || 
            yPos + height_plane >= build_xy[i].y + height_building_up + gap) ||
            yPos + height_plane >= height_bg )
        {
            location.reload();
        }
        // Счет
        if (build_xy[i].x == xPos - width_building_up)
        {
            score++;
            score_audio.play();
        }
    }

    yPos = yPos + g;
    ctx.drawImage(plane,xPos,yPos,width_plane,height_plane);

    ctx.fillStyle = "#000";
    ctx.font = "30px Verdana";
    ctx.fillText("Cчет: " + score,30, height_bg - 40);

    requestAnimationFrame(draw);
}
bg.onload = draw;


