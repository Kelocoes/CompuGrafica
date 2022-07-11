var x1 = 200;
var y1 = 100;

var x2 = 600;
var y2 = 100;

var x3 = 600;
var y3 = 350;

var x4 = 200;
var y4 = 350;

var viewport = [[x1, x2, x3, x4], [y1, y2, y3, y4]];

function productoPunto(p1, p2) {
	var res = 0;

	for (var i = 0; i < 2; i++) {
		res += p1[i] * p2[i];
	}

	return res;
}

function cyrusBeck(px1, py1, px2, py2) {
	var k = viewport[0].length;
	var d = [px2 - px1, py2 - py1];
	var f = viewport;
	var norma = [];
	var w;
	var n = viewport[0].length;
	var tl = 0;
	var tu = 1;
	var Ddotn, Wdotn, t;

	for (var i = 0; i < n; i++) {
		norma.push([viewport[1][(i) % n] - viewport[1][(i + 1) % n], [viewport[0][(i + 1) % n] - viewport[0][i % n]]]);
	}

	for (var i = 0; i < k; i++) {
		w = [px1 - f[0][i], py1 - f[1][i]];

		Ddotn = productoPunto(d, norma[i]);
		Wdotn = productoPunto(w, norma[i]);

		if (Ddotn != 0) {
			t = -Wdotn / Ddotn;

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

	var linea = [[], []];

	if (tl <= tu) {
		linea[0].push(px1 + (px2 - px1) * tl);
		linea[1].push(py1 + (py2 - py1) * tl);

		linea[0].push(px1 + (px2 - px1) * tu);
		linea[1].push(py1 + (py2 - py1) * tu);
	}
    return linea

}

function transcript(texto) {
    let construnct = texto.replace('[','');
    construnct = construnct.replace(']', '');
    construnct = construnct.replace(' ', '')

    construnct = construnct.split('(')
    let i = 0; 
    while (i < construnct.length)
    {
        if (construnct[i] == '') {
            construnct.splice(i, i+1);
            i = 0;
        } else {
            construnct[i] = construnct[i].replace(')', '');
            aux2 = construnct[i].split(',');
            for(let y = 0; y < aux2.length; y++) {
                aux2[y] = parseFloat(aux2[y]);
            }
            construnct[i] = aux2;
            i++; 
        }
    }
    return construnct;
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

function iniciar() {
    
    var canvas = document.getElementById('myCanvas')
    var ctx = canvas.getContext('2d');
    
    var figureText = document.formulario.figure.value; 
    var clipPolygon = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]; 
    var subjectPolygon = transcript(figureText);

    var lineaRecortada = cyrusBeck(subjectPolygon[0][0], subjectPolygon[0][1], subjectPolygon[1][0], subjectPolygon[1][1]);
    
    dibujar(ctx, clipPolygon, '#888','#ffc369');
    dibujar(ctx, subjectPolygon, '#888','#7f95e3');
    dibujar(ctx, [[lineaRecortada[0][0], lineaRecortada[1][0]],[lineaRecortada[0][1], lineaRecortada[1][1]]], '#000','#73ab67');
}

window.onload = function () {
    var canvas = document.getElementById('myCanvas')
    var ctx = canvas.getContext('2d');
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height)
    
}