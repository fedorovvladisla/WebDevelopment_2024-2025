import socket
import threading

HOST = '0.0.0.0'
PORT = 12345

clients = []

def handle_client(client_socket, address):
    print(f"Соединение установлено с {address}")
    clients.append(client_socket)

    while True:
        try:
            message = client_socket.recv(1024)
            if message:
                print(f"Получено сообщение от {address}: {message.decode('utf-8')}")
                broadcast_message(message, client_socket)
            else:
                break
        except ConnectionResetError:
            break

    print(f"Соединение с {address} закрыто")
    clients.remove(client_socket)
    client_socket.close()

def broadcast_message(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            client.send(message)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Чат-сервер запущен. Ожидание соединений на {HOST}:{PORT}")

    while True:
        client_socket, address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, address)).start()
