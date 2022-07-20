
PShape mesa;
  
public void setup() {
  size(630, 360, P3D);
    
  mesa = loadShape("mesa.obj");
  mesa.rotateZ(PI);
  mesa.scale(100);//Factor de escalado un 100*100%
  mesa.translate(300,280,0);
  
}

public void draw() {
  background(0);
  lights();
  
  camera( width/2 -100, height/2, 200, width/2, height/2 +50, 0, 0, 1, 0);
         
  shape(mesa);
  println(mouseX,mouseY);
  
}
