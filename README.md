# modules_vehicule

Système de contrôle pour un véhicule robotique fonctionnant sous Raspberry Pi

Testé avec Raspbian Stretch sur un Raspberry Pi 3 B+.

Interface de contrôle moteur: Cytron HAT-MDD10.

Écrit in python3.

4 programmes sont disponibles:

	Contrôle moteur - rover_control_module_UDP.py
	Commandes système - rover_system_module_TCP.py
	Serveur video - rover_video_module_TCP.py
	Script de démarrage - start.py

Étape 1 - Créer un répertoire /rover et attribuer la propriété à l'utilisateur pi

	$ sudo -s
	$ cd /
	$ mkdir /rover
	$ chown pi:pi /rover
	$ exit

Étape 2 - Cloner le repo 

	$ cd /rover
	$ git clone https://github.com/framboiserobot/modules_vehicule

Les fichiers suivants seront présents dans le répertoire /rover/modules_vehicule

	README.md
	rover_control_module_UDP.py
	rover_system_module_TCP.py
	rover_video_module_TCP.py
	start.py

Étape 3 - Activer le droit d'exécution pour les scripts

	$ cd /rover/modules_vehicule
	$ chmod +x *.py

Étape 4 - Assigner le script de démarrage au service cron
	
	$ crontab -e

Ajouter la ligne suivantes

	@reboot /rover/modules_vehicule/start.py
	
Étape 5 - Redémarrer

Les programmes seront executés au prochain démarrage.
