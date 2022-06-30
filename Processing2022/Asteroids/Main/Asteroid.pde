class Asteroid{
  
  private int screenWidth, screenHeight;

  private float xpos, ypos;
  private float xvel, yvel;
  
  
  
  Asteroid(int screenHeight, int screenWidth){
    this.screenWidth = screenWidth;
    this.screenHeight = screenHeight;
    
    this.xpos = random(screenWidth);
    this.ypos = random(screenHeight);
    
    this.xvel = random(screenHeight/200);
    this.yvel = random(screenWidth/200);
    
    if(floor(xvel) % 2 == 0){
      xvel *= -1;
    }
    if(floor(yvel) % 2 == 0){
      yvel *= -1;
    }
    
    
    
  }
  
  
  public void update(){
    xpos = (xpos + xvel) % screenWidth;
    ypos = (ypos + yvel) % screenHeight;
  }
  
  public float getXPos(){
    return xpos;
  }
  
  public float getYPos(){
    return ypos;
  }
  
  
  

}
