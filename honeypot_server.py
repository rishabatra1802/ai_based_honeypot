import socket
import threading
import json
from datetime import datetime
from utils.logger import log_event

FAKE_SERVICES = {
    'HTTP': 8080,
    'SSH': 2222
}

def handle_client(client_socket, addr, service):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {
        "ip": addr[0],
        "port": addr[1],
        "service": service,
        "timestamp": timestamp
    }
    log_event(data)
    print(f"[+] Connection logged from {addr[0]}:{addr[1]} on {service}")

    try:
        client_socket.send(f"{service} honeypot ready...\n".encode())
    except:
        pass
    client_socket.close()

def start_server(service, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', port))
    server.listen(5)
    print(f"[+] Honeypot listening on {service} port {port}...")

    while True:
        client_socket, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, addr, service))
        thread.start()

if __name__ == "__main__":
    for service, port in FAKE_SERVICES.items():
        thread = threading.Thread(target=start_server, args=(service, port))
        thread.start()
