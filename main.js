inputs = document.querySelectorAll('input');

for (let i=0; i < inputs.length; i++) {
  inputs[i].oninput = () => {
    addInputData(inputs);
    draw();
  }
}

function addInputData(node_list) {
  inputDate = [];

  for (let i=0; i < node_list.length-1; i=i+2) {
    if (+node_list[i].value > 0 && +node_list[i+1].value > 0) {
      inputDate.push([+node_list[i].value, +node_list[i+1].value]);
    }
  }
  console.log(inputDate);
}

let canvas = document.getElementById('c1');
ctx = canvas.getContext('2d');

function draw() {
  ctx.clearRect(0, 0, 1000, 500);
  ctx.strokeStyle = 'red';
  ctx.lineWidth = '5';
  ctx.beginPath();
  ctx.moveTo(500, 250);
  let x = 0;
  let y = 0;
  for (let i=0; i < inputDate.length; i++) {
    x = inputDate[i][0];
    y = inputDate[i][1];
    ctx.lineTo(x, y);
  }
  // ctx.closePath();
  ctx.stroke();
  // ctx.closePath();

}



// // прямоугольник с заливкой
// ctx.fillStyle = 'red';
// ctx.fillRect(100, 50, 150, 75);
// ctx.fillStyle = 'blue';
// ctx.fillRect(150, 100, 100, 50);
//
// // стёрка
// ctx.clearRect(0, 0, 400, 200);
//
// // прямоугольник с контуром
// ctx.strokeStyle = 'green';
// ctx.lineWidth = '10';
// ctx.rect(50 ,10, 100, 100);
// ctx.stroke();
// ctx.fillStyle = 'orange';
// ctx.fill();
// ctx.beginPath();
// ctx.strokeStyle = 'red';
// ctx.lineWidth = '5';

// ctx.moveTo(0, 0);
// ctx.lineTo(150, 150);
// ctx.stroke();

// ctx.lineTo(300, 50);
// ctx.stroke();

// ctx.beginPath();
// ctx.strokeStyle = 'blue';
// ctx.lineWidth = '20';
// ctx.moveTo(200, 50);
// ctx.lineTo(300, 50);
// ctx.lineCap = "round";
// ctx.stroke();

// рисование без нажатия
// canvas.onmousemove = (event) => {
//   let x = event.offsetX;
//   let y = event.offsetY;
//   ctx.fillRect(x-5, y-5, 10, 10);
// };

// рисование с нажатие
// canvas.onmousedown = (event) => {
//   let x = event.offsetX;
//   let y = event.offsetY;
//   ctx.fillRect(x-5, y-5, 10, 10);
// };

// // рисование при нажатие
// canvas.onmousedown = (event) => {
//   canvas.onmousemove = (event) => {
//     let x = event.offsetX;
//     let y = event.offsetY;
//     ctx.fillRect(x-5, y-5, 10, 10);
//   };
//   canvas.onmouseup = () => {
//     canvas.onmousemove = null;
//   }
// };

// // Рисовалка
// let myColor = 'red';
//
// document.getElementById('color').oninput = function()  {
//   myColor = this.value;
// };
// // рисование при нажатие
// canvas.onmousedown = (event) => {
//   canvas.onmousemove = (event) => {
//     let x = event.offsetX;
//     let y = event.offsetY;
//     ctx.fillRect(x-5, y-5, 10, 10);
//     ctx.fillStyle = myColor;
//     ctx.fill();
//   };
//   canvas.onmouseup = () => {
//     canvas.onmousemove = null;
//   }
// };

// окружность
// let pi = Math.PI;
// ctx.beginPath();
// ctx.lineWidth = 5;
// ctx.strokeStyle = 'red';
// ctx.fillStyle = 'yellow';
// ctx.arc(150, 100, 75, 0, 2*pi, true);
// ctx.stroke();
// ctx.fill();
//
// ctx.beginPath();
// ctx.lineWidth = 5;
// ctx.strokeStyle = 'greeb';
// ctx.fillStyle = 'pink';
// ctx.arc(270, 100, 75, 0, 2*pi, true);
// ctx.stroke();
// ctx.fill();
// ctx.clearRect(0,0,400,200);
//
// canvas.onmousemove = (e) => {
//   let x = e.offsetX;
//   let y = e.offsetY;
//
//   ctx.clearRect(0,0,400,200);
//   ctx.beginPath();
//
//   let radius = Math.pow(Math.pow(x-200, 2)+Math.pow(y-100,2), 0.5);
//   ctx.arc(200, 100, radius, 0, 2*pi, false);
//   ctx.stroke();
//   ctx.fill();
// };

