inputs = document.querySelectorAll('input');
output = document.getElementById('0');

for (let i=0; i < inputs.length; i++) {
  inputs[i].oninput = () => {
    const inputDate = addInputData(inputs);
    const coordinates = CoordinatesFromInput(inputDate);
    toDraw(coordinates);
    const area = countArea(coordinates);
    insertArea(area);
  }
}

function addInputData(node_list) {
  let inputDate = [];

  for (let i=0; i < node_list.length-1; i=i+2) {
    if (+node_list[i].value > 0 && +node_list[i+1].value > 0) {
      inputDate.push([+node_list[i].value, +node_list[i+1].value]);
    }
  }
  console.log(inputDate);
  return inputDate;
}

let canvas = document.getElementById('c1');
ctx = canvas.getContext('2d');


function CoordinatesFromInput(inputData) {
  const pi = Math.PI;
  let coordinate = [[500, 250]];

  inputData.unshift([500, 250]);

  for (let i=1; i < inputData.length; i++) {
    let expression = inputData[i][0] * (pi / 180);

    let x = Math.cos(expression) * inputData[i][1];
    let y = Math.sin(expression) * inputData[i][1];

    console.log(`coordinatesFromInput-> x=${x}`);
    console.log(`coordinatesFromInput-> y=${y}`);

    x += coordinate[i-1][0];
    y += coordinate[i-1][1];

    coordinate.push([x, y]);
  }
  console.log(`coordinatesFromInput-> ${coordinate}`);
  return coordinate;
}

function toDraw(coordinates) {
  ctx.clearRect(0, 0, 1000, 500);
  ctx.strokeStyle = 'red';
  ctx.lineWidth = '5';

  ctx.beginPath();
  ctx.moveTo(coordinates[0][0], coordinates[0][1]);
  for (let i=0; i < coordinates.length; i++) {
    ctx.lineTo(coordinates[i][0], coordinates[i][1]);
  }
  ctx.stroke();
}

function countArea(coordinates) {
  let multySumm = 0;

  for (let i=1; i < coordinates.length; i++) {
    console.log(`countArea-> coorx=${coordinates[i][0]}`);
    console.log(`countArea-> coorx=${coordinates[i][1]}`);

    let x = coordinates[i][0];
    let y = coordinates[i][1];

    x = (coordinates[i-1][0] + x) / 2;
    y = coordinates[i-1][1] - y;
    multySumm += (x * y);

    console.log(`countArea-> x=${x} y=${y}`);
    console.log(`countArea-> multy=${multySumm}`);
  }
  let result = Math.abs(multySumm / 10000);

  return result.toFixed(2)
}

function insertArea(area) {
  output.innerText = area;
}
