#include <LiquidCrystal.h>

// Déclaration des objets pour l'écran LCD
LiquidCrystal lcd(12, 11, 5, 4, 3, 2); 

void setup() {
  // Initialisation de la communication série et de l'écran LCD
  Serial.begin(9600);  // Démarre la communication série à 9600 bauds
  Serial.println("Initialisation de la communication série...");
  
  delay(1000);  // Petit délai pour s'assurer que l'écran est prêt

  lcd.begin(16, 2);    // Initialisation de l'écran LCD avec 16 colonnes et 2 lignes
  Serial.println("Ecran LCD initialisé.");
  
  lcd.print("System IP:"); // Afficher "System IP:" sur la première ligne
  Serial.println("Affichage du texte 'System IP:' sur l'écran LCD.");

  // Attente de la première donnée série (l'adresse IP)
  while (!Serial) {
    // Attendre que la communication série soit prête
  }
  Serial.println("Communication série prête.");

  lcd.setCursor(0, 1);  // Positionner le curseur sur la deuxième ligne de l'écran LCD
  Serial.println("Curseur positionné sur la ligne 2.");
}

void loop() {
  // Vérifier si des données sont disponibles sur le port série
  if (Serial.available() > 0) {
    String ipAddress = Serial.readString();  // Lire la chaîne reçue (l'adresse IP)
    
    Serial.print("Adresse IP reçue : ");
    Serial.println(ipAddress);  // Afficher l'adresse IP reçue dans la console série
    
    // Affichage de l'adresse IP reçue sur l'écran LCD
    lcd.setCursor(0, 1);  // Positionner le curseur sur la deuxième ligne de l'écran LCD
    lcd.print(ipAddress);  // Afficher l'adresse IP sur la deuxième ligne
    Serial.println("Adresse IP affichée sur l'écran LCD.");
  }
}
