import socket

def main():
    host = 'localhost'
    port = 12345

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    base = input("Введите основание параллелограмма: ")
    height = input("Введите высоту параллелограмма: ")

    client_socket.send(f"{base} {height}".encode())

    result = client_socket.recv(1024).decode()
    print(result)

    client_socket.close()

if __name__ == "__main__":
    main()
