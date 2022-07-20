PShape mesa;
PShape silla1;
PShape silla2;
PShape lampara;

public void setup() {
  size(630, 360, P3D);

  mesa = loadShape("mesa.obj");
  mesa.rotateZ(PI);
  mesa.scale(100);//Factor de escalado un 100*100%
  mesa.translate(300,280,0);

  silla1 = loadShape("chair.obj");
  silla1.rotateZ(PI);
  silla1.rotateY(230);
  silla1.scale(2);
  silla1.translate(310,280,100);

  silla2 = loadShape("chair.obj");
  silla2.rotateZ(PI);
  silla2.rotateY(360);
  silla2.scale(2);
  silla2.translate(245,280,10);

  lampara = loadShape("glass.obj");
  lampara.rotateZ(PI);
  lampara.scale(5);
  lampara.translate(300, 200, 0);

}

public void draw() {
  background(0);
  lights();

  camera( width/2 -100, height/2, 200, width/2, height/2 +50, 0, 0, 1, 0);

  shape(mesa);
  shape(silla1);
  shape(silla2);
  shape(lampara);
  println(mouseX,mouseY);

}
