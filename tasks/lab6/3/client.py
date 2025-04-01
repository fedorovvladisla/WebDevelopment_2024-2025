import socket

HOST = '127.0.0.1'
PORT = 12345

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))

    request = "GET / HTTP/1.1\r\nHost: {}\r\n\r\n".format(HOST)
    client_socket.sendall(request.encode('utf-8'))

    response = b""
    while True:
        chunk = client_socket.recv(1024)
        if not chunk:
            break
        response += chunk

    print("Ответ от сервера:")
    print(response.decode('utf-8'))
