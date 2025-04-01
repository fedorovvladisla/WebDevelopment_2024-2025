import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Сервер запущен и ожидает подключения...")

    conn, addr = server_socket.accept()
    print(f"Подключение от {addr}")

    message_from_client = conn.recv(1024).decode()
    print(f"Сообщение от клиента: {message_from_client}")

    response_message = "Hello, client"
    conn.send(response_message.encode())
    print("Сообщение отправлено клиенту.")

    conn.close()
    server_socket.close()

if __name__ == "__main__":
    start_server()
