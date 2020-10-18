#include<DHT.h>
#include <PulseSensorPlayground.h>
#include <Arduino.h> 
#include <TinyGPS.h>


//pin defines
#define DHTPIN 13
#define DHTTYPE DHT11
#define PULSE_PIN A0
int Signal;
float lattitude , longitude;
int year , month , date, hour , minute , second;
String date_str , time_str , lat_str , lng_str;
int pm;

TinyGPS gps;

//intial Startups
DHT dht(DHTPIN,DHTTYPE);
void setup() 
{
  Serial.begin(9600);
  Serial1.begin(9600);
  //Serial.println("TESTING NOW.....");
  dht.begin();
}

void loop() 
{
  //Reading DHT
  delay(200);
  float h=dht.readHumidity();
  float t=dht.readTemperature();
  //Serial.print("Humidity:");
  Serial.print(h);
  Serial.print("x");
  //Serial.print("Temperature = ");
  Serial.print(t);
  Serial.print("x");
  
  Signal=analogRead(PULSE_PIN);
  if(Signal>550)
    {
      //Serial.print("Pulse Rate= ");
      Serial.println(Signal);
     

    }
   
     bool newData = false;
  unsigned long chars;
  unsigned short sentences, failed;

  // For one second we parse GPS data and report some key values
  for (unsigned long start = millis(); millis() - start < 1000;)
  {
    while (Serial1.available())
    {
      char c = Serial1.read();
      //Serial.print(c);
      if (gps.encode(c)) 
        newData = true;  
    }
  }

  if (newData)      //If newData is true
  {
    float flat, flon;
    unsigned long age;
    gps.f_get_position(&flat, &flon, &age);   
    //Serial1.print("Latitude = ");
    Serial1.print(flat == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flat, 6);
    //Serial1.print(" Longitude = ");
    Serial1.print("x");
    Serial1.print(flon == TinyGPS::GPS_INVALID_F_ANGLE ? 0.0 : flon, 6);
    Serial1.println();
  }
}
