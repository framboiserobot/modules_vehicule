# vehiclecontrol

Système de contrôle pour un véhicule robotique fonctionnant sous Raspberry Pi

Testé avec Raspbian Stretch sur un Raspberry Pi 3 B+.

Interface de contrôle moteur: Cytron HAT-MDD10.

Écrit in python3.

4 programmes sont disponibles:

	Contrôle moteur - rover_control_module_UDP.py
	Commandes système - rover_system_module_TCP.py
	Serveur video - rover_video_module_TCP.py
	Script de démarrage - start.py

Step 1 - Créer un répertoire /rover et attribuer la propriété à l'utilisateur pi

	$ sudo -s
	$ cd /
	$ mkdir /rover
	$ chown pi:pi /rover
	$ exit

Step 2 - Cloner le repo 

	$ cd /rover
	$ git clone https://github.com/framboiserobot/vehiclecontrol

Les fichiers suivants seront présents dans le répertoire /rover/vehiclecontrol

	README.md
	rover_control_module_UDP.py
	rover_system_module_TCP.py
	rover_video_module_TCP.py
	start.py

Step 3 - Activer le droit d'exécution pour les scripts

	$ cd /rover/vehiclecontrol
	$ chmod +x *.py

Step 4 - Assigner le script de démarrage au service cron
	
	$ crontab -e

Ajouter la ligne suivantes

	@reboot /rover/vehiclecontrol/start.py
	
Step 5 - Redémarrer

Les programmes seront executés au prochain démarrage.
