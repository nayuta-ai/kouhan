#include <Servo.h>
Servo myServo;
#define IN1 7
#define IN2 8
#define IN3 9
#define IN4 10
#define ENA 5
#define ENB 6

/*motor control*/
void go_back(int t)  //motor rotate clockwise -->robot go ahead
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4,HIGH);
  delay(t);
}
void go_ahead(int t) //motor rotate counterclockwise -->robot go back
{
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4,LOW); 
  delay(t);
}
void go_stop() //motor brake -->robot stop
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4,LOW); 
}
void turn_left(int t)  //left motor rotate clockwise and right motor rotate counterclockwise -->robot turn right
{
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  digitalWrite(IN3, LOW);
  digitalWrite(IN4, HIGH);
  delay(t);
}
void turn_right(int t) //left motor rotate counterclockwise and right motor rotate clockwise -->robot turn left
{
  digitalWrite(IN1, LOW);
  digitalWrite(IN2, HIGH);
  digitalWrite(IN3, HIGH);
  digitalWrite(IN4, LOW);
  delay(t);
}
/*set motor speed */
void set_motorspeed(int lspeed,int rspeed) //change motor speed
{
  analogWrite(ENA,lspeed);//lspeed:0-255
  analogWrite(ENB,rspeed);//rspeed:0-255   
}


void setup() {
  myServo.attach(4);
  /******L298N******/
  pinMode(IN1, OUTPUT); 
  pinMode(IN2, OUTPUT); 
  pinMode(IN3, OUTPUT);
  pinMode(IN4, OUTPUT); 
  pinMode(ENA, OUTPUT);  
  pinMode(ENB, OUTPUT);
  /*
  set_motorspeed(255,255);
  //go ahead 5s
  go_ahead(1000);
  //go back 5s
  go_back(1000);
  //turn left 5s
  set_motorspeed(180,180);
  turn_left(2000);
  //turn right 5s
  turn_right(2000);
  //stop
  go_stop();
  */
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()){
    int x = Serial.read();
    int y = Serial.read();
    int z = 1;
    set_motorspeed(x,x);
    go_ahead(1);
    delay(100);
    myServo.write(100);
    /*
    set_motorspeed(180,180);
    turn_left(2);
    set_motorspeed(y,y);
    go_ahead(1);
    myServo.write(100);
    delay(10);
    myServo.write(0);
    set_motorspeed(y,y);
    go_back(1);
    set_motorspeed(180,180);
    turn_left(2);
    set_motorspeed(x,x);
    go_back(1);
    */
  }
  /*
  set_motorspeed(x,x);
  go_ahead(1000);
  set_motorspeed(180,180);
  turn_left(2000);
  set_motorspeed(y,y);
  go_ahead(1000); 
  set_motorspeed(y,y);
  go_back(1000);
  set_motorspeed(180,180);
  turn_left(2000);
  set_motorspeed(x,x);
  go_back(1000);
  */
}
