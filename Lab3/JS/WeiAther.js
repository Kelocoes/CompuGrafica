function WeitherAtherton(figuraEdit) {
    var polygon = figuraEdit;

    function ordenar(polygon) {
        if (polygon[polygon.length-1][2] != 1) {
            polygon.unshift(polygon[polygon.length-1]); 
            polygon.pop(); 
            ordenar(polygon); 
        } 
    }

    ordenar(polygon); 

    function sacarPedazoFigura(polygon) {
        var a = 0, b = 0; 
        var eys = [], poligonosVisibles = [];

        for(let posPareja = 0; posPareja < polygon.length; posPareja++) {
            if (polygon[posPareja][2] == 0) {
                a = a + posPareja; 
            }
            if (polygon[posPareja][2] == 1 && a > 0) {
                b = b + posPareja; 

                // sacando los puntos entre la entrada (a) y la salida (b)
                while (a <= b) {
                    eys.push(polygon[a]);
                    a = a + 1;
                }
                a = 0; 
                b = 0; 
                poligonosVisibles.push(eys); 
                eys = []
            }
        }
        return poligonosVisibles; 
    }
    var resultado = sacarPedazoFigura(polygon); 
    return resultado
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
                aux2[y] = parseFloat(aux2[y]);
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
    var clipPolygon = transcript(viewportText); 
    var figurasCortadas = WeitherAtherton(subjectPolygon); 
    console.log(figurasCortadas)
    dibujar(ctx, clipPolygon, '#888','#ffc369');
    dibujar(ctx, subjectPolygon, '#888','#7f95e3');

    for(let i = 0; i < figurasCortadas.length; i++) {
        dibujar(ctx, figurasCortadas[i], '#000')
    }
}

window.onload = function () {
    var canvas = document.getElementById('myCanvas')
    var ctx = canvas.getContext('2d');
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height)
}
