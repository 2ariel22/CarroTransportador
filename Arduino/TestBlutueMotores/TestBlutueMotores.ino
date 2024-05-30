#include "BluetoothSerial.h"
BluetoothSerial SerialBT;

const int Motor1A = 32;
const int Motor1B = 33;
const int Motor1PWM = 25;

const int Motor2A = 26;
const int Motor2B = 27;
const int Motor2PWM = 16;

bool motorEncendido = false;

void setup() {
  Serial.begin(115200);
  SerialBT.begin("PROMEESP32");

  // Inicializar los pines de control como salida
  pinMode(Motor1A, OUTPUT);
  pinMode(Motor1B, OUTPUT);
  pinMode(Motor1PWM, OUTPUT);

  pinMode(Motor2A, OUTPUT);
  pinMode(Motor2B, OUTPUT);
  pinMode(Motor2PWM, OUTPUT);

  digitalWrite(Motor1A, LOW); // Configurar la dirección inicial
  digitalWrite(Motor1B, LOW); // Apagar el motor
  digitalWrite(Motor2A, LOW); // Configurar la dirección inicial
  digitalWrite(Motor2B, LOW); // Apagar el motor

}

void loop() {
  if (SerialBT.available()) {
    String comando = SerialBT.readString();
    comando.trim(); // Eliminar espacios en blanco al principio y al final de la cadena
    Serial.println(comando);

    if (comando.indexOf("iniciar") != -1) { // Si la cadena contiene "iniciar"
      Serial.println("Iniciar motor");
      digitalWrite(Motor1A, HIGH); // Configurar la dirección
      digitalWrite(Motor1B, LOW); // Activar el motor
      analogWrite(Motor1PWM, 120);

    digitalWrite(Motor2A, HIGH); // Configurar la dirección
      digitalWrite(Motor2B, LOW); // Activar el motor
      analogWrite(Motor2PWM, 255);

      motorEncendido = true;
    } else if (comando.indexOf("stop") != -1) { // Si la cadena contiene "stop"
      Serial.println("Detener motor");
      digitalWrite(Motor1A, LOW); // Detener el motor
      digitalWrite(Motor2A, LOW);
      motorEncendido = false;
    }
  }
  

  delay(20);
}
