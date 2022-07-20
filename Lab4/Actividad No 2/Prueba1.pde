
PShape bicycle;
PShape bicycle1;
  
public void setup() {
  size(630, 360, P3D);
    
  bicycle = loadShape("bicycle.obj");
  bicycle.rotateX(PI/2.0);
  bicycle.rotateY(PI/2.0);
  bicycle.scale(7);//Factor de escalado un 700%
  bicycle.translate((width/2)-150,(height/2)+100,0);
  
  bicycle1 = loadShape("bicycle.obj");
  bicycle1.rotateX(PI/2.0);
  bicycle1.rotateY(PI/2.0);
  bicycle1.scale(7);//Factor de escalado un 700%
  bicycle1.translate((width/2)+150,(height/2)+100,0);
}

public void draw() {
  background(0);
  lights();
  shape(bicycle);
  shape(bicycle1);
  println(mouseX,mouseY);
  
}
