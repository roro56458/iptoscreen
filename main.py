import serial
import subprocess
import time
import yaml
import os
import sys

# Fonction pour récupérer l'adresse IP en fonction du port Ethernet et de l'OS
def get_ip(ethernet_port, os_name):
    ip_address = None
    if os_name == 'windows':
        # Commande pour récupérer l'IP sous Windows
        result = subprocess.run(['ipconfig'], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if ethernet_port in line and "IPv4" in line:
                ip_address = line.split(':')[1].strip()  # Prendre l'IP après le ":"
    elif os_name in ['linux', 'darwin']:  # Linux ou macOS
        # Commande pour récupérer l'IP sous Linux/macOS
        result = subprocess.run(['hostname', '-I'], capture_output=True, text=True)
        ip_address = result.stdout.strip()
        # Si plusieurs adresses sont renvoyées, prendre la première
        ip_address = ip_address.split()[0]

    if ip_address:
        return ip_address
    return None

# Fonction pour initialiser et enregistrer la configuration dans un fichier YAML
def init_config(port_name, os_name, arduino_port):
    config = {
        'ethernet_port': port_name,
        'os': os_name,
        'arduino_port': arduino_port  # Ajouter le port Arduino dans la configuration
    }
    # Enregistrer la configuration dans un fichier YAML
    config_path = '/etc/iptoscreen/config.yaml'
    with open(config_path, 'w') as file:
        yaml.dump(config, file, default_flow_style=False)
    print(f"Configuration enregistrée dans '{config_path}'. Port Ethernet : {port_name}, OS : {os_name}, Port Arduino : {arduino_port}")

# Fonction pour envoyer l'IP à l'Arduino via le port série
def send_ip_to_arduino(ip_address, arduino_port):
    ser = serial.Serial(arduino_port, 9600)  # Utiliser le port Arduino spécifié dans la config
    time.sleep(2)  # Attendre que la connexion série soit prête
    ser.write(ip_address.encode())  # Convertir l'IP en bytes et l'envoyer
    print("Adresse IP envoyée à l'Arduino.")
    time.sleep(10)  # Attendre 10 secondes avant de fermer la connexion série
    ser.close()  # Fermer la connexion série

# Charger la configuration depuis le fichier YAML
config_path = '/etc/iptoscreen/config.yaml'
if os.path.exists(config_path):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)

    ethernet_port = config.get('ethernet_port', 'non spécifié')
    os_name = config.get('os', 'non spécifié')
    arduino_port = config.get('arduino_port', '/dev/ttyACM0')  # Port Arduino par défaut
else:
    print("Aucun fichier de configuration trouvé.")
    sys.exit(1)

# Récupérer l'adresse IP en temps réel en fonction du port Ethernet et de l'OS
ip_address = get_ip(ethernet_port, os_name)

if ip_address:
    # Afficher l'adresse IP pour vérifier
    print(f"Adresse IP de l'ordinateur : {ip_address}")

    # Envoyer l'adresse IP à l'Arduino
    send_ip_to_arduino(ip_address, arduino_port)
else:
    print("Aucune adresse IP valide trouvée pour le port spécifié.")
    sys.exit(1)
