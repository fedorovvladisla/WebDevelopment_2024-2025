import socket

def calculate_area(base, height):
    return base * height

def main():
    host = 'localhost'
    port = 12345

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)
    print(f"Сервер запущен, слушает на {host}:{port}")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Подключено: {addr}")

        data = client_socket.recv(1024).decode()
        base, height = map(float, data.split())
        area = calculate_area(base, height)

        client_socket.send(f"Площадь параллелограмма: {area}".encode())
        client_socket.close()

if __name__ == "__main__":
    main()
