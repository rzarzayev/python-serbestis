import socket

def simple_honeypot(host="0.0.0.0", port=8080):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Honeypot çalışır: {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Gələn əlaqə: {client_address}")
        client_socket.send(b"Xoş gəlmisiniz!\n")
        client_socket.close()

if __name__ == "__main__":
    simple_honeypot()
