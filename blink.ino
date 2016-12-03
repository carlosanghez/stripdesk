const int VERDE = 9;
const int BLU = 11;
const int ROSSO = 10;
const int delayTime = 1000;
String inString = "";
int index = 0;

void setup() {
  // imposta il pin digitale come output
  Serial.begin(9600);
  pinMode(VERDE, OUTPUT);
  pinMode(BLU, OUTPUT);
  pinMode(ROSSO, OUTPUT);
  pinMode(LED_BUILTIN, OUTPUT);
  // si impostano ad HIGH i pin VERDE, BLU, ROSSO
  // inizialmente il led RGB sarà spento
  digitalWrite(VERDE, 0);
  digitalWrite(BLU, 0);
  digitalWrite(ROSSO, 0);
}

void loop() {
}

void serialEvent()
{
  while (Serial.available() > 0) {
    int inChar = Serial.read();
    if (isDigit(inChar)) {
      // convert the incoming byte to a char
      // and add it to the string:
      inString += (char)inChar;
    }
    // if you get a newline, print the string,
    // then the string's value:
    if (inChar == '\n') {
      Serial.print("Value:");
      Serial.println(inString.toInt());
      Serial.print("String: ");
      Serial.println(inString);
      index=index+1;
      Serial.println(0+index);
      if(index==1){
        analogWrite( ROSSO, inString.toInt());
        Serial.println(inString.toInt());
        //digitalWrite(LED_BUILTIN, HIGH);
        //delay(100);
        //digitalWrite(LED_BUILTIN,LOW);
      }
      if(index==2){
        analogWrite( VERDE, inString.toInt());
        Serial.println(inString.toInt());
        //digitalWrite(LED_BUILTIN, HIGH);
        //delay(100);
        //digitalWrite(LED_BUILTIN,LOW);
      }
      if(index==3){
        analogWrite( BLU, inString.toInt());
        Serial.println(inString.toInt());
        index=0;
        //digitalWrite(LED_BUILTIN, HIGH);
        //delay(100);
        //digitalWrite(LED_BUILTIN,LOW);
      }
      inString = "";
    }
  }
}
