void setup() {
  Serial.begin(9600);
  for (int thisPin = 6; thisPin < 13; thisPin++) {
    pinMode(thisPin, OUTPUT);
  }
}

char command=' ';

void setPins(int pin11, int pin12, int pin7, int pin8) {
  digitalWrite(11, pin11);
  digitalWrite(12, pin12);
  digitalWrite(7, pin7);
  digitalWrite(8, pin8);
}

void loop() {
  if(Serial.available()>0){
  	command = Serial.read();
  }
  switch(command){
    case 'a':
    // 1
	setPins(HIGH, LOW, LOW, HIGH);
	delay(10);
    case 'b':
    	// 2
      setPins(HIGH, LOW, HIGH, LOW);
      break;
    case 'c':
    	// 3
      setPins(LOW, HIGH, LOW, HIGH);
      break;
    case 'd':
    	// 4
      setPins(LOW, HIGH, HIGH, LOW);
      break;
    case 'e':
    // 1, 2
      setPins(HIGH, LOW, LOW, LOW);
      break;
    case 'f':
    // 3, 4
      setPins(LOW, HIGH, LOW, LOW);
      break;
    case 'g':
    // 1, 3
      setPins(HIGH, HIGH, LOW, HIGH);
      break;
    case 'h':
    // 2, 4
      setPins(HIGH, HIGH, HIGH, LOW);
      break;
    
    case 'i':
    // 1, 4
      setPins(HIGH, LOW, LOW, HIGH);
        delay(10);
      setPins(LOW, HIGH, HIGH, LOW);
        delay(10);
      break;
    
    case 'j':
    // 2, 3
      setPins(HIGH, LOW, HIGH, LOW);
        delay(10);
      setPins(LOW, HIGH, LOW, HIGH);
        delay(10);
      break;
    
    case 'k':
    // 1, 2, 3
      setPins(HIGH, LOW, LOW, LOW);
        delay(10);
      setPins(LOW, HIGH, LOW, HIGH);
        delay(10);
      break;
    
    case 'l':
    // 2, 3, 4
      setPins(HIGH, LOW, HIGH, LOW);
        delay(10);
      setPins(LOW, HIGH, LOW, LOW);
        delay(10);
      break;
    
    case 'm':
    // 3, 4, 1
      setPins(HIGH, LOW, HIGH, LOW);
        delay(10);
      setPins(LOW, HIGH, LOW, LOW);
        delay(10);
      break;
    
    case 'n':
    // 4, 1, 2
      setPins(HIGH, LOW, LOW, LOW);
        delay(10);
      setPins(LOW, HIGH, HIGH, LOW);
        delay(10);
      break;
    
    case 'o':
    // 1, 2, 3, 4
      setPins(HIGH, HIGH, LOW, LOW);
        delay(10);
      setPins(LOW, LOW, LOW, LOW);
        delay(10);
      break;
    
    case 'p':
    // off
      setPins(LOW, LOW, LOW, LOW);
      break;
    
	default:
    	break;
    }
}