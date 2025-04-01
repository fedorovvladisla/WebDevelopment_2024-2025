import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    message = "Hello, server"
    client_socket.send(message.encode())
    print("Сообщение отправлено серверу.")

    response = client_socket.recv(1024).decode()
    print(f"Сообщение от сервера: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
