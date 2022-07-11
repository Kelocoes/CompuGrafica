function clippingKevin(figura, viewport) {
    
    var c1, c2, s1, s2; 

    function dentro(p){
        var R = (c2[0] - c1[0]) * (p[1] - c1[1]) > (c2[1] - c1[1]) * (p[0] - c1[0]); 
        return R; 
    }

    function interseccion() {
        var dc = [ c1[0] - c2[0], c1[1] - c2[1] ],
            dp = [ s1[0] - s2[0], s1[1] - s2[1] ],
            n1 = c1[0] * c2[1] - c1[1] * c2[0],
            n2 = s1[0] * s2[1] - s1[1] * s2[0],
            n3 = 1.0 / (dc[0] * dp[1] - dc[1] * dp[0]);
        return [(n1*dp[0] - n2*dc[0]) * n3, (n1*dp[1] - n2*dc[1]) * n3];
    }

    var salida = figura; 
    // Por cada lado del viewport, deberá hacerse la comparación con cada lado de la figura dada, y así saber cuales puntos están afuera o adentro
    var c1 = viewport[viewport.length-1]; // Se toma el punto de inicio del lado del viewport
    for(let i = 0; i < viewport.length; i++) {
        var c2 = viewport[i]; //Se toma el punto final del lado del viewport 
        var auxCopy = salida; //Copia de la salida para utilizarla como iterador
        salida = []; // Se reinicia el arreglo de la salida
        
        var s1 = auxCopy[auxCopy.length-1];// Se toma el punto de inicio del lado de la figura recortada
        for(let j = 0; j < auxCopy.length; j++) { // Iterar por cada lado de la figura que está siendo recortada    
            var s2 = auxCopy[j]; // Se toma el punto final del lado de la figura recortada
            if (dentro(s2)) {// Se pregunta si el punto final del lado actual (figura) está dentro del área marcada por el lado del viewport
                if (!dentro(s1)) { // Se pregunta si el punto inicial del lado actual (figura) está fuera del área marcada por el lado del viewport
                    salida.push(interseccion()); // Nuevo punto de la figura recortada respecto a la intersección 
                }
                salida.push(s2); // Nuevo punto de la figura recortada, es el punto final del lado actual
            } 
            else if (dentro(s1)) { // Se pregunta si el punto inicial del lado actual (figura) está dentro del área marcada por el lado del viewport
                salida.push(interseccion());
            }
            s1 = s2; 
            
        }
        c1 = c2; 
    }   
    console.log(salida); 
    return salida; 
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
    
    var figuraRecortada = clippingKevin(subjectPolygon, clipPolygon);
    
    dibujar(ctx, clipPolygon, '#888','#ffc369');
    dibujar(ctx, subjectPolygon, '#888','#7f95e3');
    dibujar(ctx, figuraRecortada, '#000','#73ab67');
    
   clippingKevin(subjectPolygon, clipPolygon); 
}

window.onload = function () {
    var canvas = document.getElementById('myCanvas')
    var ctx = canvas.getContext('2d');
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height)
    
}