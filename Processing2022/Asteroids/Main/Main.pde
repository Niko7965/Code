
ArrayList<Asteroid> asteroids = new ArrayList<Asteroid>();

int asteroidSize = 20;




public void setup(){
  size(1000,1000);
  generateAsteroids(10);
  

}


public void draw(){
  moveAsteroids();
  checkCollisions();
  drawBackground();
  drawAsteroids();
 
}


public void drawBackground(){
  fill(0,0,0);
  rect(0,0,displayWidth,displayHeight);
}

public void generateAsteroids(int n){
  for(int i = 0; i<n; i++){
    asteroids.add(new Asteroid(displayWidth,displayHeight));
  }

}

public void checkCollisions(){
  for(Asteroid a1 : asteroids){
    for(Asteroid a2: asteroids){
      if(a1 != a2 && collision(a1, a2)){
        println("collision");
      }    
    }
  }
}

public void moveAsteroids(){
  for(Asteroid a : asteroids){
    a.update();
  }

}


public float distance(Asteroid a1, Asteroid a2){
  return sqrt(pow(a2.getXPos()-a1.getXPos(),2) + pow(a2.getYPos(),a1.getYPos()));
}

public boolean collision(Asteroid a1, Asteroid a2){
  return distance(a1, a2) < asteroidSize;
}


public void drawAsteroids(){
  fill(255,255,255);
  for(Asteroid a : asteroids){
    circle(a.getXPos(),a.getYPos(),asteroidSize);
  }
  


  

}
