#define echo   2
  #define trig   3
  #define Buzzer 7

  const int scan_Distance = 100;//distance upto which the sensor should scan
  
  float  duration; // time taken by the pulse to return back
  float distance;  // oneway distance travelled by the pulse
  int obstaclepin = 4;
  int ledpin = 13;
  int hasobstacle = LOW;
  
  void setup() {
    
    pinMode(ledpin, OUTPUT);
    pinMode(trig, OUTPUT);
    pinMode(echo, INPUT);
    pinMode(Buzzer,OUTPUT);
    Serial.begin(9600);
  
  }
  
  void loop() {
      time_Measurement();
      distance = (float)duration * (0.0343) / 2;
      if (distance <= scan_Distance) 
      {

        intruder_detected(); 

        hasobstacle = digitalRead(obstaclepin);

        if (hasobstacle == HIGH)
        {
          digitalWrite(ledpin, LOW);
        }
        else {
          digitalWrite(ledpin, HIGH);
        }

      }
      else {
        Serial.println("path is clear");
      }
      delay(100);
    }
  
  void time_Measurement()
  {
    digitalWrite(trig, LOW);
    delayMicroseconds(2);
  
    digitalWrite(trig, HIGH);
    delayMicroseconds(10);
    digitalWrite(trig, LOW);
  
    duration = pulseIn(echo, HIGH);
  }
  
  void intruder_detected()
  {
    Serial.println("  Intruder at ");
    Serial.println("    ");
    Serial.println(distance);
    Serial.println(" cm");
    digitalWrite(Buzzer, HIGH);
    delay(1000);
    digitalWrite(Buzzer, LOW);
  }
