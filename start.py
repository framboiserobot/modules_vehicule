#!/usr/bin/python3
import os

os.system('/rover/modules_vehicule/rover_system_module_TCP.py &')
os.system('/rover/modules_vehicule/rover_control_module_UDP.py &')
os.system('/rover/modules_vehicule/rover_video_module_TCP.py &')
