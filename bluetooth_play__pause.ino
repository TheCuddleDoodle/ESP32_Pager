/**
 * This example turns the ESP32 into a Bluetooth to control media of onging bluetooth device
 */
#include <BleKeyboard.h>

BleKeyboard bleKeyboard;
const int threshold = 17;
const int touchPin = 4;

void setup() {
  Serial.begin(115200);
  Serial.println("Starting BLE work!");
  pinMode(LED_BUILTIN, OUTPUT);
  bleKeyboard.begin();
  
}

void loop() {
  if(bleKeyboard.isConnected()){
    Serial.println("Bluetooth is connected");
    int touch_val = touchRead(touchPin);
    Serial.println(touch_val);
    if(touch_val <  threshold ){
    digitalWrite(LED_BUILTIN, HIGH);
    Serial.println("Sending Play/Pause media key...");
    bleKeyboard.write(KEY_MEDIA_PLAY_PAUSE);
    delay(500);
    digitalWrite(LED_BUILTIN, LOW);
    }
  }
  digitalWrite(LED_BUILTIN, LOW);

  Serial.println("No delay.");
  delay(200);
}
