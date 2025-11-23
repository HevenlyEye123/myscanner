import socket

target = "127.0.0.1"
ports = [21, 22, 80, 443, 8080]

print(f"Scanning {target}...")

for port in ports:
    s = socket.socket()
    s.settimeout(0.5)
    try:
        s.connect((target, port))
        print(f"Port {port} OPEN")
    except:
        pass
