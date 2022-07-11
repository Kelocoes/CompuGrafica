function CohenShuterland(figura, viewport) {

    var x1 = figura[0][0];
    var y1 = figura[0][1];
    var x2 = figura[1][0];
    var y2 = figura[1][1];
    var code1 = CodeGenerator([x1,y1], viewport);
    var code2 = CodeGenerator([x2,y2], viewport);
    var LEFT = 1;
    var INSIDE = 0;
    var RIGHT = 2;
    var TOP = 8;
    var BOTTOM = 4;
    var x_max = viewport[1][0];
    var y_max = viewport[1][1];
    var x_min = viewport[0][0];
    var y_min = viewport[0][1];

    var salida = [];

    while (true) {
        if (!(code1 || code2)) {
            salida = [[x1,y1],[x2,y2]];
            break;
        } else if (code1 & code2) {
            salida = [];
            break;
        } else {
            var newX;
            var newY;
            var newCode = code2;

            if (code1 > code2) {
                newCode = code1
            }

            if (newCode & TOP) {
				newX = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1);
				newY = y_max;
			} else if (newCode & BOTTOM) {
				newX = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1);
				newY = y_min;
			} else if (newCode & RIGHT) {
				newX = x_max;
                newY = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1);
			} else if (newCode & LEFT) { 
				newX = x_min;
                newY = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1);
			}

            if (newCode == code1) {
                x1 = newX;
                y1 = newY;
                code1 = CodeGenerator([x1,y1], viewport);
            } else {
                x2 = newX;
                y2 = newY;
                code2 = CodeGenerator([x2,y2], viewport);
            }
        }
    }

    return salida
}

function CodeGenerator(codelist, viewport) {
        
    var LEFT = 1;
    var INSIDE = 0;
    var RIGHT = 2;
    var TOP = 8;
    var BOTTOM = 4;
    
    var x_max = viewport[1][0];
    var y_max = viewport[1][1];
    var x_min = viewport[0][0];
    var y_min = viewport[0][1];
    var code;
    code = INSIDE;

    if (codelist[0] < x_min) {
        code = LEFT;
    }else if (codelist[0]> x_max) {
        code = RIGHT;
    } 
    if (codelist[1] < y_min) {
        code = BOTTOM;
    }else if (codelist[1] > y_max) {
        code = TOP;
    } 

    return code
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
                if (Number.isNaN(aux2[y])) {
                    aux2[y].pop();
                } else {
                    aux2[y] = parseFloat(aux2[y]);
                }
               
            }
            construnct[i] = aux2;
            i++; 
        }
    }
    return construnct;
}

function iniciar() {
    var canvas = document.getElementById('myCanvas')
    var ctx = canvas.getContext('2d');
    
    var viewportText = document.formulario.vertView.value;
    var figureText = document.formulario.figure.value; 
    
    var subjectPolygon = transcript(figureText);
    var viewport = transcript(viewportText); 

    
    var figuraRecortada = CohenShuterland(subjectPolygon, viewport);
    
    var clipPolygon = [[viewport[0][0],viewport[0][1]],[viewport[0][1],viewport[1][1]],[viewport[1][0],viewport[1][1]],[viewport[1][0],viewport[0][1]]]
    
    dibujar(ctx, clipPolygon, '#888','#ffc369');
    dibujar(ctx, subjectPolygon, '#888','#7f95e3');
    dibujar(ctx, figuraRecortada, '#000','#73ab67');
}

window.onload = function () {
    var canvas = document.getElementById('myCanvas')
    var ctx = canvas.getContext('2d');
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height)
    
}