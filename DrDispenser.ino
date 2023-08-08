#include <DS3231.h>
#include <RTClib.h>
#include <Wire.h>
#include <Servo.h>
#include <SPI.h>
#include <SD.h>
#include <string.h> 
#include "Chambers.h"

#define CS_PIN 53

#define ROW_DIM 7
#define COL_DIM 16

Time currTime;
RTC_DS3231 RTC; 
Chambers chamber1, chamber2, chamber3, chamber4, chamber5, chamber6;

Servo myservo11, myservo12;
Servo myservo21, myservo22;
Servo myservo31, myservo32;
Servo myservo41, myservo42;
Servo myservo51, myservo52;
Servo myservo61, myservo62;

long wait;

int speakerPin = 2;
int pirPin = 10;
int irPin1 = A0;
int irPin2 = A1;
int irPin3 = A2;
int irPin4 = A3;
int irPin5 = A4;
int irPin6 = A5;
int pirVal, irVal;

int resVal1 = 0;
int resVal2 = 0;
int resVal3 = 0;
int resVal4 = 0;
int resVal5 = 0;
int resVal6 = 0;

uint8_t resMin;

String str;
String arr[15];
String Data;
int c1q = 0;
int c2q = 0;
int c3q = 0;
int c4q = 0;
int c5q = 0;
int c6q = 0;

int cin,dosage,quantity,mtime,atime,etime,Mon,Tues,Wed,Thur,Fri,Sat,Sun;
String DData;

void Dispense(Servo obj1, Chambers obj2, int irPin)
{
  for (int i = 0; i < obj2.dosage; i++)
  {
    obj1.write(180);
    delay(500);
    obj1.write(0);
    delay(500);
    //obj2.current_quantity = obj2.current_quantity - 1;
    //Serial.print("dispensing");
  }
}

void sendDataToSerial()
{

}

void processIncomingSerial()
{
  if(Serial.available() > 0)
  {
    String data = Serial.readStringUntil('\n');
    sscanf(data.c_str(),"%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d,%d",&cin,&dosage,&quantity,&mtime,&atime,&etime,&Mon, &Tues,&Wed,&Thur,&Fri,&Sat,&Sun);
    if(cin == 1)
    {
      chamber1.Days[0] = Mon;
      chamber1.Days[1] = Tues;
      chamber1.Days[2] = Wed;
      chamber1.Days[3] = Thur;
      chamber1.Days[4] = Fri;
      chamber1.Days[5] = Sat;
      chamber1.Days[6] = Sun;

      chamber1.dosage = dosage;
      chamber1.current_quantity = quantity;

      chamber1.MorningTime.hour = mtime;
      chamber1.MorningTime.min = 0;
      chamber1.AfternoonTime.hour = atime;
      chamber1.AfternoonTime.min = 0;
      chamber1.EveningTime.hour = etime;
      chamber1.EveningTime.min = 0;
    }
    if(cin == 2)
    {
      chamber2.Days[0] = Mon;
      chamber2.Days[1] = Tues;
      chamber2.Days[2] = Wed;
      chamber2.Days[3] = Thur;
      chamber2.Days[4] = Fri;
      chamber2.Days[5] = Sat;
      chamber2.Days[6] = Sun;

      chamber2.dosage = dosage;
      chamber2.current_quantity = quantity;

      chamber2.MorningTime.hour = mtime;
      chamber2.MorningTime.min = 0;
      chamber2.AfternoonTime.hour = atime;
      chamber2.AfternoonTime.min = 0;
      chamber2.EveningTime.hour = etime;
      chamber2.EveningTime.min = 0;
    }
    if(cin == 3)
    {
      chamber3.Days[0] = Mon;
      chamber3.Days[1] = Tues;
      chamber3.Days[2] = Wed;
      chamber3.Days[3] = Thur;
      chamber3.Days[4] = Fri;
      chamber3.Days[5] = Sat;
      chamber3.Days[6] = Sun;

      chamber3.dosage = dosage;
      chamber3.current_quantity = quantity;

      chamber3.MorningTime.hour = mtime;
      chamber3.MorningTime.min = 0;
      chamber3.AfternoonTime.hour = atime;
      chamber3.AfternoonTime.min = 0;
      chamber3.EveningTime.hour = etime;
      chamber3.EveningTime.min = 0;
    }
    if(cin == 4)
    {
      chamber4.Days[0] = Mon;
      chamber4.Days[1] = Tues;
      chamber4.Days[2] = Wed;
      chamber4.Days[3] = Thur;
      chamber4.Days[4] = Fri;
      chamber4.Days[5] = Sat;
      chamber4.Days[6] = Sun;

      chamber4.dosage = dosage;
      chamber4.current_quantity = quantity;

      chamber4.MorningTime.hour = mtime;
      chamber4.MorningTime.min = 0;
      chamber4.AfternoonTime.hour = atime;
      chamber4.AfternoonTime.min = 0;
      chamber4.EveningTime.hour = etime;
      chamber4.EveningTime.min = 0;
    }
    if(cin == 5)
    {
      chamber5.Days[0] = Mon;
      chamber5.Days[1] = Tues;
      chamber5.Days[2] = Wed;
      chamber5.Days[3] = Thur;
      chamber5.Days[4] = Fri;
      chamber5.Days[5] = Sat;
      chamber5.Days[6] = Sun;

      chamber5.dosage = dosage;
      chamber5.current_quantity = quantity;

      chamber5.MorningTime.hour = mtime;
      chamber5.MorningTime.min = 0;
      chamber5.AfternoonTime.hour = atime;
      chamber5.AfternoonTime.min = 0;
      chamber5.EveningTime.hour = etime;
      chamber5.EveningTime.min = 0;
    }
    if(cin == 6)
    {
      chamber6.Days[0] = Mon;
      chamber6.Days[1] = Tues;
      chamber6.Days[2] = Wed;
      chamber6.Days[3] = Thur;
      chamber6.Days[4] = Fri;
      chamber6.Days[5] = Sat;
      chamber6.Days[6] = Sun;

      chamber6.dosage = dosage;
      chamber6.current_quantity = quantity;

      chamber6.MorningTime.hour = mtime;
      chamber6.MorningTime.min = 0;
      chamber6.AfternoonTime.hour = atime;
      chamber6.AfternoonTime.min = 0;
      chamber6.EveningTime.hour = etime;
      chamber6.EveningTime.min = 0;
    }
  }
}

void setup() 
{
  // put your setup code here, to run once: 
  Serial.begin(9600);
  RTC.begin();
  
  pinMode(pirPin, INPUT);
  pinMode(irPin1, INPUT);
  pinMode(irPin2, INPUT);
  pinMode(irPin3, INPUT);
  pinMode(irPin4, INPUT);
  pinMode(irPin5, INPUT);
  pinMode(irPin6, INPUT);
  pinMode(speakerPin, OUTPUT);
  
  myservo11.attach(22);
  myservo21.attach(23);
  myservo31.attach(30);
  myservo41.attach(34);
  myservo51.attach(38);
  myservo61.attach(42);

  myservo11.write(0);
  myservo21.write(0);
  myservo31.write(0);
  myservo41.write(0);
  myservo51.write(0);
  myservo61.write(0);
  
}

void loop() 
{
  // put your main code here, to run repeatedly:
  
//  Serial.print("Motion Sensor Test \n");
//  pirVal = digitalRead(pirPin);
//  if(pirVal)
//  {
//  Serial.print ("motion detected, PIR VALUE: ");
//  Serial.print(pirVal);
//  Serial.print("\n");
//  }
//  else
//  {
//    Serial.print("no motion detected, PIR VALUE: ");
//    Serial.print(pirVal);
//    Serial.print("\n");
//  }
  
  resMin = 61;
  processIncomingSerial();

  //Serial.print("CHECKING");
  //Serial.print("\n");
  wait = 0;
  DateTime now = RTC.now();
  uint8_t Day = now.dayOfTheWeek();
  
  currTime.hour = now.hour();
  currTime.min = now.minute();
  currTime.sec = now.second();

  /*Serial.print(" <--- Device Current Time ");
  Serial.print("Dr. Dispenser Current Time: ");
  Serial.print(currTime.hour);
  Serial.print(":");
  Serial.print(currTime.min);
  Serial.print(":");
  Serial.print(currTime.sec);
  Serial.print("\n");*/
  
  if (Day == 7)
  {
    Day = 0;
  }
  
  
  if (chamber1.Days[Day] == 1)
    {
      if (chamber1.Refill())
        {
          //send refill notfication 
        }
        
      if ((currTime.hour == chamber1.MorningTime.hour && currTime.min == chamber1.MorningTime.min) || (currTime.hour == chamber1.AfternoonTime.hour && currTime.min == chamber1.AfternoonTime.min) || (currTime.hour == chamber1.EveningTime.hour && currTime.min == chamber1.EveningTime.min))
        {
          chamber1.dval = 1;
        }
    }
  
  if (chamber2.Days[Day] == 1)
    {
      if (chamber2.Refill())
        {
          //send refill notfication 
        }
        
      if ((currTime.hour == chamber2.MorningTime.hour && currTime.min == chamber2.MorningTime.min) || (currTime.hour == chamber2.AfternoonTime.hour && currTime.min == chamber2.AfternoonTime.min) || (currTime.hour == chamber2.EveningTime.hour && currTime.min == chamber2.EveningTime.min))
        {
          chamber2.dval = 1;
        }
    }
  
  if (chamber3.Days[Day] == 1)
    {
      if (chamber3.Refill())
        {
          //send refill notfication 
        }
        
      if ((currTime.hour == chamber3.MorningTime.hour && currTime.min == chamber3.MorningTime.min) || (currTime.hour == chamber3.AfternoonTime.hour && currTime.min == chamber3.AfternoonTime.min) || (currTime.hour == chamber3.EveningTime.hour && currTime.min == chamber3.EveningTime.min))
        {
          chamber3.dval = 1;
        }
    }
  
  if (chamber4.Days[Day] == 1)
    {
      if(chamber4.Refill())
        {
          //send refill notfication 
        }
        
      if ((currTime.hour == chamber4.MorningTime.hour && currTime.min == chamber4.MorningTime.min) || (currTime.hour == chamber4.AfternoonTime.hour && currTime.min == chamber4.AfternoonTime.min) || (currTime.hour == chamber4.EveningTime.hour && currTime.min == chamber4.EveningTime.min))
        {
          chamber4.dval = 1;
        }
    }
  
  if (chamber5.Days[Day] == 1)
    {
      if(chamber5.Refill())
        {
          //send refill notfication 
        }
        
      if ((currTime.hour == chamber5.MorningTime.hour && currTime.min == chamber5.MorningTime.min) || (currTime.hour == chamber5.AfternoonTime.hour && currTime.min == chamber5.AfternoonTime.min) || (currTime.hour == chamber5.EveningTime.hour && currTime.min == chamber5.EveningTime.min))
        {
          chamber5.dval = 1;
        }
    }
  
  if (chamber6.Days[Day] == 1)
    {
      if(chamber6.Refill())
        {
          //send refill notfication 
        }
        
      if ((currTime.hour == chamber6.MorningTime.hour && currTime.min == chamber6.MorningTime.min) || (currTime.hour == chamber6.AfternoonTime.hour && currTime.min == chamber6.AfternoonTime.min) || (currTime.hour == chamber6.EveningTime.hour && currTime.min == chamber6.EveningTime.min))
        {
          chamber6.dval = 1;
        }
    }
  
  
  if (currTime.min == resMin)
  {
    while ((!pirVal) && (wait != 300000))
    {
//      Serial.print("pir: ");
//      Serial.print(pirVal);
//      Serial.print("\n");
      
      if ((wait == 0) || (wait == 150000))
      {
//        Serial.print("wait: ");
//        Serial.print(wait);
//        Serial.print("\n");
//        Serial.print("Alarm On");
//        Serial.print("\n");
        tone(speakerPin, 394, 30000);
      }
      
      pirVal = digitalRead(pirPin);
      
      if (pirVal)
        {
          noTone(speakerPin);
//          Serial.print("Alarm Off");
//          Serial.print("\n");
//          Serial.print("pir: ");
//          Serial.print(pirVal);
//          Serial.print("\n");
        }
        
      wait = wait + 1000;
//      Serial.print("wait: ");
//      Serial.print(wait);
//      Serial.print("\n");
      delay(1000);
    }
  
    if (pirVal == 1)
    {
      if (resVal1 == 1)
      {
//        Serial.print("dispensing chamber 1");
//        Serial.print("\n");
        Dispense(myservo11, chamber1, irPin1);
        c1q = chamber1.current_quantity - chamber1.dosage;
        resVal1 = 0;
      }
      
      if (resVal2 == 1)
      {
//        Serial.print("dispensing chamber 2");
//        Serial.print("\n");
        Dispense(myservo21, chamber2, irPin2);
        c2q = chamber2.current_quantity - chamber2.dosage;
        resVal2 = 0;
      }
      
      if (resVal3 == 1)
      {
//        Serial.print("dispensing chamber 3");
//        Serial.print("\n");
        Dispense(myservo31, chamber3, irPin3);
        c3q = chamber3.current_quantity - chamber3.dosage;
        resVal3 = 0;
      }
      
      if (resVal4 == 1)
      {
//        Serial.print("dispensing chamber 4");
//        Serial.print("\n");
        Dispense(myservo41, chamber4, irPin4);
        c4q = chamber4.current_quantity - chamber4.dosage;
        resVal4 = 0;
      }
      
      if (resVal5 == 1)
      {
//        Serial.print("dispensing chamber 5");
//        Serial.print("\n");
        Dispense(myservo51, chamber5, irPin5);
        c5q = chamber5.current_quantity - chamber5.dosage;
        resVal5 = 0;
      }
      
      if (resVal6 == 1)
      {
//        Serial.print("dispensing chamber 6");
//        Serial.print("\n");
        Dispense(myservo61, chamber6, irPin6);
        c6q = chamber6.current_quantity - chamber6.dosage;
        resVal6 = 0;
      }
    }
    
    resMin = 61;
  
    if (pirVal == 0)
    {
      //display medication not taken and send notification
    }
  }
  
  if ((chamber1.dval == 1) || (chamber2.dval == 1) || (chamber3.dval == 1) || (chamber4.dval == 1) || (chamber5.dval == 1) || (chamber6.dval == 1))
  {
    while ((!pirVal) && (wait != 300000))
    {
//      Serial.print("pir: ");
//      Serial.print(pirVal);
//      Serial.print("\n");
      
      if ((wait == 0) || (wait == 150000))
      {
//        Serial.print("wait: ");
//        Serial.print(wait);
//        Serial.print("\n");
//        Serial.print("Alarm On");
//        Serial.print("\n");
        tone(speakerPin, 394, 30000);
      }
      
      pirVal = digitalRead(pirPin);
      
      if (pirVal)
        {
          noTone(speakerPin);
//          Serial.print("Alarm Off");
//          Serial.print("\n");
//          Serial.print("pir: ");
//          Serial.print(pirVal);
//          Serial.print("\n");
        }
        
      wait = wait + 1000;
//      Serial.print("wait: ");
//      Serial.print(wait);
//      Serial.print("\n");
      
      if ((wait == 30000) || (wait == 180000))
      {
//       Serial.print("Alarm Off");
//       Serial.print("\n"); 
      }
      
      delay(1000);
    }
  
    if (pirVal == 1)
    {
      if (chamber1.dval == 1)
      {
//        Serial.print("dispensing chamber 1");
//        Serial.print("\n");
        Dispense(myservo11, chamber1, irPin1);
        c1q = chamber1.current_quantity - chamber1.dosage;
        chamber1.dval = 0;
        //delay(1000);
      }
      
      if (chamber2.dval == 1)
      {
//        Serial.print("dispensing chamber 2");
//        Serial.print("\n");
        Dispense(myservo21, chamber2, irPin2);
        c2q = chamber2.current_quantity - chamber2.dosage;
        chamber2.dval = 0;
      }
      
      if (chamber3.dval == 1)
      {
//        Serial.print("dispensing chamber 3");
//        Serial.print("\n");
        Dispense(myservo31, chamber3, irPin3);
        c3q = chamber3.current_quantity - chamber3.dosage;
        chamber3.dval = 0;
      }
      
      if (chamber4.dval == 1)
      {
//        Serial.print("dispensing chamber 4");
//        Serial.print("\n");
        Dispense(myservo41, chamber4, irPin4);
        c4q = chamber4.current_quantity - chamber4.dosage;
        chamber4.dval = 0;
      }
      
      if (chamber5.dval == 1)
      {
//        Serial.print("dispensing chamber 5");
//        Serial.print("\n");
        Dispense(myservo51, chamber5, irPin5);
        c5q = chamber5.current_quantity - chamber5.dosage;
        chamber5.dval = 0;
      }
      
      if (chamber6.dval == 1)
      {
//        Serial.print("dispensing chamber 6");
//        Serial.print("\n");
        Dispense(myservo61, chamber6, irPin6);
        c6q = chamber6.current_quantity - chamber6.dosage;
        chamber6.dval = 0;
      }

//      c1q = chamber1.current_quantity;
//      c2q = chamber2.current_quantity;
//      c3q = chamber3.current_quantity;
//      c4q = chamber4.current_quantity;
//      c5q = chamber5.current_quantity;
//      c6q = chamber6.current_quantity;

      //sendDataToSerial();
      now = RTC.now();
      currTime.sec = now.second();
      long dlay = abs(60 - currTime.sec);
      long dlay2 = dlay * 1000;
      //Serial.print("delaying");
      delay(dlay2);
    }
  
    if (pirVal == 0)
    {
      if (chamber1.dval == 1)
      {
        resMin = (currTime.min + 10) % 60;
        resVal1 = chamber1.dval;
        chamber1.dval = 0;
//        Serial.print("Chamber 1 rescheduling");
//        Serial.print("\n");
      }
      
      if (chamber2.dval == 1)
      {
        resMin = (currTime.min + 10) % 60;
        resVal2 = chamber2.dval;
        chamber2.dval = 0;
//        Serial.print("Chamber 2 rescheduling");
//        Serial.print("\n");
      }
      
      if (chamber3.dval == 1)
      {
        resMin = (currTime.min + 10) % 60;
        resVal3 = chamber3.dval;
        chamber3.dval = 0;
//        Serial.print("Chamber 3 rescheduling");
//        Serial.print("\n");
      }
      
      if (chamber4.dval == 1)
      {
        resMin = (currTime.min + 10) % 60;
        resVal4 = chamber4.dval;
        chamber4.dval = 0;
//        Serial.print("Chamber 4 rescheduling");
//        Serial.print("\n");
      }
      
      if (chamber5.dval == 1)
      {
        resMin = (currTime.min + 10) % 60;
        resVal5 = chamber5.dval;
        chamber5.dval = 0;
//        Serial.print("Chamber 5 rescheduling");
//        Serial.print("\n");
      }
      
      if (chamber6.dval == 1)
      {
        resMin = (currTime.min + 10) % 60;
        resVal6 = chamber6.dval;
        chamber6.dval = 0;
//        Serial.print("Chamber 6 rescheduling");
//        Serial.print("\n");
      }

//      c1q = chamber1.current_quantity;
//      c2q = chamber2.current_quantity;
//      c3q = chamber3.current_quantity;
//      c4q = chamber4.current_quantity;
//      c5q = chamber5.current_quantity;
//      c6q = chamber6.current_quantity;

      //sendDataToSerial();

      now = RTC.now();
      currTime.sec = now.second();
      long dlay = abs(60 - currTime.sec);
      long dlay2 = dlay * 1000;
      //Serial.print("delaying");
      delay(dlay2);
      
    }
  }

      //sendDataToSerial();
}
