#define sensor_pin A0
bool streaming = false;
bool send_one_value = false;
long send_count = 0;
long current_time = 0;
int val = 0;

bool siren_mode = false;
bool auto_mode = false;
bool on = false; // ручной режим

void setup()
{
  pinMode(12, OUTPUT);
  pinMode(11, OUTPUT);
  Serial.begin(9600);
}

void loop()
{
  current_time = millis();
  val = analogRead(sensor_pin);
  data_reading();
  led();
  if (streaming == true and 
      current_time / 100 != send_count) {
    send_photo_data();
    send_count = current_time / 100;
    Serial.print("Time in millis:");
    Serial.println(millis());
  }
  if (send_one_value == true) {
    send_photo_data();
    send_one_value = false;
  }
}

void send_photo_data(){
  Serial.print("Sensor value: ");
  Serial.println(val);
}

void data_reading() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'p') { // p for Photo sensor
      streaming = true;
    } else if (command == 's') { // s for Single value
      streaming = false;
      send_one_value = true;
    }
    else {
      streaming = false;
    }
    if (command == 'h'){
      siren_mode = false;
      auto_mode = false;
      on = !on;
    } else if (command == 'b'){
      siren_mode = true;
      auto_mode = false;
      on = false;
    } else if (command == 'a'){
      siren_mode = false;
      auto_mode = true;
      on = false;
    }
  }
}

void led(){
  if (auto_mode){
    if (val > 40) {
      digitalWrite(12, LOW);
    }
    else {
      digitalWrite(12, HIGH);
    }
  }
  else if (siren_mode){
    if (current_time % 200 <= 100) digitalWrite(12, HIGH);
    else digitalWrite(12, LOW);
  }
  else if (on) {
    digitalWrite(12, HIGH);
  }
  else digitalWrite(12, LOW);
}
