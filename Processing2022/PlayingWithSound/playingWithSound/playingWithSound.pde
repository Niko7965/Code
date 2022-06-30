import processing.sound.*;

SinOsc sin;
Reverb rev;
int framecount = 0;
boolean on = true;


public void setup(){
  sin = new SinOsc(this);
  sin.play();
  
  rev = new Reverb(this);
  rev.wet(0.5);
  rev.room(1);
  rev.process(sin);
  

}


public void draw(){
 
  

}
