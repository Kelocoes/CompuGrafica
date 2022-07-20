/*HOW TO USE :

				Open this file in a modern browser (firefox version 26 and above)
				Click anywhere on the diagram to clip a line
				To see console log, press ctr+shift+k			
			*/

//global variables to hold the end points of lines
//start and end are arrays that contains 2 values
//That is, start and end are always arrays of length 2
var start = [];
var end = [];

//Stack that keep tracks of the end points.
var stack = [];

//viewport is a square of vertices a, b, c and d
var ax = 200;
var ay = 200;

var bx = 500;
var by = 200;

var cx = 500;
var cy = 500;

var dx = 200;
var dy = 500;

var clipper_polygon = [[ax, bx, cx, dx], [ay, by, cy, dy]];

//min max values required to create the outcodes
var xmin = ax;
var xmax = cx;
var ymin = ay;
var ymax = cy;

//Boilerplate code. Required to access the html5 canvas
var canvas = document.getElementById('myCanvas');
var context = canvas.getContext("2d");

//Google "html5 compositing"
context.globalCompositeOperation = 'source-over';

//input coordenates
var x1 = "";
var y1 = "";

var x2 = "";
var y2 = "";



//This is an event listener
//The function inside fires only when the mouse is clicked
canvas.addEventListener('mousedown', function (evt) {

	if (stack.length > 0)
		end_points = stack.pop();
	console.log('end points of line : ' + end_points[0] + 'to' + end_points[1]);
	cyrusBeck(end_points[0][0], end_points[0][1], end_points[1][0], end_points[1][1]);
});

function dotProduct(p1, p2) {
	var res = 0;

	for (var i = 0; i < 2; i++) {
		res += p1[i] * p2[i];
	}

	return res;
}


function cyrusBeck(x1, y1, x2, y2) {
	console.log(x1);
	console.log(y1);
	console.log(x2);
	console.log(y2);
	var k = clipper_polygon[0].length;
	var d = [x2 - x1, y2 - y1];
	var f = clipper_polygon;
	var normals = [];
	var w, mi, ni;
	mi = encontrarPendientes();
	var n = clipper_polygon[0].length;
	var points = [];
	var tl = 0;
	var tu = 1;
	var Ddotn, Wdotn, t;

	//calcular las normales
	for (var i = 0; i < n; i++) {
		normals.push([clipper_polygon[1][(i) % n] - clipper_polygon[1][(i + 1) % n], [clipper_polygon[0][(i + 1) % n] - clipper_polygon[0][i % n]]]);
	}

	for (var i = 0; i < k; i++) {
		w = [x1 - f[0][i], y1 - f[1][i]];

		Ddotn = dotProduct(d, normals[i]);
		Wdotn = dotProduct(w, normals[i]);

		if (Ddotn != 0) {
			t = -Wdotn / Ddotn;
			console.log(t);

			if (Ddotn > 0) {
				if (t > 1) {
					return;
				}
				else {
					tl = Math.max(t, tl);
				}
			}
			else {
				if (t < 0) {
					return;
				}
				else {
					tu = Math.min(t, tu);
				}
			}
		}
		else {
			if (Wdotn < 0) {
				return;
			}
		}
	}

	var newLine = [[], []];

	if (tl <= tu) {
		newLine[0].push(x1 + (x2 - x1) * tl);
		newLine[1].push(y1 + (y2 - y1) * tl);

		newLine[0].push(x1 + (x2 - x1) * tu);
		newLine[1].push(y1 + (y2 - y1) * tu);
	}

	console.log(newLine);
	return newLine;


}

function encontrarPendientes() {
	var mi;
	var m = [];
	for (var i; i < clipper_polygon[0].length; i++) {
		var k = (i + 1) % poligonoE[0].length;

		mi = (clipper_polygon[1][k] - polyCoordinates[1][i].y) / (polyCoordinates[k].x - polyCoordinates[i].x);
		m.push(mi);
		if (polyCoordinates[0][k] == polyCoordinates[0][i]) {
			m.push(null);
		}
	}
	return m;
}


function x_intersect(x1, y1, x2, y2,
	x3, y3, x4, y4) {
	var num = (x1 * y2 - y1 * x2) * (x3 - x4) -
		(x1 - x2) * (x3 * y4 - y3 * x4);
	var den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
	return num / den;
}

function y_intersect(x1, y1, x2, y2,
	x3, y3, x4, y4) {
	var num = (x1 * y2 - y1 * x2) * (y3 - y4) -
		(y1 - y2) * (x3 * y4 - y3 * x4);
	var den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4);
	return num / den;
}

function draw_line1() {
	start = [300, 300];
	end = [400, 400];

	stack.push([start, end]);

	//drawing the line
	context.beginPath();
	context.moveTo(start[0], start[1]);
	context.lineTo(end[0], end[1]);

	//setting stroke color in RGB. Here R=ff, G=0, B=0 to get full red
	context.strokeStyle = "#000";
	context.lineWdith = 1;
	context.stroke();
}

function draw_line2() {
	start = [220, 100];
	end = [300, 150];

	stack.push([start, end]);

	context.beginPath();
	context.moveTo(start[0], start[1]);
	context.lineTo(end[0], end[1]);

	context.strokeStyle = "#000";
	context.lineWidth = 1;
	context.stroke();
}

//Draw a line with one end point outside and one endpoint inside the viewport
function draw_line3() {
	start = [150, 300];
	end = [300, 280];

	stack.push([start, end]);

	context.beginPath();
	context.moveTo(start[0], start[1]);
	context.lineTo(end[0], end[1]);

	context.strokeStyle = "#000";
	context.lineWidth = 1;
	context.stroke();
}

//Draw a line that cuts the viewport at 2 locations, with both endpoints outside
function draw_line4() {
	start = [150, 250];
	end = [550, 400];

	stack.push([start, end]);

	context.beginPath();
	context.moveTo(start[0], start[1]);
	context.lineTo(end[0], end[1]);

	context.strokeStyle = "#000";
	context.lineWidth = 1;
	context.stroke();
}



function draw_line5() {
	start = [200, 268.75];
	end = [500, 381.25];

	stack.push([start, end]);

	context.beginPath();
	context.moveTo(start[0], start[1]);
	context.lineTo(end[0], end[1]);

	context.strokeStyle = "#000000";
	context.lineWidth = 1;
	context.stroke();
}


function dibujar(ctx, pol, strStyle, fillStyle) {
    ctx.strokeStyle = strStyle; 
    ctx.fillStyle = fillStyle; 
    ctx.beginPath(); 
    ctx.moveTo(pol[0][0], pol[0][1]); 
    for(var i = 1; i < pol.length; i++) {
        ctx.lineTo(pol[i][0], pol[i][1]);
    }
    ctx.lineTo(pol[0][0], pol[0][1]); 
    ctx.fill();
    ctx.stroke(); 
    ctx.closePath();  
}

window.onload = function () {
    var canvas = document.getElementById('myCanvas')
    var ctx = canvas.getContext('2d');
	ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height)

	dibujar(ctx, [[ax, ay],[bx, by],[cx, cy], [dx, dy]], '#888', '#ffc369')
	dibujar(ctx, [[150, 250],[550, 400]], '#888', '#ffc369')
	var dibujado = cyrusBeck(150, 250, 550, 400)
	dibujar(ctx, [[dibujado[0][0], dibujado[1][0]],[dibujado[0][1], dibujado[1][1]]], '#000', '#ffc369')
	console.log(dibujado, 'aqui')
}


//The next 4 blocks draw our viewport
//drawing line x=200, of length 300 units (pixels)
context.beginPath();
context.moveTo(ax, ay);
context.lineTo(bx, by);
context.stroke();

//drawing line y=200, length 300 pixels
context.beginPath();
context.moveTo(bx, by);
context.lineTo(cx, cy);
context.stroke();

//drawing line x=500
context.beginPath();
context.moveTo(cx, cy);
context.lineTo(dx, dy);
context.stroke();

//drawing line y=500
context.beginPath();
context.moveTo(dx, dy);
context.lineTo(ax, ay);
context.stroke();
