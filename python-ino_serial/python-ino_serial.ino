#define TRIG 9 //TRIG 핀 설정 (초음파 보내는 핀)
#define ECHO 8 //ECHO 핀 설정 (초음파 받는 핀)
#include <ArduinoJson.h>

String output_data;
StaticJsonDocument<200> doc;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);

  pinMode(TRIG, OUTPUT);
  pinMode(ECHO, INPUT);
  
  while(!Serial) continue;
  
}

void loop() {
    long duration, distance;

    digitalWrite(TRIG, LOW);
    delayMicroseconds(2);
    digitalWrite(TRIG, HIGH);
    delayMicroseconds(10);
    digitalWrite(TRIG, LOW);

    duration = pulseIn (ECHO, HIGH);
    distance = duration * 17 / 1000;

    Serial.println(distance);
  
  
}
