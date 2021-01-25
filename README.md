# Description

Système de contrôle pour un véhicule robotique fonctionnant sous Raspberry Pi.
Interface de contrôle moteur: Cytron HAT-MDD10.
Écrit in python3.

Testé avec les versions suivantes;

	Raspbian stretch - 2018-11-13-raspbian-stretch-lite
	Raspbian buster - 2019-06-20-raspbian-buster-lite
	Raspbian buster - 2020-05-27-raspios-buster-lite
	Raspberry Pi OS Lite - January 11th 2021

4 programmes sont disponibles:

	Contrôle moteur - rover_control_module_UDP.py
	Commandes système - rover_system_module_TCP.py
	Serveur video - rover_video_module_TCP.py
	Script de démarrage - start.py

# Installation et configuration

Étape 1 - configuration du RaspberryPi

	$ sudo raspi-config
	Advanced options - Expand file system
	Interface options - Enable camera 
	
Étape 2 - installation des composantes logicielles requises

	sudo apt-get install python3-rpi.gpio 
    	sudo apt-get install python3-picamera
    	sudo apt-get install git

Étape 3 - Créer un répertoire /rover et attribuer la propriété à l'utilisateur pi

	$ sudo -s
	$ cd /
	$ mkdir /rover
	$ chown pi:pi /rover
	$ exit

Étape 4 - Cloner le repo 

	$ cd /rover
	$ git clone https://github.com/framboiserobot/modules_vehicule

Les fichiers suivants seront présents dans le répertoire /rover/modules_vehicule

	README.md
	rover_control_module_UDP.py
	rover_system_module_TCP.py
	rover_video_module_TCP.py
	start.py

Étape 5 - Activer le droit d'exécution pour les scripts

	$ cd /rover/modules_vehicule
	$ chmod +x *.py

Étape 6 - Assigner le script de démarrage au service cron
	
	$ crontab -e

Ajouter la ligne suivantes

	@reboot /rover/modules_vehicule/start.py

Étape 7 - Redémarrer

Les programmes seront executés au prochain démarrage.
