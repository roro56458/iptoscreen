# IPtoScreen
**IPtoScreen** is a software that **displays** the IP address of the machine on a **Liquid Crystal Display (LCD).**

## How to set up
For more information, visit the IPtoScreen Documentation.

1. Clone this repository
bash
Copier
Modifier
git clone https://github.com/roro56458/iptoscreen.git
2. Upload the code to the Arduino
Make sure to respect the pinout! Also, don't forget to install the required dependencies (found in requirements.txt).

3. Initialize the script
Run the following command, replacing the parameters with your setup:

bash
Copier
Modifier
python main.py init "eth_port" "running_os" "arduino_port"  # Example: COM3 or /dev/ttyUSB0
4. Launch the script
bash
Copier
Modifier
python main.py
IPtoScreen (Français)
IPtoScreen est un logiciel qui affiche l'adresse IP de la machine sur un écran à cristaux liquides (LCD).

Installation
Pour plus d'informations, rendez-vous sur la documentation IPtoScreen.

1. Cloner ce dépôt
bash
Copier
Modifier
git clone https://github.com/roro56458/iptoscreen.git
2. Téléverser le code sur l'Arduino
Assurez-vous de respecter le câblage ! N'oubliez pas non plus d'installer les dépendances nécessaires (listées dans requirements.txt).

3. Initialiser le script
Exécutez la commande suivante en remplaçant les paramètres par votre configuration :

bash
Copier
Modifier
python main.py init "port_eth" "os" "port_arduino"  # Exemple : COM3 ou /dev/ttyUSB0
4. Lancer le script
bash
Copier
Modifier
python main.py
