import socket


target_host = "127.0.0.1"
target_port = 4444

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"Hello server!")

respone = client.recv(1024)

print(response.decode())
client.close()
