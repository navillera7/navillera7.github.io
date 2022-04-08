const int StepX = 2;
const int DirX = 5;
const int StepY = 3;
const int DirY = 6;
const int StepZ = 4;
const int DirZ = 7;
const int EnX = 0;

String sig;

void setup() {
  pinMode(StepX, OUTPUT);
  pinMode(StepY, OUTPUT);
  pinMode(StepZ, OUTPUT);
  pinMode(DirX, OUTPUT);
  pinMode(DirY, OUTPUT);
  pinMode(DirZ, OUTPUT);
}

void loop() {
  while (Serial.available()){
    char wait = Serial.read();
    sig.concat(wait);
  }
  String sss = String(sig);

  String dx = sss.substring(0, 1);
  String dy = sss.substring(3, 4);
  String dz = sss.substring(6, 7);

  String a1 = sss.substring(1, 3);
  String a2 = sss.substring(4, 6);
  String a3 = sss.substring(7, 9);

//  int v1 = 1000 * (a1.toInt());
//  int v2 = 1000 * (a2.toInt());
//  int v3 = 1000 * (a3.toInt());
  int v1 = 4000;
  int v2 = 8000;
  int v3 = 4000;

  
  
  if (dx == "n") {
    digitalWrite(DirX, HIGH);
  }
  if (dy == "p") {
    digitalWrite(DirY, HIGH);
  }
  if (dz == "p") {
    digitalWrite(DirZ, HIGH);
  }
  if (dx == "p") {
    digitalWrite(DirX, LOW);
  }
  if (dy == "n") {
    digitalWrite(DirY, LOW);
  }
  if (dz == "n") {
    digitalWrite(DirZ, LOW);
  }

  for (int x=0; x<0; x++) {
    digitalWrite(StepX, HIGH);
    delayMicroseconds(1);
//    digitalWrite(StepX, LOW);
//    delayMicroseconds(1);
  }
  delay(500);
  for (int x=0; x<8000; x++){
    digitalWrite(StepY, HIGH);
    delayMicroseconds(1);
    digitalWrite(StepY, LOW);
    delayMicroseconds(1);
  }
  delay(500);
  for (int x=0; x<0; x++){
    digitalWrite(StepZ, HIGH);
    delayMicroseconds(1);
    digitalWrite(StepZ, LOW);
    delayMicroseconds(1);
  }
  delay(500);
}