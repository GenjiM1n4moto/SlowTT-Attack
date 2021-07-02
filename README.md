# SlowTT-Attack
Refering to the Paper SlowTT A Slow Denial of Service Against IoT Networks, I use Python3 to simulate this attack.

Requirements
Python3.9.5
paho-mqtt 1.5.1

You can just use

pip install paho-mqtt 

to install this module.

I dont write a decetion part. If you want to use detect the packet, you can use wireshark, it is very convenient.

In my code, I use mqtt5 protocol, for the paper referred that, if you want to use other broker which does not support MQTT5, you can just change the attack.py 18th row, just delete the protocol=5, the default is MQTTv311.

I use Mosquitto as my mqtt broker, and it supports MQTT5, if you dont need that, you can use activemq, too, which supports MQTTv311.

If you want to change the ip_address or other configuration, you can just change them in the net.config.

Execution.

You can just use 

python attack.py

to execute this code, or you can just use ctrl + shift + F10 in pycharm or other IDEs.

Sorry for my poor English, if you have any question, please tell me and I will reply to you as soon as possible.

[1]Vaccari, Ivan & Aiello, Maurizio & Cambiaso, Enrico. (2020). SlowTT: A Slow Denial of Service against IoT Networks. Information (Switzerland). 11. 10.3390/info11090452. 
